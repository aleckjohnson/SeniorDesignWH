import pygame
import random

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
    _radius = 0
    _origin = [0, 0] #the origin point
    _notAllowed = OffLimitArea([0, 0], [0, 0]) #an area within the node where no other nodes should spawn

    def __init__(self, orig, rad):
        self._radius = rad
        self._origin = orig
        print("Created a wifi node at ", self._origin, " with a radius of ", self._radius)
        x = orig[0]
        y = orig[1]
        self._notAllowed.setArea([x - rad, y - rad], [x + rad, y + rad])

    def contains(self, x, y):
        print("Running check from node at ", self._origin)
        contains = self._notAllowed.contains(x, y)
        return contains

    def setArea(self, orig, rad):
        self._radius = rad
        self._origin = orig
        self._notAllowed.setArea([orig[0] - rad, orig[1] - rad], [orig[0] + rad, orig[1] + rad])

    def getRadius(self):
        return self._radius

    def getOriginX(self):
        return self._origin[0]

    def getOriginY(self):
        return self._origin[1]

    def getOrigin(self):
        return self._origin

size = [500, 500]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = [0, 0, 255]

radius = 20

nodeList = []
noNoSquareList = []

for i in range(random.randint(1, size[0]/10)):
    x = random.randint(0, size[0])
    y = random.randint(0, size[1])
    xdif = random.randint(19, 100)
    ydif = random.randint(19, 100)
    noNoSquareList.append(OffLimitArea([x, y], [x + xdif, y + ydif]))

cont = True
while cont:
    cont = False
    x = random.randint(0, size[0])
    y = random.randint(0, size[1])
    for o in noNoSquareList:
        if o.contains(x, y):
            cont = True
            break

nodeList.append(WifiNode([x, y], radius))

l = 0
newl = len(nodeList)

while l != newl:
    for i in range(l, newl):
        addRad = (nodeList[i].getRadius() + 1)
        for j in range(4):
            good = True

            newLoc = [nodeList[i].getOriginX(), nodeList[i].getOriginY()]
            if j == 0:
                newLoc[0] += addRad
            elif j == 1:
                newLoc[0] -= addRad
            elif j == 2:
                newLoc[1] += addRad
            else:
                newLoc[1] -= addRad

            print("Testing location ", newLoc)

            if (newLoc[0] >= 0) and (newLoc[0] <= size[0]) and (newLoc[1] >= 0) and (newLoc[1] <= size[1]):
                for o in noNoSquareList:
                    if o.contains(newLoc[0], newLoc[1]):
                        good = False
                        break
                if not good:
                    print(newLoc, " in off limits area")
                    good = False
                else:
                    for n in nodeList:
                        if (n.getOriginX() == newLoc[0]) and (n.getOriginY() == newLoc[1]):
                            print(newLoc, " already exists as a node")
                            good = False
                            break
                        elif n.contains(newLoc[0], newLoc[1]):
                            print(newLoc, " already in existing node")
                            good = False
                            break

            else:
                print(newLoc, " out of range")
                good = False

            if good:
                print(newLoc, " passed")
                obj = WifiNode(newLoc, radius)
                nodeList.append(obj)
                print("Current number of nodes: ", len(nodeList))
    l = newl
    newl = len(nodeList)



print("Nodes calculated. Prepare to print to screen!")

screen = pygame.display.set_mode(size)

# this loop is used to keep the window opened until user closes out of window
done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #this line is used to clear the window and set background color (later background will be a portion of a location on a map)
    screen.fill(WHITE)

    #draw the off limit area
    for o in noNoSquareList:
        pygame.draw.rect(screen, BLACK, pygame.Rect(o.getOrigX(), o.getOrigY(), o.getEndX() - o.getOrigX(), o.getEndY() - o.getOrigY()))

    #draw all the nodes in the list
    for n in nodeList:
        pygame.draw.circle(screen, BLUE, n.getOrigin(), n.getRadius(), 1)
        pygame.draw.circle(screen, BLUE, n.getOrigin(), 1)



    pygame.display.flip()


pygame.quit()