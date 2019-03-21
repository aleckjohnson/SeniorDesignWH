#just ignore this for now

class WifiNode:
    _radius = 0
    _origin = [0, 0]
    _notAllowed = OffLimitArea([0, 0], [0, 0])

    def __init__(self, orig, rad):
        self._radius = rad
        self._origin = orig
        self._notAllowed.setArea([self._origin[0] - 0.5*self._radius, self._origin[1] - 0.5*self._radius],
                                 [self._origin[0] + 0.5*self._radius, self._origin[1] + 0.5*self._radius])

    def isInArea(self, x, y):
        return self._notAllowed.isInArea(x, y)

    def setArea(self, orig, rad):
        self._radius = rad
        self._origin = orig
        self._notAllowed.setArea([self._origin[0] - 0.5 * self._radius, self._origin[1] - 0.5 * self._radius],
                                 [self._origin[0] + 0.5 * self._radius, self._origin[1] + 0.5 * self._radius])

    def getRadius(self):
        return self._radius

    def getOriginX(self):
        return self._origin[0]

    def getOriginY(self):
        return self._origin[1]