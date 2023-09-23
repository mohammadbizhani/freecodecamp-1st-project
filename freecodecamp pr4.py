# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 19:22:47 2023

@author: Mohamad
"""

class Rectangle :
  def __init__(self , width , height):
    self.width = width
    self.height = height
    
  def set_width(self , width) :
    self.width = width
    
  def set_height(self , height) :
    self.height = height
    
  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2*(self.width + self.height)

  def get_diagonal(self):
    return (self.width**2 + self.height**2) ** 0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
     return "Too big for picture."
    else:
     
     shape_list = []
     for i in range(self.height):
       star_line = ''
       for j in range(self.width):
         star_line += '*'
      
       shape_list.append(star_line)
    
     shap='\n'.join(shape_list)
     import os
     final_shap = shap + os.linesep
     return final_shap
 
  def get_amount_inside(self , self_2):
      return(self.width//self_2.width)*(self.height//self_2.height)
      
  def __str__(self):
    return 'Rectangle(width={}, height={})'.format(self.width , self.height)

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
    
  def set_side(self ,side):
    Rectangle.set_width(self,side)
    Rectangle.set_height(self,side)
    
  def __str__(self):
    return "Square(side={})".format(self.width)