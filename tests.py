# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 21:16:58 2021

@author: SOE9CT
"""

# Unit test for Cube class

# importing csv module
import csv
import numpy as np
import CUBO
  
# initializing the titles and rows list

  

def read_data(file_name):
    
    fields = []
    rows = []
    
    # reading csv file
    with open(file_name, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
          
        # extracting field names through first row
        fields = next(csvreader)
      
        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

    solution = np.zeros((5,6,3,3), dtype=int)

    i = 0
 
    for face in range(6):
        for row in range(3):
            data = rows[i][0].split("#")
            solution[0][face][row] = data[0].split(";")[:-1]
            solution[1][face][row] = data[1].split(";")[1:-1]
            solution[2][face][row] = data[2].split(";")[1:-1]
            solution[3][face][row] = data[3].split(";")[1:-1]
            solution[4][face][row] = data[4].split(";")[1:]
            i +=1
            
    return solution

def check_result(current, solution):
    result = True
    for x in range(6):
        for y in range(3):
            for z in range(3):
                if(solution[x][y][z] != current[x][y][z]):
                    print("Face -> " + str(x) + " Row: " + str(y) + " Column: " + str(z))
                    print("Right: " + str(solution[x][y][z]))
                    print("Current: " + str(current[x][y][z]))
                    result = False
                    
    return result

def check_movements(cubo1,movement):
    
    result = True

    if(not(check_result(cubo1.status, solution_vector[0]))):
        print("############# Initial state incorrect #################")  
        result = False
    else:
        print("############# Initial state correct #################")  
               
    cubo1.do_movement(movement)
    
    if(not(check_result(cubo1.status, solution_vector[1]))):
        print("############# First movement incorrect #################")  
        result = False
    else:
        print("############# First movement correct #################")  
        
    cubo1.do_movement(movement)
    
    if(not(check_result(cubo1.status, solution_vector[2]))):
        print("############# Second movement incorrect #################")  
        result = False
    else:
        print("############# Second movement correct #################")  
        
    cubo1.do_movement(movement)
        
    if(not(check_result(cubo1.status, solution_vector[3]))):
        print("############# Third movement incorrect #################") 
        result = False
    else:
        print("############# Third movement correct #################")  
        
    cubo1.do_movement(movement)
        
    if(not(check_result(cubo1.status, solution_vector[4]))):
        print("############# Fourth movement incorrect #################")  
        result = False
    else:
        print("############# Fourth movement correct #################") 
        
        return result
        
movements = []
movements.append("f")   #OK
movements.append("fr")  #OK
movements.append("b")   #OK
movements.append("br")  #OK
movements.append("r")   #OK
movements.append("rr")  #OK
movements.append("l")   #OK
movements.append("lr")  #OK
movements.append("u")   #OK
movements.append("ur")
movements.append("d")
movements.append("dr")

test_case = 11
# csv file name

cubo = CUBO.cube()
final = True

for i in range(len(movements)): 
    
    filename = 'tests/test_'
    file_type = ".csv"
    file = filename + movements[i] + file_type
    print(file)

    solution_vector = read_data(file)
    if(check_movements(cubo, i)):
        print("\n\nMovement " + movements[i] + " approved ------------------------------")
    else:
        print("Movement " + movements[i] + " reproved ------------------------------")
        final = False
    
print("\n\n--------------                        --------------------")
print("--------------                        --------------------")
print("--------------                        --------------------")

if(final):

    print("-------------- All movements approved --------------------")
else:
    print("-------------- One or more movements reproved --------------------")
    


    
           

