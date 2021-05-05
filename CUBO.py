# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 21:08:22 2021

@author: sedos
"""
import numpy as np
import random

movements = []
movements.append("f")
movements.append("fr")
movements.append("b")
movements.append("br")
movements.append("r")
movements.append("rr")
movements.append("l")
movements.append("lr")
movements.append("u")
movements.append("ur")
movements.append("d")
movements.append("dr")


# face 0 = front
# face 1 = back
# face 2 = right
# face 3 = left
# face 4 = top
# face 5 = bottom
 
class cube:
    
    faces = 6
    rows = 3
    columns = 3
    
    def __init__(self):
        # self.status = np.zeros(shape=(6,3,3))
        self.status = np.zeros((self.faces,self.rows,self.columns), int)
        self.organize_faces()

                    
    def organize_faces(self):
        for x in range (self.faces):
            value = 0;
            for y in range (self.rows):
                for z in range (self.columns):
                    # self.status[x][y][z] = 100*x + 10*y + z
                    self.status[x][y][z] = x
                    value += 1
                    
    def sort_faces(self):
        self.organize_faces()
        for i in range(100):
            sort = random.randint(0, 11)
            self.do_movement(sort)
            
    def get_score(self):
        score = 0
        for x in range (self.faces):
            for y in range (self.rows):
                for z in range (self.columns):
                    if(self.status[x][y][z] == x):
                        score += 1
        return score
                        
    def do_movement(self, movement):
        face = int((movement)/2)
        
        clockwise = False
        
        if(movement%2 == 0):
            clockwise = True 

        # print("\nExecuting movement: " + str(movements[movement]) + " face -> " + str(face) + " cw -> " + str(clockwise) + " ..\n")
        self.face_flip(face, clockwise)
        
        right_edge = np.zeros((1,3), int)
        left_edge = np.zeros((1,3), int)
        top_edge = np.zeros((1,3), int) 
        bottom_edge = np.zeros((1,3), int)
        
        right_face = 0
        left_face = 0
        top_face = 0 
        bottom_face = 0
            
        ############### Front face ############### 
        if(face == 0):
            
            right_face = 2
            left_face = 3
            top_face = 4
            bottom_face = 5
        
            right_edge = self.status[2][:,0].copy()
            left_edge = self.status[3][:,2].copy()
            top_edge = self.status[4][2].copy()
            bottom_edge = self.status[5][0].copy()
            
            if(clockwise):
                self.status[right_face][:,0] = top_edge
                self.status[left_face][:,2] = bottom_edge
                self.status[top_face][2] = np.flip(left_edge)
                self.status[bottom_face][0] = np.flip(right_edge)
                
            else:           
                self.status[right_face][:,0] = np.flip(bottom_edge)
                self.status[left_face][:,2] = np.flip(top_edge)
                self.status[top_face][2] = right_edge
                self.status[bottom_face][0] = left_edge
             
        ############### Back face ###############
        if(face == 1):
            
            right_face = 3
            left_face = 2
            top_face = 4
            bottom_face = 5
            
            right_edge = self.status[3][:,0].copy()
            left_edge = self.status[2][:,2].copy()
            top_edge = self.status[4][0].copy()
            bottom_edge = self.status[5][2].copy()
            
            if(clockwise):
                self.status[right_face][:,0] = np.flip(top_edge)
                self.status[left_face][:,2] = np.flip(bottom_edge)
                self.status[top_face][0] = left_edge
                self.status[bottom_face][2] = right_edge
                
            else:           
                self.status[right_face][:,0] = bottom_edge
                self.status[left_face][:,2] = top_edge
                self.status[top_face][0] = np.flip(right_edge)
                self.status[bottom_face][2] = np.flip(left_edge)
                
        ############### Right face ###############        
        if(face == 2):
            
            right_face = 1
            left_face = 0
            top_face = 4
            bottom_face = 5
            
            right_edge = self.status[1][:,0].copy()
            left_edge = self.status[0][:,2].copy()
            top_edge = self.status[4][:,2].copy()
            bottom_edge = self.status[5][:,2].copy() 
            
            if(clockwise):
                self.status[right_face][:,0] = np.flip(top_edge)
                self.status[left_face][:,2] = bottom_edge
                self.status[top_face][:,2] = left_edge
                self.status[bottom_face][:,2] = np.flip(right_edge)
                
            else:           
                self.status[right_face][:,0] = np.flip(bottom_edge)
                self.status[left_face][:,2] = top_edge
                self.status[top_face][:,2] = np.flip(right_edge)
                self.status[bottom_face][:,2] = left_edge
                
        ############### Left face ###############        
        if(face == 3):
            
            right_face = 0
            left_face = 1
            top_face = 4
            bottom_face = 5
            
            right_edge = self.status[0][:,0].copy()
            left_edge = self.status[1][:,2].copy()
            top_edge = self.status[4][:,0].copy()
            bottom_edge = self.status[5][:,0].copy() 
            
            if(clockwise):
                self.status[right_face][:,0] = top_edge
                self.status[left_face][:,2] = np.flip(bottom_edge)
                self.status[top_face][:,0] = np.flip(left_edge)
                self.status[bottom_face][:,0] = right_edge
                
            else:           
                self.status[right_face][:,0] = bottom_edge
                self.status[left_face][:,2] = np.flip(top_edge)
                self.status[top_face][:,0] = right_edge
                self.status[bottom_face][:,0] = np.flip(left_edge)
                
        ############### Up face ###############        
        if(face == 4):
            
            right_face = 2
            left_face = 3
            top_face = 1
            bottom_face = 0
            
            right_edge = self.status[2][0].copy()
            left_edge = self.status[3][0].copy()
            top_edge = self.status[1][0].copy()
            bottom_edge = self.status[0][0].copy() 
            
            if(clockwise):
                self.status[right_face][0] = top_edge
                self.status[left_face][0] = bottom_edge
                self.status[top_face][0] = left_edge
                self.status[bottom_face][0] = right_edge
                
            else:           
                self.status[right_face][0] = bottom_edge
                self.status[left_face][0] = top_edge
                self.status[top_face][0] = right_edge
                self.status[bottom_face][0] = left_edge
                
        ############### Down face ###############        
        if(face == 5):
            
            right_face = 2
            left_face = 3
            top_face = 0
            bottom_face = 1
            
            right_edge = self.status[2][2].copy()
            left_edge = self.status[3][2].copy()
            top_edge = self.status[0][2].copy()
            bottom_edge = self.status[1][2].copy() 
            
            if(clockwise):
                self.status[right_face][2] = top_edge
                self.status[left_face][2] = bottom_edge
                self.status[top_face][2] = left_edge
                self.status[bottom_face][2] = right_edge
                
            else:           
                self.status[right_face][2] = bottom_edge
                self.status[left_face][2] = top_edge
                self.status[top_face][2] = right_edge
                self.status[bottom_face][2] = left_edge  
                
    def face_flip(self, face, clockwise):
        temporary_copy = np.zeros((self.rows,self.columns), int)
        
        for x in range (self.rows):
            for y in range (self.columns):
                
                new_x = 2-y
                new_y = x
                
                if(not(clockwise)):
                    new_x = y
                    new_y = 2-x
                
                temporary_copy[x][y] = self.status[face][new_x][new_y].copy()
                
        self.status[face] = temporary_copy
                