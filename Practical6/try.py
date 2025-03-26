import numpy as np
import matplotlib.pyplot as plt

SP = 9999 #susceptible_population
IP  = 1 #infected_population
RP = 0 #recovered_population
N = 10000 #total_population
beta = 0.3 #infection_rate
gamma = 0.05 #recovery_rate
#create arrays to track the changes in the population

#make array of all susceptible population
population = np.zeros((100,100))
#randomly choose the location of the outbreak
outbreak = np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]] = 1
#create a kind of heat map

infect_x= [outbreak[0]]
infect_y= [outbreak[1]]

plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap='viridis',interpolation='nearest')

for a in range(0,11):
    plt.show()
    for i in range(0,IP):
        recover = np.random.randint(100)
        if (recover<=4):
            population[infect_x[i],infect_y[i]] = 2
            del(infect_x[i])
            del(infect_y[i])
            RP += 1
            IP -= 1
    for i in range(0,IP):
        for x in range(max(0,infect_x[i]-1),min(100,infect_x[i]+2)):
            for y in range(max(0,infect_y[i]-1),min(100,infect_y[i]+2)):
                infect = np.random.randint(100)
                if (infect<=30 and population[x,y]==0):
                    population[x,y] = 1
                    infect_x.append(x)
                    infect_y.append(y)
                    SP -= 1
                    IP += 1