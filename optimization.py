#The purpose of this file is to optimize the program by any means necessary.

from PIL import Image
import tkinter as tk
from tkinter import messagebox


# OSMNX imports
import sys		# For reading arguments from the command line.
import networkx as nx
import osmnx as ox
import requests
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, Polygon
from  matplotlib.collections import PatchCollection

import time

# PyGame imports
#import pygame
import math

# Zoom function. Still needs to be implemented.
# Find a way to pull from mouse (pynput library?) or zoom in and out using pygame. 
st = time.time()
if(len(sys.argv) < 4):
	sys.exit("One of the following is missing: City, State, or Country.")


backend = matplotlib.get_backend()
def zoom(location_point):
	G2 = ox.graph_from_point(location_point, distance=500, distance_type='bbox', network_type='all_private')
	G2 = ox.project_graph(G2)
	fig, ax = ox.plot_graph(G2, node_size=30, node_color='#66cc66', save=True)
	

sqrMeters = 0.0

# Read in arguments from the command line and grab the corresponding area.
def makeGraph(city, state, country):
    G = ox.graph_from_place(city+','+state+','+country, network_type='all_private')
    fig, ax = ox.plot_graph(G, node_size=0, save=True, show=False)
    proj = ox.project_graph(G)
    gdfs = ox.graph_to_gdfs(proj, edges=False)
    return gdfs.unary_union.convex_hull.area


sqrMeters = makeGraph(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))

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

ratio = float(im.size[1])/float(im.size[0])

temp = float(sqrMeters) / float(ratio)
x = math.sqrt(temp)
ppm = float(im.size[0])/x
pixPerKM = ppm*float(1000) #Pixels per kilometer conversion

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



frequency = float(2400)

print(str(pixPerKM))
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
i = 0
patches = []            # Patches list
# Iterate through nodes and generate circles for each.
for n in nodeList:
    i += 1
    print(str(round((float(i)/float(totalNodes))*100.00, 2))+"%                   ", end='\r')      # Update percentage.
    c1 = Circle(n.getOrigin(), radius = max(int(n.getRad80() * pixPerKM), 1), color='#DD4420')       # Creastes a matplot circle with a center of getOrigin(), radius, and color. Mostly reused from Star's code.
    c2 = Circle(n.getOrigin(), radius = 1, color='#0000FF')
    patches.extend([c1, c2])                            # extend allows multiple variables to be appended to a list.

# Plot data

fig, ax = plt.subplots()                                              # Create figure ax of subplots
p = PatchCollection(patches, match_original=False, alpha=0.4)         # Assigns PatchCollection() and feeds the collection of patches (2D Artists--graphical primatives) and alpha (transparancy) value.
img = plt.imread("images/temp.png")         # Reads in the desired image background using plt.imread.
ax.add_collection(p)                        # Adds the collecttion to the figure ax, which allows the circles to be plotted.
plt.axis('off')                             # Disables axes.
ax.imshow(img, aspect='equal')              # Tells the figure to display the image with equal aspect
plt.show()                                  # Prints the image and circles specified above to the screen.

# Generate node costs

ciscoCost = totalNodes * 3000
ruckusCost = totalNodes * 3500
print("The Estimated Associated cost for "+str(totalNodes)+" Nodes is: Cisco Aironet 1572EAC: $"+str(ciscoCost)+" Ruckus T811-CM: $"+str(ruckusCost))
et = time.time()
root = tk.Tk()
root.withdraw()
messagebox.showinfo("Estimated Costs", "The Estimated Associated cost for "+str(totalNodes)+" Nodes is: Cisco Aironet 1572EAC: $"+str(ciscoCost)+" Ruckus T811-CM: $"+str(ruckusCost))
print("Total time in minutes = " + str((et - st) / 60))
