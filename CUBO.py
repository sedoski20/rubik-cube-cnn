# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 21:08:22 2021

@author: sedos
"""
import numpy as np

# "f" = 0
# "fr" = 1

# "r" = 2
# "rr" = 3

# "l" = 4
# "lr" = 5 

# "u" = 6
# "ur" = 7

# "d" = 8
# "dr" = 9

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
        for x in range (self.faces):
            value = 0;
            for y in range (self.rows):
                for z in range (self.columns):
                    self.status[x][y][z] = x
                    value += 1
                    
    def do_movement(self, movement):
        face = int((movement)/2)
        
        clockwise = False
        
        if(movement%2 == 0):
            clockwise = True 

        print("\nExecuting movement: " + str(movements[movement]) + " face -> " + str(face) + " cw -> " + str(clockwise) + " ..\n")
        # self.face_flip(face, clockwise)
        
        temporary_copy = np.zeros((4,3), int)
        
        right_edge = np.zeros((1,3), int)
        left_edge = np.zeros((1,3), int)
        top_edge = np.zeros((1,3), int) 
        bottom_edge = np.zeros((1,3), int)
        
        right_face = 0
        left_face = 0
        top_face = 0 
        bottom_face = 0
        
        #Set the faces around the face that will be flipped by the selected movement
        #Save the edges around the this face
        
        if(face == 0):
            #front
            right_face = 2
            left_face = 3
            top_face = 4
            bottom_face = 5
        
            right_edge = self.status[2][:,0].copy()
            left_edge = self.status[3][:,2].copy()
            top_edge = self.status[4][2].copy()
            bottom_edge = self.status[5][0].copy()
        
        elif(face == 1):
            #back    
            right_face = 3
            left_face = 2
            top_face = 5
            bottom_face = 4
            
            right_edge = self.status[3][:,0].copy()
            left_edge = self.status[2][:,2].copy()
            top_edge = self.status[5][2].copy()
            bottom_edge = self.status[4][0].copy()
            
        elif(face == 2):
            #right      
            right_face = 1
            left_face = 0
            top_face = 4
            bottom_face = 5
            
            right_edge = self.status[1][:,0].copy()
            left_edge = self.status[0][:,2].copy()
            top_edge = self.status[4][:,2].copy()
            bottom_edge = self.status[5][:,2].copy() 
            
            
        #Re-organize the faces after the movement
        if(face == 0 or face ==1):
            if(clockwise):
                self.status[right_face][:,0] = top_edge
                self.status[left_face][:,2] = bottom_edge
                self.status[top_face][2] = left_edge
                self.status[bottom_face][0] = right_edge
                
            else:           
                self.status[right_face][:,0] = bottom_edge
                self.status[left_face][:,2] = top_edge
                self.status[top_face][2] = right_edge
                self.status[bottom_face][0] = left_edge
                
        if(face == 2):
            if(clockwise):
                self.status[right_face][:,0] = top_edge
                self.status[left_face][:,2] = bottom_edge
                self.status[top_face][:,2] = left_edge
                self.status[bottom_face][:,2] = right_edge
                
            else:           
                self.status[right_face][:,0] = bottom_edge
                self.status[left_face][:,2] = top_edge
                self.status[top_face][2] = right_edge
                self.status[bottom_face][0] = left_edge
                
    def face_flip(self, face, clockwise):
        temporary_copy = np.zeros((self.faces,self.rows,self.columns), int)
        
        for x in range (self.rows):
            for y in range (self.columns):
                
                new_x = 2-y
                new_y = x
                
                if(not(clockwise)):
                    new_x = y
                    new_y = 2-x
                
                temporary_copy[face][x][y] = self.status[face][new_x][new_y]
                
        self.status = temporary_copy
                
                    
cubo1 = cube()
print("\n\nInicio: ----------------------\n\n")
print(cubo1.status)
print("\n\nMov 1: ----------------------\n\n")
cubo1.do_movement(4)
print(cubo1.status)
print("\n\nMov 2: ----------------------\n\n")
cubo1.do_movement(4)
print(cubo1.status)
print("\n\nMov 3: ----------------------\n\n")
cubo1.do_movement(4)
print(cubo1.status)
print("\n\nMov 4: ----------------------\n\n")
cubo1.do_movement(4)
print(cubo1.status)





