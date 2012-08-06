# -*- coding: utf-8 -*-
import copy

class System(object):

    def __init__(self, **kwargs):
        pass

    def get_lifetime(self, *args, **kwargs):
        raise NotImplementedError

    def reconfigure(self, *args, **kwargs):
        raise NotImplementedError

class SerialMC(object):
    system = None
    
    def on_exit(self, samplers, step, dt, old_cfg, new_cfg):
        pass

    def run(self, steps, smpl_classes, **kwargs):
        samplers = [cls(steps, **kwargs) for cls in smpl_classes]
        walker = self.system(**kwargs)
        for step in xrange(steps):
            dt = walker.get_lifetime(**kwargs)
            old_cfg = copy.deepcopy(walker)
            walker.reconfigure()
            self.sample(samplers, step, dt, old_cfg, walker)
        self.on_exit(samplers, step, dt, old_cfg, walker)
        return samplers
            

    def sample(self, samplers, step, dt, old_cfg, new_cfg):
        """ Sygnalizuje wszystkim samplerom zawartym w liście 'samplers', że można by coś
         w końcu policzyć - wywołuje po kolei każdego, podając mu na wejściu informacje.

         Każdy z samplerów powinien lokalnie zarządzać pamięcią - obiekty te są lokalnie 
         (w sensie na poziomie wątku MPI) tworzone i trzymane przez cały czas pracy symulacji.

         """
        for sampler in samplers:
            sampler.sample(step, dt, old_cfg, new_cfg)






