import math

class WifiNode:
    #a circle representing the wifi node
    _origin = [0, 0] #the origin point
    _frequecy = 0 #input frequency in MHz
    #all rads in km
    _rad30 = 0 #Best Coverage
    _rad67 = 0 #Good Coverage
    _rad70 = 0 #Okay Coverage
    _rad80 = 0 #Bad Coverage
    _rad90 = 0 #unusable coverage

    _piPerKM = 0

    def __init__(self, orig, freq, ppk):
        self._frequency = freq
        self._origin = orig
        print("Created a wifi node at ", self._origin, " with a frequency of ", self._frequency,"MHz")
        self._piPerKM = ppk
        self._rad30 = math.pow(float(10),
                               (float(30) - float(32.44) - (float(20)*math.log10(self._frequency)))/float(20))
        self._rad67 = math.pow(float(10),
                               (float(67) - float(32.44) - (float(20) * math.log10(self._frequency))) / float(20))
        self._rad70 = math.pow(float(10),
                               (float(70) - float(32.44) - (float(20) * math.log10(self._frequency))) / float(20))
        self._rad80 = math.pow(float(10),
                               (float(80) - float(32.44) - (float(20) * math.log10(self._frequency))) / float(20))
        self._rad90 = math.pow(float(10),
                               (float(90) - float(32.44) - (float(20) * math.log10(self._frequency))) / float(20))

    def setArea(self, orig, freq, ppk):
        self._frequency = freq
        self._origin = orig
        print("Changed a wifi node at ", self._origin, " with a frequency of ", self._frequency, "MHz")
        self._piPerKM = ppk
        self._rad30 = math.pow(float(10),
                               (float(30) - float(32.44) - (float(20) * math.log10(self._frequency))) / float(20))
        self._rad67 = math.pow(float(10),
                               (float(67) - float(32.44) - (float(20) * math.log10(self._frequency))) / float(20))
        self._rad70 = math.pow(float(10),
                               (float(70) - float(32.44) - (float(20) * math.log10(self._frequency))) / float(20))
        self._rad80 = math.pow(float(10),
                               (float(80) - float(32.44) - (float(20) * math.log10(self._frequency))) / float(20))
        self._rad90 = math.pow(float(10),
                               (float(90) - float(32.44) - (float(20) * math.log10(self._frequency))) / float(20))

    def getFrequency(self):
        return self._frequency

    def getRad30(self):
        return self._rad30

    def getRad67(self):
        return self._rad67

    def getRad70(self):
        return self._rad70

    def getRad80(self):
        return self._rad80

    def getRad90(self):
        return self._rad90

    def getOriginX(self):
        return self._origin[0]

    def getOriginY(self):
        return self._origin[1]

    def getOrigin(self):
        return self._origin
