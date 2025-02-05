from src.core.muon import muon
from src.tools.line import line
from src.tools.vector import vector
from src.tools.confparser import confparser

import pandas as pd
import np as np

class detector:

    def __init__(self, conf, index, activeVolume, opacityMap):

        self.index = index
        self.x = conf.detector[index].x
        self.y = conf.detector[index].y
        self.z = conf.detector[index].z
        self.Lx = conf.detector[index].Lx
        self.Ly = conf.detector[index].Ly
        self.Lz = conf.detector[index].Lz
        self.nx = conf.detector[index].nx
        self.ny = conf.detector[index].ny
        self.openSkyDatasetName = conf.detector[index].openSkyDataset
        self.WorkDatasetName = conf.detector[index].WorkDataset
        self.OutputopenSkyDatasetName = conf.detector[index].OutputopenSkyDataset
        self.OutputWorkDatasetName = conf.detector[index].OutputWorkDataset
        self.activeVolume = activeVolume
        self.opacityMap = opacityMap
        self.stepX = self.Lx/self.nx
        self.stepY = self.Ly/self.ny
        self.partitionLimits = []
        for i in range(0, self.nx):
            for j in range(0, self.ny):
                limits = [-self.Lx/2.0 + i * self.stepX, -self.Lx/2.0 + (i+1) * self.stepX, -self.Ly/2.0 + j * self.stepY, -self.Ly/2.0 + (j+1) * self.stepY]
                self.partitionLimits(limits)

    def readAndTransformDatasets(self):

        self.readAndTransformDataset(self.openSkyDatasetName, self.OutputopenSkyDatasetName)
        self.readAndTransformDataset(self.WorkDatasetName, self.OutputWorkDatasetName)

    def readAndTransformDataset(self, input, output):
        
        dataset= pd.read_csv(input)
        outputDataset = pd.DataFrame(columns=('x', 'y', 'z', 'vx', 'vy', 'vz', 'det', 'partition'))

        for index, row in dataset.iterrows():
            r = np.asarray([row['x'], row['y'], row['z']])
            v = np.asarray([row['vx'], row['vy'], row['vz']])
            partition = -1
            for i, l in enumerate(self.partitionLimits):
                if r[0] > l[0] and r[0] <= l[1] and r[1] > l[2] and r[1] <= l[3]:
                    partition = i
                    break           
            globalr = self.toGlobal(r)
            globalv = self.toGlobal(v)
            mu = muon(globalr, globalv, self.index, partition)
            self.activeVolume.fillMuonGeometricalInformation(mu)
            

   

    def print(self, tag):
        print('-----Detector ', tag, '------')
        print('x:', self.x, 'y:', self.y, 'z:', self.z)
        print('Lx:', self.Lx, 'Ly:', self.Ly, 'Lz:', self.Lz)