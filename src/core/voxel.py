from src.tools.vector import vector


class voxel:

    def __init__(self, x, y, z, Lx, Ly, Lz, lrad):

        self.p = vector(x, y, z)
        self.pmin = vector(x - Lx / 2.0, y - Ly / 2.0, z - Lz / 2.0) 
        self.pmax = vector(x + Lx / 2.0, y + Ly / 2.0, z + Lz / 2.0) 
        self.lrad = lrad
        self.scattbase = (0.0136 * 0.0136) / lrad        
        
    def print(self, nx, ny, nz):

        print('------Voxel ', nx, ny, nz, '------')
        print('Position:', self.p.x(), self.p.y(), self.p.z())
        print('Size Lx:', (self.pmax.x()-self.pmin.x()), 'Size Ly:', (self.pmax.y()-self.pmin.y()), 'Size Lz:', (self.pmax.z()-self.pmin.z()))
        print('Lambda', self.lrad)


    def setLrad(self, lrad):
        self.lrad = lrad
        self.scattbase = (0.0136*0.0136) / lrad


    def isInside(self, p):

        # If p is inside the voxel returns true,
        # false otherwise.
        if p.x() <= self.pmin.x() or p.x() > self.pmax.x():
            return False 
        if p.y() <= self.pmin.y() or p.y() > self.pmax.y():
            return False 
        if p.z() <= self.pmin.z() or p.z() > self.pmax.z():
            return False 
        return True

    def propagateToPlane(self, line):

        # This method propagates a geometrical line to the
        # next closest surface of the voxel. It returns the
        # distance to the plane, the point of intersection,
        # and also the plane number
        points = [] 
        points.append(line.intersectionX(self.pmin.x()))
        points.append(line.intersectionX(self.pmax.x()))
        points.append(line.intersectionY(self.pmin.y()))
        points.append(line.intersectionY(self.pmax.y()))
        points.append(line.intersectionZ(self.pmin.z()))
        points.append(line.intersectionZ(self.pmax.z()))
         
        dmin = float('inf')
        intersection = vector(0, 0, 0)
        planeNumber = -1
        for i, po in enumerate(points):
            if po[0] > 0 and po[0] < dmin:
                dmin = po[0]
                intersection = po[1]
                planeNumber = i
        return dmin, intersection, planeNumber


    def propagateBackwardsToPlane(self, line):

        # This method is similar to propagateToPlane but 
        # it does the extrapolation backwards.           
        points = [] 
        points.append(line.intersectionX(self.pmin.x()))
        points.append(line.intersectionX(self.pmax.x()))
        points.append(line.intersectionY(self.pmin.y()))
        points.append(line.intersectionY(self.pmax.y()))
        points.append(line.intersectionZ(self.pmin.z()))
        points.append(line.intersectionZ(self.pmax.z()))
         
        dmin = float('inf')
        intersection = vector(0, 0, 0)
        planeNumber = -1
        for i, po in enumerate(points):
            if po[0] < 0 and abs(po[0]) < dmin:
                dmin = abs(po[0])
                intersection = po[1]
                planeNumber = i

        return dmin, intersection, planeNumber

  