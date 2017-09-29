

import pygame
from rect_collision import Rect_Collision as collision
from random import choice, randrange

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 102, 255)
CYAN = (0, 255, 255)
FUCHSIA = (204, 0, 102)
LT_BLUE = (0, 128, 255)
DARK_GREEN = (0,153,0)
ORANGE = (255,153,51)
GREY = (192,192,192)
DARK_GREY = (64,64,64)
LIME = (153, 255, 51)
LIPSTICK = (255, 102, 102)
LIGHT_PURPLE = (255, 153, 255)
LIGHT_GREEN =(51,255,153)
pygame.init()

# Set the width and height of the screen [width, height]
WIDTH = 700  #700
HEIGHT = 500 #500
W = WIDTH - 50
H = HEIGHT - 50
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Moving Rectangle")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
rect_x_1 = 50   #randrange(50, 650, 10)#50 #650<---top collide  #(50)
rect_y_1 = 50   #randrange(50, 450, 10)#50
rect_x_2 = 650  #randrange(50, 650, 10)#650
rect_y_2 = 50   #150#randrange(50, 450, 10)#50 #<------ 350 top collide
rect_x_3 = 250  #450#randrange(50, 650, 10)#650
rect_y_3 = 250  #200
rect_x_4 = 350
rect_y_4 = 450
x_speed = 5
y_speed = 5
switch = 1
n = 4

color_a = FUCHSIA
color_b = LT_BLUE
color_c = RED
color_d = DARK_GREEN
colors = [FUCHSIA, LT_BLUE, RED, CYAN, PURPLE, BLACK, WHITE, BLUE, DARK_GREEN, GREY, ORANGE]#, LIGHT_GREEN, LIGHT_PURPLE,
          #LIPSTICK, LIME, DARK_GREY]

shapes = []
# for i in range (n):
#     x = randrange(50, 650, 70)
#     y = randrange(50, 450, 70)
#     shape = [[x, y, 50, 50, 0], [x, y, 30, 30, 10], 5, 5]
#     shapes.append(shape)

shape = [[rect_x_1, rect_y_1, 50, 50, 0], [rect_x_1, rect_y_1, 30, 30, 10], x_speed, y_speed]
shapes.append(shape)
shape = [[rect_x_2, rect_y_2, 50, 50, 0], [rect_x_2, rect_y_2, 30, 30, 10], x_speed, y_speed]
shapes.append(shape)
shape = [[rect_x_3, rect_y_3, 50, 50, 0], [rect_x_3, rect_y_3, 30, 30, 10], x_speed, y_speed]
shapes.append(shape)
shape = [[rect_x_4, rect_y_4, 50, 50, 0], [rect_x_4, rect_y_4, 30, 30, 10], x_speed, y_speed]
shapes.append(shape)


def draw_rect(color, shape):
    [x,y,w, h, offset] = shape
    pygame.draw.rect(screen, color, [x+offset, y+offset, w, h])


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill(BLACK)
    draw_rect(WHITE, shapes[0][0])
    draw_rect(color_a, shapes[0][1])
    draw_rect(GREEN, shapes[1][0])
    draw_rect(color_b, shapes[1][1])
    draw_rect(BLUE, shapes[2][0])
    draw_rect(color_c, shapes[2][1])
    draw_rect(ORANGE, shapes[3][0])
    draw_rect(color_d, shapes[3][1])


    #Monitor for rectangles colliding with wall
    for shape in shapes:

        if shape[0][0] > W or shape[0][0] < 0:
            shape[2] = -shape[2]

        if shape[0][1] > H or shape[0][1] < 0:#and corner is not True:
           shape[3] = -shape[3]

        shape[0][0] += shape[2]
        shape[0][1] += shape[3]
        shape[1][0] += shape[2]
        shape[1][1] += shape[3]

    #check for rectangles colliding with one another
    a = collision(shapes)
    collision_type = a.collide()
    x, y = a.color()

    if collision_type == 1:
        shapes[0][2] = -shapes[0][2]
        shapes[1][2] = -shapes[1][2]
        shapes[2][2] = -shapes[2][2]
        shapes[3][2] = -shapes[3][2]


    if collision_type == 2:
        shapes[0][3] = -shapes[0][3]
        shapes[1][3] = -shapes[1][3]
        shapes[2][3] = -shapes[2][3]
        shapes[3][3] = -shapes[3][3]

    if x + y != 0:  #this statement is not necessary but keeps the loop (and print statement) from executing
                    #when there is no collision; Also the choices of 0 and 1 are NOT the block numbers but represent
                    #the list after items have been delected (see rect_collision.py for loop)
        if (x == 0 and y == 1):
            color_a = choice(colors)    #RED#colors[switch]
            color_b = choice(colors)    #RED#colors[abs(switch - 1)]
            #switch = abs(switch - 1)
        elif (x == 1 and y == 1):
            color_b = choice(colors)    #RED#colors[switch]
            color_c = choice(colors)    #RED#colors[abs(switch - 1)]
            #switch = abs(switch - 1)
        elif (x == 0 and y == 2):
            color_a = choice(colors)    #RED#colors[switch]
            color_c = choice(colors)    #RED#colors[abs(switch - 1)]
        #switch = abs(switch - 1)
        elif (x == 0 and y == 3):
            color_a = choice(colors)
            color_d = choice(colors)
        elif (x == 1 and y == 2):
            color_b = choice(colors)
            color_d = choice(colors)
        elif (x == 2 and y == 1):
            color_c = choice(colors)
            color_d = choice(colors)
        print(x,y) #debug statement


    #update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()