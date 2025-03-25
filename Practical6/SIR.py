#import the neccessary libraries
import numpy as np
import matplotlib.pyplot as plt
SP = 9999 #susceptible_population
IP  = 1 #infected_population
RP = 0 #recovered_population
N = 10000 #total_population
beta = 0.3 #infection_rate
gamma = 0.05 #recovery_rate
#create arrays to track the changes in the population
S =  [SP]
I = [IP]
R = [RP]

#the time course
#randomly choose people in the SP to be infected
#randomly choose people in the IP to be recovered
#new_SP = SP - newly_infected
#new_IP = IP + newly_infected - newly_recovered
#new_RP = RP + newly_recovered
#loop in the range of 1000
for i in range(1000):
    newly_infected = np.random.choice(range(2),SP,p=[1-beta, beta]).sum() #1 for infected, 0 for not infected
    newly_recovered = np.random.choice(range(2),IP,p=[1-gamma, gamma]).sum() #i for recovery, 0 for not recovery
    new_SP = SP - newly_infected
    new_IP = IP + newly_infected - newly_recovered
    new_RP = RP + newly_recovered
    S.append(new_SP)
    I.append(new_IP)
    R.append(new_RP)
    SP = new_SP
    IP = new_IP
    RP = new_RP

#set up the dimensions and resolution of the plot
plt.figure(figsize=(6,4),dpi=140)
# plot the results
plt.plot(S, label="susceptible_population")
plt.plot(I, label="infected_population")
plt.plot(R, label="recovered_population")
plt.title("SIR model for 10000 people")
plt.xlabel("time")
plt.ylabel("population")
plt.legend()
#save the plot
plt.savefig("SIR model.png")
plt.show()


