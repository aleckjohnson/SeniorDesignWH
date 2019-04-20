#The purpose of this file is to optimize the program by any means necessary.

from PIL import Image
import tkinter as tk
from tkinter import messagebox


# OSMNX imports
import sys		# For reading arguments from the command line.
import os
import networkx as nx
import osmnx as ox
import requests
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, Polygon
from  matplotlib.collections import PatchCollection
# PyGame imports
import math
import WifiNode_class as WirelessNode
import time         # For debugging only.
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
    fig, ax = ox.plot_graph(G, node_size=0, save=True, filename=city, show=False)
    proj = ox.project_graph(G)
    ox.save_graphml(proj, city+'.graphml')
    gdfs = ox.graph_to_gdfs(proj, edges=False)
    return gdfs.unary_union.convex_hull.area

if (os.path.isfile('data/'+str(sys.argv[1])+'.graphml') == False):
    sqrMeters = makeGraph(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))
else:
    proj = ox.load_graphml(str(sys.argv[1])+'.graphml')
    gdfs = ox.graph_to_gdfs(proj, edges=False)
    sqrMeters = gdfs.unary_union.convex_hull.area

try:            # If the initial reading of the image fails, run makeGraph() and reattempt to read the image.
    img = Image.open("images/"+str(sys.argv[1])+'.png')
except IOError:
    sqrMeters = makeGraph(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))
    img = Image.open("images/"+str(sys.argv[1])+'.png')

pix = img.load()
size = [img.size[0], img.size[1]]

ratio = float(img.size[1])/float(img.size[0])

temp = float(sqrMeters) / float(ratio)
x = math.sqrt(temp)
ppm = float(img.size[0])/x
pixPerKM = ppm*float(1000) #Pixels per kilometer conversion

nodeList = []
noNoSquareList = []
streets = []

# Matplotlib PatchCollection expects all colors to be expressed as rgba values from 0 to 1
WHITE = [1, 1, 1]
BLACK = [0, 0, 0]
BLUE = [0, 0, 1,]
PURPLE = [1, 0, 1]
GREEN = [0, 1, 0]
YELLOW = [1, 1, 0]
GOLD = [1, 0.8, 0]
REDORANGE = [1, 0.2, 0]
RED = [1, 0, 0]



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
            nodeList.append(WirelessNode.WifiNode(newLoc, frequency, pixPerKM))
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
    #c1 = Circle(n.getOrigin(), max(int(n.getRad90() * pixPerKM), 1), color=RED, alpha=0.6)
    c2 = Circle(n.getOrigin(), max(int(n.getRad80() * pixPerKM), 1), color=REDORANGE, alpha=0.4)       # Creates a matplot circle with a center of getOrigin(), radius, and color. Mostly reused from Star's code.
    #c3 = Circle(n.getOrigin(), max(int(n.getRad70() * pixPerKM), 1), color=GOLD, alpha=0.50)
    #c4 = Circle(n.getOrigin(), max(int(n.getRad67() * pixPerKM), 1), color=YELLOW, alpha=0.45)
    #c5 = Circle(n.getOrigin(), max(int(n.getRad30() * pixPerKM), 1), color=GREEN, alpha=0.35)
    c6 = Circle(n.getOrigin(), 1, color=BLUE, alpha=0.25)
    patches.extend([c2,c6])                            # extend allows multiple variables to be appended to a list.

# Plot data

fig, ax = plt.subplots()                                              # Create figure ax of subplots
p = PatchCollection(patches, match_original=True)         # Assigns PatchCollection() and feeds the collection of patches (2D Artists--graphical primatives) and alpha (transparancy) value.
plt.axis('off')                             # Disables axes.
ax.add_collection(p)
ax.imshow(img, aspect='equal')               # Tells the figure to display the image with equal aspect. img was read using pillow when performing calculations.
#plt.tight_layout()
et = time.time()
plt.show()                                  # Prints the image and circles specified above to the screen.

# Generate node costs

ciscoCost = totalNodes * 3000
ruckusCost = totalNodes * 3500
print("The Estimated Associated cost for "+str(totalNodes)+" Nodes is: Cisco Aironet 1572EAC: $"+str(ciscoCost)+" Ruckus T811-CM: $"+str(ruckusCost))
root = tk.Tk()
root.withdraw()
messagebox.showinfo("Estimated Costs", "The Estimated Associated cost for "+str(totalNodes)+" Nodes is: Cisco Aironet 1572EAC: $"+str(ciscoCost)+" Ruckus T811-CM: $"+str(ruckusCost))
print("Total time in minutes = " + str((et - st) / 60))
