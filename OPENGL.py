# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 16:47:03 2021

@author: sedos
"""
import sys
from PySide2 import QtCore, QtOpenGL
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QLabel


class GLDemo(QtOpenGL.QGLWidget):
    def __init__(self,parent=None):
        QtOpenGL.QGLWidget().__init__(self,parent)
        self.xsize = 512
        self.ysize = 512
        
    def initializeGL():
        print("initialized")
        # glClearColor()
        
    def paintGL():
        print("resized")
        # glClearColor() 
 
if not QApplication.instance():
    app = QApplication(sys.argv)
else:
    app = QApplication.instance()
    
window = QWidget() # Create a window.



app.exec_() # Execute the App

