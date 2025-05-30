#make array of all susceptible population
#randomly choose the location of the outbreak
#show the initial state of the population
#loop every point
#located the infected person
#try to infect the neighbor of the infected person
#try to recover the infected person
#plot the heat map

import numpy as np
import matplotlib.pyplot as plt

#make array of all susceptible population
population = np.zeros((100,100))
#randomly choose the location of the outbreak
outbreak = np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]] = 1

#show the initial state of the population
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap='viridis',vmin=0, vmax=2, interpolation='nearest')
plt.title('Initial State')
plt.show()

SP = 9999 #susceptible_population
IP  = 1 #infected_population
RP = 0 #recovered_population
N = 10000 #total_population
beta = 0.3 #infection_rate
gamma = 0.05 #recovery_rate

#loop every point
new_population=population.copy()
for a in range(100):  #loop 100 times
    #loop every point
    for x in range(100):
        for y in range(100):
            if population[x,y] == 1: #located the infected person
                #try to infect the neighbor of the infected person
                #locate its neighbor (ensure is within the size)
                for i in range(max(0,x-1),min(100,x+2)):
                    for j in range(max(0,y-1),min(100,y+2)):
                        if population[i,j] == 0: #if the neighbor is susceptible
                            #randomly choose some of them to be infected (beta infetion rate)
                            if np.random.choice(range(2),1,p=[1-beta,beta]).sum() == 1:
                                new_population[i,j] = 1
                #try to recover the infected person (gamma recovery rate)
                if np.random.choice(range(2),1,p=[1-gamma,gamma]).sum() == 1:
                    new_population[x,y] = 2
    population = new_population
   #plot the heat map
    if a%10 == 0:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap='viridis',vmin=0, vmax=2, interpolation='nearest')
        plt.show()
        
  
        
            
   
            
            
            
 

    
   
