from PIL import Image
from tkinter import messagebox

# OSMNX imports
import sys		# For reading arguments from the command line.
import networkx as nx
import osmnx as ox
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors

# PyGame imports
import pygame

import math

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

#import WifiNode

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


im = Image.open("images/temp.png")
pix = im.load()
size = [im.size[0], im.size[1]]

nodeList = []
noNoSquareList = []
streets = []

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

populated = []
for x in range(size[0]):
    newArr = []
    for y in range(size[1]):
        newArr.append(False)
    populated.append(newArr)

#read pixels
for y in range(size[1]):
    for x in range(size[0]):
        if pix[x, y][0] == 255 and pix[x, y][1] == 255 and pix[x, y][2] == 255:
            continue
        if populated[x][y]:
            continue
        else:
            newLoc = [x, y]
            nodeList.append(WifiNode(newLoc, frequency, pixPerKM))
            lenny = len(nodeList)
            print("Current number of nodes: ", lenny)
            lenny -= 1
            node = nodeList[lenny]
            marg = int(node.getRad80() * pixPerKM)
            for tempx in range(max(0, x - marg), min(size[0], x + marg + 1)):
                for tempy in range(max(0, y - marg), min(size[1], y + marg + 1)):
                    populated[tempx][tempy] = True

print("Nodes calculated. Prepare to print to screen!")
totalNodes = len(nodeList)

screen = pygame.display.set_mode(size)
back = pygame.image.load("images/temp.png")		# Image saved from previous run.
surface = pygame.Surface(size, pygame.SRCALPHA, 32)

# this loop is used to keep the window opened until user closes out of window
done = False
clock = pygame.time.Clock()

surfaces = []
#this line is used to clear the window and set background color (later background will be a portion of a location on a map)
screen.fill(WHITE)


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
messagebox.showinfo("Estimated Costs", "The Estimated Associated cost for "+str(totalNodes)+" Nodes is: Cisco Aironet 1572EAC: $"+str(ciscoCost)+" Ruckus T811-CM: $"+str(ruckusCost))
while not done:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()

