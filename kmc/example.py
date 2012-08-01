from optparse import OptionParser
from parallel import ParallelMC
from serial import SerialMC, System
from sampler import Sampler

parser = OptionParser()
parser.add_option('-s', '--steps', type='int', help='MC steps to go')
parser.add_option('-r', '--runs', type='int', help='MC runs')
parser.add_option('-p', '--path', type='string', help="Result path")


class MySystem(System):

    def get_lifetime(self, *args, **kwargs):
        return 1

    def reconfigure(self, *args, **kwargs):
        pass

class MySampler(Sampler):

    def sample(self, step, dt, old_cfg, new_cfg, *args, **kwargs):
        pass

    @classmethod
    def merge(cls, results, steps, repeats, **kwargs):
        pass


class MySerialMC(SerialMC):
    system = MySystem

if __name__=='__main__':
    (options, args) = parser.parse_args()
    # path is some extra argument, steps and repeats are required
    ParallelMC().run(steps=options.steps, repeats=options.runs, run_cls=MySerialMC, smpl_classes=[MySampler], path=options.path)



