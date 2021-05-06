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
colors.append((255,0,0))        #red
colors.append((255,128,0))      #orange
colors.append((0,150,0))        #green
colors.append((0,0,150))        #blue
colors.append((230,230,0))      #yellow
colors.append((255,255,255))    #white
colors.append((255,55,155))     #pink
    

def face(color, axis):

    list = glGenLists(1)
    glNewList(list, GL_COMPILE)
    glNormal3d(0.0, 0.0, 0.0)
    
    glBegin(GL_QUADS) 
    glColor3ubv(color)
    for vertex in surfaces[axis]:
        glVertex3fv(verticies[vertex])
    glEnd()
    
    index = 0
    for vertex in surfaces[axis]:
        
        if((vertex + 1) < len(verticies[vertex])):
            index = vertex +1
        else:
            index = 0
            
        
    
    glEndList()
    return list

def draw_lines():
    draw_line((2,2,-4),(2,2,2))
    draw_line((0,2,-4),(0,2,2))
    draw_line((-2,2,-4),(-2,2,2))
    draw_line((-4,2,-4),(-4,2,2))
    draw_line((-4,2,0),(2,2,0))
    draw_line((-4,2,-2),(2,2,-2))
    
    draw_line((2,-4,-4),(2,-4,2))
    draw_line((0,-4,-4),(0,-4,2))
    draw_line((-2,-4,-4),(-2,-4,2))
    draw_line((-4,-4,-4),(-4,-4,2))
    draw_line((-4,-4,0),(2,-4,0))
    draw_line((-4,-4,-2),(2,-4,-2))
    
    draw_line((-4,-4,2),(-4,2,2))
    draw_line((-4,-4,0),(-4,2,0))
    draw_line((-4,-4,-2),(-4,2,-2))
    draw_line((-4,-4,-4),(-4,2,-4))
    draw_line((-4,0,-4),(-4,0,2))
    draw_line((-4,-2,-4),(-4,-2,2))
    
    draw_line((2,-4,2),(2,2,2))
    draw_line((2,-4,0),(2,2,0))
    draw_line((2,-4,-2),(2,2,-2))
    draw_line((2,-4,-4),(2,2,-4))
    draw_line((2,0,-4),(2,0,2))
    draw_line((2,-2,-4),(2,-2,2))
    
    draw_line((-4,-4,2),(2,-4,2))
    draw_line((-4,-2,2),(2,-2,2))
    draw_line((-4,0,2),(2,0,2))
    draw_line((-4,2,2),(2,2,2))
    draw_line((0,-4,2),(0,2,2))
    draw_line((-2,-4,2),(-2,2,2))
    
    draw_line((-4,-4,-4),(2,-4,-4))
    draw_line((-4,-2,-4),(2,-2,-4))
    draw_line((-4,0,-4),(2,0,-4))
    draw_line((-4,2,-4),(2,2,-4))
    draw_line((0,-4,-4),(0,2,-4))
    draw_line((-2,-4,-4),(-2,2,-4))

    

def draw_line(p1, p2):
    glColor3ub(151,151,152)
    glLineWidth(5)
    glBegin(GL_LINES)       
    glVertex3f(p1[0], p1[1], p1[2])
    glVertex3f(p2[0], p2[1], p2[2]) 
    glEnd()
    
def draw_shape(shape, dx, dy, dz):
    """Helper to translate, rotate and draw the shape."""
    glPushMatrix()
    glTranslated(dx, dy, dz)
    glCallList(shape)
    glPopMatrix()
    
def cube_arrangement(current):
    draw_lines() 
    # Face 0
    for x in range(3):
        for y in range(3):
            x1 = -3 + (2*x)
            y1 = -3 + (2*y)
            draw_shape(face(colors[current[0][y][x]], 0), x1, y1, -3.0)
            
    # Face 1
    for x in range(3):      
        for y in range(3):
            x1 = -3 + (2*x)
            y1 = -3 + (2*y) 
            draw_shape(face(colors[current[1][y][2-x]], 0), x1, y1, 3.0)
            
    # Face 2 
    for y in range(3):
        for z in range(3):
            y1 = -3 + (2*y)
            z1 = -3 + (2*z)
            draw_shape(face(colors[current[2][y][z]], 1), 3.0, y1, z1)
            
    # Face 3
    for y in range(3):
        for z in range(3):
            y1 = -3 + (2*y)
            z1 = -3 + (2*z)
            draw_shape(face(colors[current[3][y][2-z]], 1), -3.0, y1, z1)
            
    # Face 4 
    for x in range(3):
        for z in range(3):
            x1 = -3 + (2*x)
            z1 = -3 + (2*z)
            draw_shape(face(colors[current[4][2-z][x]], 2), x1, -5.0, z1)
            
    # Face 5 
    for x in range(3):
        for z in range(3):
            x1 = -3 + (2*x)
            z1 = -3 + (2*z)
            draw_shape(face(colors[current[5][z][x]], 2), x1, 1.0, z1)  

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(1.0,0.0, -20)
    glRotatef(180, 1, 0, 0)
    glEnable(GL_DEPTH_TEST);
    cubo1 = CUBO.cube()
  
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)      
    cube_arrangement(cubo1.status)
    pygame.display.flip()
    pygame.time.wait(10)
    
    auto_mode = False    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                 
                
                if event.key == K_n:
                    auto_mode = True
                if event.key == K_m:
                    auto_mode = False
                if event.key == K_0:
                    cubo1.do_movement(0)
                if event.key == K_1:
                    cubo1.do_movement(1)
                if event.key == K_2:
                    cubo1.do_movement(2)
                if event.key == K_3:
                    cubo1.do_movement(3)
                if event.key == K_4:
                    cubo1.do_movement(4)
                if event.key == K_5:
                    cubo1.do_movement(5)
                if event.key == K_6:
                    cubo1.do_movement(6)
                if event.key == K_7:
                    cubo1.do_movement(7)
                if event.key == K_8:
                    cubo1.do_movement(8)
                if event.key == K_9:
                    cubo1.do_movement(9)
                if event.key == K_o:
                    cubo1.do_movement(10)
                if event.key == K_p:
                    cubo1.do_movement(11)
                if event.key == K_r:
                    cubo1.organize_faces()

                if(not(auto_mode)):
                    if event.key == K_a:
                        glRotatef(10, 5, 5, 1)
                    if event.key == K_d:
                        glRotatef(-10, 5, 5, 1)
                        
                    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                    cube_arrangement(cubo1.status)
                    pygame.display.flip()
        
        if(auto_mode):
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)            
            cube_arrangement(cubo1.status)     
            glRotatef(2, 5, 5, 1)
            pygame.display.flip()
            pygame.time.wait(50)
                
main()





    


