# -*- coding: utf-8 -*-

class Sampler(object):
    
    def __init__(self, steps, **kwargs):
        self.steps = steps

        self.initialize()

    def initialize(self):
        pass

    def sample(self, step, dt, old_cfg, new_cfg, *args, **kwargs):
        """" Use the data provided in args and do something! """
        raise NotImplementedError

    @classmethod
    def merge(cls, results, prob, steps, repeats, **kwargs):
        """ This will be called at the end of calculations """
        raise NotImplementedError
