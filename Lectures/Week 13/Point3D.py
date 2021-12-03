class Point3D:
    def __init__(self, x=0, y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return 'Point3D(' + str(self.x) +',' \
        + str(self.y) + ', ' + str(self.z)+ ')'