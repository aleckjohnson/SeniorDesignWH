# Implementing Drawing Shape test with python Drawing Libraries
# Last Edited on : 2/12/2019
# Modified by: Tien Phan

# Import library to be able to use draw tools
import pygame
import OffLimitArea

# this is used to load the console
pygame.init()

# setting the size of the frame or specifying a region of an area
size = [800, 640]
screen = pygame.display.set_mode(size)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = [0, 0, 255]

## can use this line to display the title, but not needed for our scope
pygame.display.set_caption("First Prototype")

# this loop is used to keep the window opened until user closes out of window
done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # this line is used to clear the window and set background color (later background will be a portion of a location on a map)
    screen.fill(WHITE)

    # draw circle
    # first row of circles
    pygame.draw.circle(screen, BLACK, [80, 80], 80, 1)
    pygame.draw.circle(screen, BLACK, [240, 80], 80, 1)
    pygame.draw.circle(screen, BLACK, [400, 80], 80, 1)
    pygame.draw.circle(screen, BLACK, [560, 80], 80, 1)
    pygame.draw.circle(screen, BLACK, [720, 80], 80, 1)
    # second row of circles
    pygame.draw.circle(screen, BLACK, [80, 240], 80, 1)
    pygame.draw.circle(screen, BLACK, [240, 240], 80, 1)
    pygame.draw.circle(screen, BLACK, [400, 240], 80, 1)
    pygame.draw.circle(screen, BLACK, [560, 240], 80, 1)
    pygame.draw.circle(screen, BLACK, [720, 240], 80, 1)
    # third row of circles
    pygame.draw.circle(screen, BLACK, [80, 400], 80, 1)
    pygame.draw.circle(screen, BLACK, [240, 400], 80, 1)
    pygame.draw.circle(screen, BLACK, [400, 400], 80, 1)
    pygame.draw.circle(screen, BLACK, [560, 400], 80, 1)
    pygame.draw.circle(screen, BLACK, [720, 400], 80, 1)
    # 4th row of circles
    pygame.draw.circle(screen, BLACK, [80, 560], 80, 1)
    pygame.draw.circle(screen, BLACK, [240, 560], 80, 1)
    pygame.draw.circle(screen, BLACK, [400, 560], 80, 1)
    pygame.draw.circle(screen, BLACK, [560, 560], 80, 1)
    pygame.draw.circle(screen, BLACK, [720, 560], 80, 1)

    ###########################
    # first row
    pygame.draw.circle(screen, BLUE, [0, 0], 80, 1)
    pygame.draw.circle(screen, BLUE, [160, 0], 80, 1)
    pygame.draw.circle(screen, BLUE, [320, 0], 80, 1)
    pygame.draw.circle(screen, BLUE, [480, 0], 80, 1)
    pygame.draw.circle(screen, BLUE, [640, 0], 80, 1)
    pygame.draw.circle(screen, BLUE, [800, 0], 80, 1)
    # second row
    pygame.draw.circle(screen, BLUE, [0, 160], 80, 1)
    pygame.draw.circle(screen, BLUE, [160, 160], 80, 1)
    pygame.draw.circle(screen, BLUE, [320, 160], 80, 1)
    pygame.draw.circle(screen, BLUE, [480, 160], 80, 1)
    pygame.draw.circle(screen, BLUE, [640, 160], 80, 1)
    pygame.draw.circle(screen, BLUE, [800, 160], 80, 1)
    # third row
    pygame.draw.circle(screen, BLUE, [0, 320], 80, 1)
    pygame.draw.circle(screen, BLUE, [160, 320], 80, 1)
    pygame.draw.circle(screen, BLUE, [320, 320], 80, 1)
    pygame.draw.circle(screen, BLUE, [480, 320], 80, 1)
    pygame.draw.circle(screen, BLUE, [640, 320], 80, 1)
    pygame.draw.circle(screen, BLUE, [800, 320], 80, 1)
    # 4th row
    pygame.draw.circle(screen, BLUE, [0, 480], 80, 1)
    pygame.draw.circle(screen, BLUE, [160, 480], 80, 1)
    pygame.draw.circle(screen, BLUE, [320, 480], 80, 1)
    pygame.draw.circle(screen, BLUE, [480, 480], 80, 1)
    pygame.draw.circle(screen, BLUE, [640, 480], 80, 1)
    pygame.draw.circle(screen, BLUE, [800, 480], 80, 1)
    # 5th row
    pygame.draw.circle(screen, BLUE, [0, 640], 80, 1)
    pygame.draw.circle(screen, BLUE, [160, 640], 80, 1)
    pygame.draw.circle(screen, BLUE, [320, 640], 80, 1)
    pygame.draw.circle(screen, BLUE, [480, 640], 80, 1)
    pygame.draw.circle(screen, BLUE, [640, 640], 80, 1)
    pygame.draw.circle(screen, BLUE, [800, 640], 80, 1)

    #####################################
    # first row
    pygame.draw.circle(screen, BLACK, [80, 80], 1)
    pygame.draw.circle(screen, BLACK, [240, 80], 1)
    pygame.draw.circle(screen, BLACK, [400, 80], 1)
    pygame.draw.circle(screen, BLACK, [560, 80], 1)
    pygame.draw.circle(screen, BLACK, [720, 80], 1)
    # second row
    pygame.draw.circle(screen, BLACK, [80, 240], 1)
    pygame.draw.circle(screen, BLACK, [240, 240], 1)
    pygame.draw.circle(screen, BLACK, [400, 240], 1)
    pygame.draw.circle(screen, BLACK, [560, 240], 1)
    pygame.draw.circle(screen, BLACK, [720, 240], 1)
    # third row
    pygame.draw.circle(screen, BLACK, [80, 400], 1)
    pygame.draw.circle(screen, BLACK, [240, 400], 1)
    pygame.draw.circle(screen, BLACK, [400, 400], 1)
    pygame.draw.circle(screen, BLACK, [560, 400], 1)
    pygame.draw.circle(screen, BLACK, [720, 400], 1)
    # 4th row
    pygame.draw.circle(screen, BLACK, [80, 560], 1)
    pygame.draw.circle(screen, BLACK, [240, 560], 1)
    pygame.draw.circle(screen, BLACK, [400, 560], 1)
    pygame.draw.circle(screen, BLACK, [560, 560], 1)
    pygame.draw.circle(screen, BLACK, [720, 560], 1)
    # 5th row
    pygame.draw.circle(screen, BLACK, [80, 720], 1)
    pygame.draw.circle(screen, BLACK, [240, 720], 1)
    pygame.draw.circle(screen, BLACK, [400, 720], 1)
    pygame.draw.circle(screen, BLACK, [560, 720], 1)
    pygame.draw.circle(screen, BLACK, [720, 720], 1)
    #############
    # first row
    pygame.draw.circle(screen, BLACK, [0, 0], 1)
    pygame.draw.circle(screen, BLACK, [160, 0], 1)
    pygame.draw.circle(screen, BLACK, [320, 0], 1)
    pygame.draw.circle(screen, BLACK, [480, 0], 1)
    pygame.draw.circle(screen, BLACK, [640, 0], 1)
    pygame.draw.circle(screen, BLACK, [800, 0], 1)
    # second row
    pygame.draw.circle(screen, BLACK, [0, 160], 1)
    pygame.draw.circle(screen, BLACK, [160, 160], 1)
    pygame.draw.circle(screen, BLACK, [320, 160], 1)
    pygame.draw.circle(screen, BLACK, [480, 160], 1)
    pygame.draw.circle(screen, BLACK, [640, 160], 1)
    pygame.draw.circle(screen, BLACK, [800, 160], 1)
    # 3rd row
    pygame.draw.circle(screen, BLACK, [0, 320], 1)
    pygame.draw.circle(screen, BLACK, [160, 320], 1)
    pygame.draw.circle(screen, BLACK, [320, 320], 1)
    pygame.draw.circle(screen, BLACK, [480, 320], 1)
    pygame.draw.circle(screen, BLACK, [640, 320], 1)
    pygame.draw.circle(screen, BLACK, [800, 320], 1)
    # 4th row
    pygame.draw.circle(screen, BLACK, [0, 480], 1)
    pygame.draw.circle(screen, BLACK, [160, 480], 1)
    pygame.draw.circle(screen, BLACK, [320, 480], 1)
    pygame.draw.circle(screen, BLACK, [480, 480], 1)
    pygame.draw.circle(screen, BLACK, [640, 480], 1)
    pygame.draw.circle(screen, BLACK, [800, 480], 1)
    # 5th row
    pygame.draw.circle(screen, BLACK, [0, 800], 1)
    pygame.draw.circle(screen, BLACK, [160, 800], 1)
    pygame.draw.circle(screen, BLACK, [320, 800], 1)
    pygame.draw.circle(screen, BLACK, [480, 800], 1)
    pygame.draw.circle(screen, BLACK, [640, 800], 1)
    pygame.draw.circle(screen, BLACK, [800, 800], 1)

    # this line is used to display the drawings on the screen
    pygame.display.flip()

# this line exits the program
pygame.quit()



