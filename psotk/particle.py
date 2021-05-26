# -*- coding: utf-8 -*-
"""
Created on Wed May 26 09:14:11 2021

@author: efrigier
"""


import random
import math

class Particle:
  
  def __init__(self, dimension, init_pos, bounds):

    self.__dim = dimension                                        #particle dimension
    self.__bounds = bounds                                        #particle initial position
    self.__pos = init_pos                                         #particle initial position
    self.__pos_best = init_pos                                    #particle best position
    self.__vel = [random.uniform(-1,1) for _ in range(dimension)] #particle velocity
    self.__err_best = -1                                          #particle best error
    self.__err = -1                                               #particle current error

  def update_position(self):
    """ 
    Update current position 
    """
    for idx in range(0, self.__dim):
      
      self.__pos[idx] = self.__pos[idx] + self.__vel[idx]
      
      # adjust position if biggger then max bound
      if(self.__pos[idx] > self.__bounds[idx][1]):
        self.__pos[idx] = self.__bounds[idx][1]
      # adjust position if smaller then min bound
      if(self.__pos[idx] < self.__bounds[idx][0]):
        self.__pos[idx] = self.__bounds[idx][0]          
  
    return self.__pos

  def get_position(self):
    """ 
    Returns current position 
    """
    return self.__pos

  def evaluate(self,costFunc):
    """ 
    Evaluate current fitness 
    """
    self.__err = costFunc(self.__pos)

    # check to see if the current position is the individual best
    if self.__err < self.__err_best or self.__err_best==-1:
        self.__pos_best = self.__pos
        self.__err_best = self.__err
    
    return self.__err

  def update_velocity(self, inertia_w, c1, c2, pos_best_g):
      """ 
      Update particle velocity

      inertia_w: constant inertia weight (how much to weigh the previous velocity)
      c1: cognitive constant
      c2: social constant
      """
      for idx in range(0,self.__dim):
          r1=random.random()
          r2=random.random()

          cognitive_vel=c1*r1*(self.__pos_best[idx]-self.__pos[idx])
          social_vel=c2*r2*(pos_best_g[idx]-self.__pos[idx])
          self.__vel[idx]=inertia_w*self.__vel[idx]+cognitive_vel+social_vel