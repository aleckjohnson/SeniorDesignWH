# OSMNX imports
import sys		# For reading arguments from the command line.
import networkx as nx
import osmnx as ox
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors

# PyGame imports
import pygame
import random
import math
import ctypes  # An included library with Python install.

# Zoom function. Still needs to be implemented.
# Find a way to pull from mouse (pynput library?) or zoom in and out using pygame. 

if(len(sys.argv) < 4):
	sys.exit("One of the following is missing: City, State, or Country.")

def zoom(location_point):
	G2 = ox.graph_from_point(location_point, distance=500, distance_type='bbox', network_type='all_private')
	G2 = ox.project_graph(G2)
	fig, ax = ox.plot_graph(G2, node_size=30, node_color='#66cc66', save=True)
	

# Read in arguments from the command line and grab the corresponding area.
def makeGraph(city, state, country):
	G = ox.graph_from_place(city+','+state+','+country, network_type='all_private')
	fig, ax = ox.plot_graph(G, node_size=0, save=True)


makeGraph(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))


#import OffLimitArea
class OffLimitArea:
    #A rectangle that nothing is allowed inside of
    _origin = [0, 0] #top left corner
    _end = [0, 0] #bottom right corner

    def __init__(self, orig, en):
        self._origin = orig
        self._end = en
        #print ("Area off limits within", self._origin, "and", self._end)

    def setArea(self, orig, en):
        self._origin = orig
        self._end = en
        print("New area off limits within", self._origin, "and", self._end)

    def contains(self, x, y):
        #is the specified point within the defined area? if yes return true, otherwise return false
        print("Running check in area between ", self._origin, " and ", self._end)
        if (x >= self._origin[0]) and (x <= self._end[0]):
            if (y >= self._origin[1]) and (y <= self._end[1]):
                return True
            else:
                return False
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

#import WifiNode

class WifiNode:
    #a circle representing the wifi node
    _origin = [0, 0] #the origin point
    _notAllowed = OffLimitArea([0, 0], [0, 0]) #an area within the node where no other nodes should spawn
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
        x = orig[0]
        y = orig[1]
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
        marg = int(self._rad80 * self._piPerKM)
        self._notAllowed.setArea([x - marg, y - marg], [x + marg, y + marg])


    def contains(self, x, y):
        print("Running check from node at ", self._origin)
        contains = self._notAllowed.contains(x, y)
        return contains

    def setArea(self, orig, freq, ppk):
        self._frequency = freq
        self._origin = orig
        print("Changed a wifi node at ", self._origin, " with a frequency of ", self._frequency, "MHz")
        self._piPerKM = ppk
        x = orig[0]
        y = orig[1]
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
        marg = int(self._rad80 * self._piPerKM)
        self._notAllowed.setArea([x - marg, y - marg], [x + marg, y + marg])

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

size = [750, 750]
WHITE = [255, 255, 255, 255]
BLACK = [0, 0, 0, 255]
BLUE = [0, 0, 255, 255]
PURPLE = [255, 0, 255, 255]
GREEN = [0, 255, 0, 50]
YELLOW = [255, 255, 0, 50]
GOLD = [255, 204, 0, 50]
REDORANGE = [255, 51, 0, 50]
RED = [255, 0, 0, 50]

pixPerKM = 100 #Pixels per kilometer conversion
frequency = float(2400)


nodeList = []
noNoSquareList = []

for i in range(random.randint(int(size[0]/20), int(size[0]/10))):
    x = random.randint(0, size[0])
    y = random.randint(0, size[1])
    xdif = random.randint(19, 100)
    ydif = random.randint(19, 100)
    noNoSquareList.append(OffLimitArea([x, y], [x + xdif, y + ydif]))

x = 0
y = 0
cont = True
while cont:
    cont = False
    for o in noNoSquareList:
        if o.contains(x, y):
            cont = True
            break
    if cont:
        if x < size[0]:
            x += 1
        else:
            x = 0
            y += 1
        if y > size[1]:
            print("Not possible to spawn initial node")
            break

if not cont:
    nodeList.append(WifiNode([x, y], frequency, pixPerKM))

while y <= size[1]:
    addRad = max(int(nodeList[len(nodeList) - 1].getRad80() * pixPerKM), 1)
    if x < size[0]:
        x += addRad
    else:
        while x > 0:
            x -= addRad
        if x < 0:
            x += addRad
        if x > size[0]:
            x = 0
        y += addRad
    if y > size[1]:
        print("Exceeded size limit")
        break
    else:
        newLoc = [x, y]
        print("Testing location ", newLoc)
        good = True
        if (x > size[0]) or (y > size[1]):
            good = False
        else:
            for o in noNoSquareList:
                if o.contains(x, y):
                    print(newLoc, " in off limits area")
                    good = False
                    break

        if good:
            print(newLoc, " passed")
            nodeList.append(WifiNode(newLoc, frequency, pixPerKM))

        print("Current number of nodes: ", len(nodeList))
totalNodes = len(nodeList)

print("Nodes calculated. Prepare to print to screen!")

screen = pygame.display.set_mode(size)
back = pygame.image.load("images/temp.png")		# Image saved from previous run.
back = pygame.transform.scale(back, (750, 750))
surface = pygame.Surface(size, pygame.SRCALPHA, 32)

# this loop is used to keep the window opened until user closes out of window
done = False
clock = pygame.time.Clock()

surfaces = []
#this line is used to clear the window and set background color (later background will be a portion of a location on a map)
screen.fill(WHITE)

#draw the off limit area
for o in noNoSquareList:
    pygame.draw.rect(screen, BLACK, pygame.Rect(o.getOrigX(), o.getOrigY(), o.getEndX() - o.getOrigX(), o.getEndY() - o.getOrigY()))
    screen.blit(back,(0,0))
#draw all the nodes in the list
for n in nodeList:
    surf = pygame.Surface(size, pygame.SRCALPHA, 32)
    #pygame.draw.circle(surf, RED, n.getOrigin(), max(int(n.getRad90() * pixPerKM), 1))
    pygame.draw.circle(surf, REDORANGE, n.getOrigin(), max(int(n.getRad80() * pixPerKM), 1))
    pygame.draw.circle(surf, GOLD, n.getOrigin(), max(int(n.getRad70() * pixPerKM), 1))
    pygame.draw.circle(surf, YELLOW, n.getOrigin(), max(int(n.getRad67() * pixPerKM), 1))
    pygame.draw.circle(surf, GREEN, n.getOrigin(), max(int(n.getRad30() * pixPerKM), 1))
    pygame.draw.circle(surf, BLUE, n.getOrigin(), 1)
    surfaces.append(surf)

for surf in surfaces:
    screen.blit(surf, [0, 0])


pygame.display.flip()

ciscoCost = totalNodes * 3000
ruckusCost = totalNodes * 3500
print("The Estimated Associated cost for "+str(totalNodes)+" Nodes is: Cisco Aironet 1572EAC: $"+str(ciscoCost)+" Ruckus T811-CM: $"+str(ruckusCost))
ctypes.windll.user32.MessageBoxW(0, "The Estimated Associated cost for "+str(totalNodes)+" Nodes is: Cisco Aironet 1572EAC: $"+str(ciscoCost)+" Ruckus T811-CM: $"+str(ruckusCost),"Estimated Node Cost", 1)

while not done:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
