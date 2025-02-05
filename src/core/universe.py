from src.core.activevolume import activevolume
from src.tools.vector import vector
from src.tools.line import line
import sys

class universe:

    # This class handles all the elements of the geometrical universe.
    # The universe is composed by an active volume that contains the voxels and the detectors
   
    def __init__(self, conf, activeVol, detectors):

        self.x = conf.unix
        self.y = conf.uniy
        self.z = conf.uniz
        self.Lx = conf.uniLx
        self.Ly = conf.uniLy
        self.Lz = conf.uniLz

        if self.x - self.Lx / 2.0 > activeVol.x - activeVol.Lx / 2.0:
            print('The active volume is not contained in the universe')
            sys.exit()
        if self.y - self.Ly / 2.0 > activeVol.y - activeVol.Ly / 2.0:
            print('The active volume is not contained in the universe')
            sys.exit()
        if self.z - self.Lz / 2.0 > activeVol.z - activeVol.Lz / 2.0:
            print('The active volume is not contained in the universe')
            sys.exit()
   
        self.activeVol = activeVol
        self.detectors = detectors
        self.opacityMap = opacityMap


  
    def print(self):
        print('------------------Universe----------------')
        print('x:', self.x, 'y:', self.y, 'z:', self.z)
        print('Lx:', self.Lx, 'Ly:', self.Ly, 'Lz:', self.Lz)
        self.activeVol.print()
        for index, det in enumerate(self.detectors):
            det.print(index)
            


 

