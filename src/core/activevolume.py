from src.core.voxel import voxel
from src.tools.line import line
import sys

class activevolume:

    def __init__(self, conf):

        self.x = conf.activex
        self.y = conf.activey
        self.z = conf.activez
        self.Lx = conf.activeLx
        self.Ly = conf.activeLy
        self.Lz = conf.activeLz
        self.nx = conf.activenx
        self.ny = conf.activeny
        self.nz = conf.activenz
        self.stepx = self.Lx/self.nx
        self.stepy = self.Ly/self.ny
        self.stepz = self.Lz/self.nz
        originx = self.x - self.Lx / 2.0
        originy = self.y - self.Ly / 2.0
        originz = self.z - self.Lz / 2.0
        self.tol = conf.tol
        self.activeAsAVoxel = voxel(self.x, self.y, self.z, self.Lx, self.Ly, self.Lz, 1.0)
        self.voxels = []        
        if len(conf.l) != self.nx * self.ny * self.nz:
            print('The config file is not consistent')
            sys.exit(0)
        # Creating the voxels
        for ix in range(0, self.nx):
            voxely = []
            for iy in range(0, self.ny):
                voxelz = []
                for iz in range(0, self.nz):
                    myVoxel = voxel(originx + self.stepx / 2.0 + ix * self.stepx, originy + self.stepy / 2.0 + iy * self.stepy, originz + self.stepz / 2.0 + iz * self.stepz, 
                                    self.stepx, self.stepy, self.stepz, 30000, False, 0)
                    voxelz.append(myVoxel)
                voxely.append(voxelz)
            self.voxels.append(voxely)
 
              
    def fillMuonGeometricalInformation(self, themuon):
        
        dmin, intersection, planeNumber = self.activeAsAVoxel.propagateToPlane(themuon.muonTrajectory)
  
        # This method propates the muon as a straight line 
        thepoint = intersection + themuon.muonTrajectory.v * self.tol
        current = line(thepoint, themuon.muonTrajectory.v) 
        i,j,k = self.findVoxel(thepoint)
        if i == -1 or j == -1 or k == -1:
            return False
        while k > -1:
            dmin, intersection, plane = self.voxels[i][j][k].propagateToPlane(current)
            newline = line(intersection, themuon.muonTrajectory.v)
            current = newline
            themuon.distances.append(dmin)      
            themuon.voxels.append([i, j, k])
            if plane == 0:
                if i == 0:
                    return False
                else:
                    i = i -1
            elif plane == 1:
                if i == self.nx-1:
                    return False
                else:
                    i = i + 1
            elif plane == 2:
                if j == 0:
                    return False
                else:
                    j = j - 1
            elif plane == 3:
                if j == self.ny-1:
                    return False
                else:
                    j = j + 1
            elif plane == 4:
                if k == 0:
                    return True
                else:
                    k = k - 1
            elif plane == 5:
                if k == self.nz-1:
                    return False
                else:
                    k = k + 1
        return False
           
    def findVoxel(self, point):
        for ix in range(0, self.nx):
            for iy in range(0, self.ny):
                if self.voxels[ix][iy][self.nz-1].isInside(point):
                    return ix,iy,self.nz-1
        return -1,-1,-1 


    def print(self):

        print('----------ActiveVolume----------')
        print('x:', self.x, 'y:', self.y, 'z:', self.z)
        print('Lx:', self.Lx, 'Ly:', self.Ly, 'Lz:', self.Lz)
        print('tol:', self.tol, 'step:', self.step)
        for ix in range(0, self.nx):
            for iy in range(0, self.ny):
                for iz in range(0, self.nz):
                    self.voxels[ix][iy][iz].print(ix, iy, iz)
                    

