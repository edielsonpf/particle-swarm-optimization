# -*- coding: utf-8 -*-
"""
Created on Wed May 26 09:16:13 2021

@author: efrigier
"""
import random
from psotk.particle import Particle

class PSO():
  def __init__(self, costFunc, dimension, bounds, num_particles, max_iter, inertia_w):
        
        self.__dimension = dimension
        self.__err_best_g=-1                   # best error for group
        self.__pos_best_g=[]                   # best position for group
        self.__max_iter = max_iter
        self.__costFunc = costFunc
        self.__inertia_w = inertia_w
        self.__c1 = 1
        self.__c2 = 2

        # create the swarm
        self.__swarm=[]
        for _ in range(0,num_particles):
            init_pos = [random.uniform(bounds[idx][0],bounds[idx][1]) for idx in range(0, dimension)]
            self.__swarm.append(Particle(dimension, init_pos, bounds))
            
  def __iter__(self):
    """
    Generator which returns the current swarm status.
    """

    iter_idx = 0
    while iter_idx < self.__max_iter:

      #print("iter {}".format(iter_idx))
      for particle in self.__swarm:
        err_particle = particle.evaluate(self.__costFunc)
        # determine if current particle is the best (globally)
        if err_particle < self.__err_best_g or self.__err_best_g == -1:
            self.__pos_best_g = particle.get_position()
            self.__err_best_g = err_particle

      # run over the swarm and update velocity and position
      for particle in self.__swarm:
        particle.update_velocity(self.__inertia_w, self.__c1, self.__c2, self.__pos_best_g)
        particle.update_position()

      iter_idx+=1
            
      yield self.__swarm, self.__pos_best_g, self.__err_best_g 