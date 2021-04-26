# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 18:38:59 2021

@author: sedos
"""
import sys
import pygame
from pygame.locals import *
import CUBO

# from PySide2 import QtCore, QtWidgets, QtOpenGL
# from PySide2.QtWidgets import QApplication
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (1,5,7,2),
    (6,7,5,4),
    (4,5,1,0),
    (4,0,3,6),
    )
colors = []
colors.append((1,0,0)) #red
colors.append((0,1,0)) #green
colors.append((0,0,1)) #blue
colors.append((1,1,0)) #yellow
colors.append((0,1,1)) #
colors.append((1,1,1)) #white
    

def face(color, axis):

    list = glGenLists(1)
    glNewList(list, GL_COMPILE)
    glNormal3d(0.0, 0.0, 0.0)
    
    glBegin(GL_QUADS) 
    glColor3fv(color)
    for vertex in surfaces[axis]:
        glVertex3fv(verticies[vertex])
    glEnd()
    
    glEndList()
    return list
    
def draw_shape(shape, dx, dy, dz):
    """Helper to translate, rotate and draw the shape."""
    glPushMatrix()
    glTranslated(dx, dy, dz)
    glCallList(shape)
    glPopMatrix()
    
def cube_arrangement(current):
    
    #Sequence of faces array:
    # x, x, y, y, z, z

    # Face 0
    for x in range(3):
        for y in range(3):
            x1 = -3 + (2*x)
            y1 = -3 + (2*y)
            draw_shape(face(colors[current[0][x][y]], 0), x1, y1, -3.0)
            
    # Face 1
    for x in range(3):      
        for y in range(3):
            x1 = -3 + (2*x)
            y1 = -3 + (2*y)
            draw_shape(face(colors[current[1][x][y]], 0), x1, y1, 3.0)
            
    # Face 2 
    for y in range(3):
        for z in range(3):
            y1 = -3 + (2*y)
            z1 = -3 + (2*z)
            draw_shape(face(colors[current[2][z][y]], 1), -3.0, y1, z1)
            
    # Face 3
    for y in range(3):
        for z in range(3):
            y1 = -3 + (2*y)
            z1 = -3 + (2*z)
            draw_shape(face(colors[current[3][z][y]], 1), 3.0, y1, z1)
            
    # Face 4 
    for x in range(3):
        for z in range(3):
            x1 = -3 + (2*x)
            z1 = -3 + (2*z)
            draw_shape(face(colors[current[4][x][z]], 2), x1, 1.0, z1)
            
    # Face 5 
    for x in range(3):
        for z in range(3):
            x1 = -3 + (2*x)
            z1 = -3 + (2*z)
            draw_shape(face(colors[current[5][x][z]], 2), x1, -5.0, z1)  

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(1.0,0.0, -20)
    glRotatef(180, 1, -1, 0)
    glEnable(GL_DEPTH_TEST);
    cubo1 = CUBO.cube()
  
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)      
    # glRotatef(145, 0, 1, 0)
    # glRotatef(30, 0, 0, 5)
    # glRotatef(90, 0, 0, 1)
    cube_arrangement(cubo1.status)
    pygame.display.flip()
    pygame.time.wait(10)
    

        

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) 
                print("Hey, you pressed the key, '0'!")
                
                if event.key == K_0:
                    cubo1.do_movement(0)
                    print(cubo1.status)
                    
                elif event.key == K_a:
                    glRotatef(10, 0, 5, 1)
                elif event.key == K_d:
                    glRotatef(-10, 0, 5, 1)
                
                     
                cube_arrangement(cubo1.status)
                pygame.display.flip()
                pygame.time.wait(10)
                


main()





    


