# -*- coding: utf-8 -*-
"""
Created on Wed May 26 09:17:58 2021

@author: efrigier
"""
from psotk import PSO

# function we are attempting to optimize (minimize)
def cost_function(x):
    cost=0
    for i in range(0, len(x)):
        cost+=x[i]**2
    return cost

initial_pos=[-5,5,5]               # initial starting location [x1,x2...]
bounds = [(-10.0,10.0),(-10.0,10.0),(-10.0,10.0)]
dimension = len(initial_pos)
max_iteration = 10
num_particles = 20
inertia = 0.01
DRAW = True
SHOW_STEPS = False

if DRAW:
  import matplotlib.pyplot as plt
  from mpl_toolkits.mplot3d import Axes3D  
  import time
    
  fig = plt.figure(figsize=(8,8))
  ax = fig.add_subplot(111,projection='3d')
    
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')
  ax.set_xlim(bounds[0][0], bounds[0][1])
  ax.set_ylim(bounds[1][0], bounds[1][1])
  ax.set_zlim(bounds[2][0], bounds[2][1])
  
  plt.ion()
  fig.show()
  fig.canvas.draw()

    
pso = PSO(cost_function,dimension,bounds,num_particles, max_iteration, inertia)

iter_idx = 1;
for swarm,pos_best_g,err_best_g in pso:
  
  if SHOW_STEPS:
    print("Iteraction {}".format(iter_idx))
    print ("Candidate solution: {}" .format(pos_best_g))
    print ("Cost: {}".format(err_best_g))

  iter_idx+=1  

  if DRAW:
     
      x = []
      y = []
      z = []
      collor = []

      for particle in swarm:
        x.append(particle.get_position()[0])
        y.append(particle.get_position()[1])
        z.append(particle.get_position()[2])
        if particle.get_position() == pos_best_g:
          collor.append('r')  
        else:
          collor.append('b')          
        
      ax.clear()
      ax.scatter(x,y,z, c = collor)
      ax.set_xlim(bounds[0][0], bounds[0][1])
      ax.set_ylim(bounds[1][0], bounds[1][1])
      ax.set_zlim(bounds[2][0], bounds[2][1])
      ax.set_xlabel('X')
      ax.set_ylabel('Y')
      ax.set_zlabel('Z')
   

      fig.canvas.draw()
      time.sleep(0.5)

print(10*"-" + "FINAL SOLUTION" + 10*"-")
print ("Candidate solution: {}" .format(pos_best_g))
print ("Cost: {}".format(err_best_g))
