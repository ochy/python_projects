import pygame
import random

class Rect_Collision:
   def __init__(self, shapes):
       self.rect = []
       for shape in shapes:
           [x, y] = shape[0][0], shape[0][1]
           self.rect.append([x, y])

       self.rects = [0, 0]
       self.flag = True

   def collide(self):
        #these two FOR loops iterate through all rectangles to see if there is a collision
        for j in range(len(self.rect)):
            for i in range(len(self.rect) - 1):

                #test side collide (< 50)
                if abs(self.rect[0][0] - self.rect[i + 1][0]) <= 50 and abs(self.rect[0][1] - self.rect[i + 1][1]) < 50:
                    self.rects = [j, i+1]
                    if self.flag ==True:
                       self.color()
                       #print(self.rects[0],self.rects[1])
                       self.flag = False
                    return 1

                #test top collide ( = 50)
                if abs(self.rect[0][0] - self.rect[i + 1][0]) <= 50 and abs(self.rect[0][1] - self.rect[i + 1][1]) == 50:
                    self.rects = [j, i + 1]

                    if self.flag == True:
                       self.color()
                    #     #print(self.rects)
                       self.flag = False
                    return 2
            del self.rect[0]


   #this function returns which two rectangles have collided
   def color(self):
       return (self.rects[0], self.rects[1])



#x1, y1,x2, y2, x3, y3 = 5
x1=1
y1=10
x2=2
y2=11
x3=3
y3=12
x4=4
y4=13
i=0
rect =[[x1,y1],[x2,y2],[x3,y3]]#,[x4,y4]]

# for j in range(len(rect)):
#     for i in range (len(rect)-1):
#         if abs(rect[0][0] - rect[i + 1][0]) <= 50 and abs(rect[0][1] - rect[i + 1][1]) < 50:
#            print(j,i+1)
#         if abs(rect[0][0] - rect[i + 1][0]) <= 50 and abs(rect[0][1] - rect[i + 1][1]) == 50:
#            print(2)
#
#         #print (str(rect[0][0]) + " " + str(rect[i+1][0]) + " " + str(rect[0][1]) + " " +  str(rect[i+1][1]))
#     del rect[0]




# for j in range(len(rect)):
#     for i in range (len(rect)-1):
#         print (str(rect[0][0]) + " " + str(rect[i+1][0]) + " " + str(rect[0][1]) + " " +  str(rect[i+1][1]))
#     del rect[0]

# for j in range(2):
#     for i in range(2):
#         if abs(rect[0][0] - rect[i+1][0] <= 50 and abs(rect[0][1] - rect[i+1][1]) < 50):
#         return 1
# for rect in rectangle:
#     print (rect[0])#(rectangle[i][0])
#     i+=1


    # def top_collide(selfself):
    #     if abs(self.xpos1 - self.xpos2) <= 50 and abs(self.ypos1 - self.ypos2) == 50:
    #         return True

# a = Rect_Collision(1,2,51,4)
# print (a.collide())
# a=[-3,4,5,7,9,3,2]
# b = [x>6  or x<0 for x in a]
# print (b)
#
# for rect in rect_x:
#     if rect > 650 or rect < 0:
#         rect_change_x[rect] = -rect_change_x[rect]


#def collide(self)
# if abs(self.xpos1 - self.xpos2) <= 50 and abs(self.ypos1 - self.ypos2) < 50:
        #     return 1
        # if abs(self.xpos1 - self.xpos2) <= 50 and abs(self.ypos1 - self.ypos2) == 50:
        #     return 2
# a=1
# b=2
# c=3
# xx=[a,b,c]
# #print
# i= random.choice(xx)
# print (i)

# class Rect_Collision:
#    def __init__(self, xpos1, ypos1, xpos2, ypos2, xpos3, ypos3):
#
#        self.rect = [[xpos1, ypos1], [xpos2, ypos2], [xpos3, ypos3]]
#        self.rects = [0, 0]
#        self.flag = True
#
#    def collide(self):
#         #these two FOR loops iterate through all rectangles to see if there is a collision
#         for j in range(len(self.rect)):
#             for i in range(len(self.rect) - 1):
#
#                 #test side collide (< 50)
#                 if abs(self.rect[0][0] - self.rect[i + 1][0]) <= 50 and abs(self.rect[0][1] - self.rect[i + 1][1]) < 50:
#                     self.rects = [j, i+1]
#                     if self.flag ==True:
#                        self.color()
#                        #print(self.rects[0],self.rects[1])
#                        self.flag = False
#                     return 1
#
#                 #test top collide ( = 50)
#                 if abs(self.rect[0][0] - self.rect[i + 1][0]) <= 50 and abs(self.rect[0][1] - self.rect[i + 1][1]) == 50:
#                     self.rects = [j, i + 1]
#
#                     if self.flag == True:
#                        self.color()
#                     #     #print(self.rects)
#                        self.flag = False
#                     return 2
#             del self.rect[0]
#
#
#    #this function returns which two rectangles have collided
#    def color(self):
#        return (self.rects[0], self.rects[1])
