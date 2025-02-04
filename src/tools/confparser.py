import json



class confparser:

    def __init__(self, fileName):
        
        with open(fileName, 'r') as f:
            data = json.load(f)
        self.unix = float(data['universe']['x'])
        self.uniy = float(data['universe']['y'])
        self.uniz = float(data['universe']['z'])
        self.uniLx = float(data['universe']['Lx'])
        self.uniLy = float(data['universe']['Ly'])
        self.uniLz = float(data['universe']['Lz'])
        self.activex = float(data['active']['x'])
        self.activey = float(data['active']['y'])
        self.activez = float(data['active']['z'])
        self.activeLx = float(data['active']['Lx'])
        self.activeLy = float(data['active']['Ly'])
        self.activeLz = float(data['active']['Lz'])
        self.activenx = int(data['active']['nx'])
        self.activeny = int(data['active']['ny'])
        self.activenz = int(data['active']['nz'])
        self.tol = float(data['active']['tol'])
        self.step = float(data['active']['step'])
        self.index = []
        self.l = []
        self.fixed = []
        self.blockid = []
        for i in range(len(data['active']['voxels'])):
            blockid = int(data['active']['voxels'][i]['blockid'])
            ix = int(data['active']['voxels'][i]['ix'])
            iy = int(data['active']['voxels'][i]['iy'])
            iz = int(data['active']['voxels'][i]['iz'])
            l = float(data['active']['voxels'][i]['l'])
            self.index.append([ix, iy, iz])
            self.l.append(l)
            self.fixed.append(int(data['active']['voxels'][i]['fixed']))
            self.blockid.append(blockid)
        self.detector1x = float(data['detector1']['x'])
        self.detector1y = float(data['detector1']['y'])
        self.detector1z = float(data['detector1']['z'])
        self.detector1Lx = float(data['detector1']['Lx'])
        self.detector1Ly = float(data['detector1']['Ly'])
        self.detector1Lz = float(data['detector1']['Lz'])
        self.detector2x = float(data['detector2']['x'])
        self.detector2y = float(data['detector2']['y'])
        self.detector2z = float(data['detector2']['z'])
        self.detector2Lx = float(data['detector2']['Lx'])
        self.detector2Ly = float(data['detector2']['Ly'])
        self.detector2Lz = float(data['detector2']['Lz'])
        


