from src.core.muon import muon
from src.tools.line import line
from src.tools.vector import vector
from src.tools.confparser import confparser
class detector:

    def __init__(self, conf, loc):

        if loc == 1:
            self.x = conf.detector1x
            self.y = conf.detector1y
            self.z = conf.detector1z
            self.Lx = conf.detector1Lx
            self.Ly = conf.detector1Ly
            self.Lz = conf.detector1Lz
        else:
            self.x = conf.detector2x
            self.y = conf.detector2y
            self.z = conf.detector2z
            self.Lx = conf.detector2Lx
            self.Ly = conf.detector2Ly
            self.Lz = conf.detector2Lz
     
    def getResponse(self, l):

        #Apply here the detector response
        distance, intersect = l.intersectionZ(self.z)
        v0 = vector(0, 0, 0)
        li = line(v0, v0)
        if intersect.x() < self.x - self.Lx / 2.0 or intersect.x() > self.x + self.Lx / 2.0:
            return False, li
        if intersect.y() < self.y - self.Ly / 2.0 or intersect.y() > self.y + self.Ly / 2.0:
            return False, li
        newline = line(intersect, l.v)
        return True, newline   

    def print(self, tag):
        print('-----Detector ', tag, '------')
        print('x:', self.x, 'y:', self.y, 'z:', self.z)
        print('Lx:', self.Lx, 'Ly:', self.Ly, 'Lz:', self.Lz)