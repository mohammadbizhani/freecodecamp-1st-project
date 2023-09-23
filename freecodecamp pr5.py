# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 18:34:03 2023

@author: Mohamad
"""

import random
import copy

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, number):
    if number > len(self.contents):
      return self.contents
  
    balls = []
    for i in range(number):
      rb = random.randrange(len(self.contents))
      balls.append(self.contents.pop(rb))
    return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  expected_no_of_balls = []
  for key in expected_balls:
      expected_no_of_balls.append(expected_balls[key])
  succes = 0

  for i in range(num_experiments):
    new_hat = copy.deepcopy(hat)
    balls = new_hat.draw(num_balls_drawn)

    no_of_balls = []
    for key in expected_balls:
      no_of_balls.append(balls.count(key))
    if no_of_balls >= expected_no_of_balls:
      succes += 1

  return succes/num_experiments