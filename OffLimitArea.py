#just ignore this for now



class OffLimitArea:
    _origin = [0, 0]
    _end = [0, 0]

    def __init__(self, orig, en):
        self._origin = orig
        self._end = en

    def setArea(self, orig, en):
        self._origin = orig
        self._end = en

    def isInArea(self, x, y):
        if (x < self._origin[0] or x > self._end[0]) and (y < self._origin[1] or y > self._end[1]):
            return True
        else:
            return False

    def getOrigX(self):
        return self._origin[0]

    def getOrigY(self):
        return self._origin[1]

    def getEndX(self):
        return self._end[0]

    def getEndY(self):
        return self._end[1]