from src.tools.line import line


class muon:

    def __init__(self, p, v, index, partition):

        self.muonTrajectory = line(p, v)
        self.index = index
        self.partition = partition
        self.distances = []
        self.voxels = []
       

    def print(self, tag):

        print('[Muon ' + tag + ']')
        print('Muon trajectory: ', '(' + str(self.muonTrajectory.p.x()) + ', ' + str(self.muonTrajectory.p.y()) + ', ' + str(self.muonTrajectory.p.z()) + ') + l (' + str(self.muonTrajectory.v.x()) + ', ' + str(self.muonTrajectory.y()) + ', ' + str(self.muonTrajectory.z()) + ')')
        for i, d in enumerate(self.distances):
            print('Distance:', self.distances[i], 'Voxel: ', self.voxels[i])
