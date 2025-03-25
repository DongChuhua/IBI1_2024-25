#import the neccessary libraries
import numpy as np
import matplotlib.pyplot as plt

#set up the dimensions and resolution of the plot
plt.figure(figsize=(6,4),dpi=150)

#add the vaccination population
vaccination_rate = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] #vaccination rate
# loop through each diferent vaccination rate
for rate in vaccination_rate:
    SP = 9999 #susceptible_population
    IP  = 1 #infected_population
    RP = 0 #recovered_population
    S =  [SP]
    I = [IP]
    R = [RP]
    N = 10000 #total_population
    beta = 0.3 #infection_rate
    gamma = 0.05 #recovery_rate
        
        #randomly choose people in the SP without vaccination to be infected
        #randomly choose people in the IP to be recovered
        #new_SP = SP - newly_infected
        #new_IP = IP + newly_infected - newly_recovered
        #new_RP = RP + newly_recovered
        #loop in the range of 1000
    for i in range(1000):
        newly_infected = np.random.choice(range(2),int(SP*(1-rate)),p=[1-beta, beta]).sum() #1 for infected, 0 for not infected
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
    plt.plot(I, label=f"infected_population with vaccination rate {rate}")

plt.title("SIR model for 10000 people with different vaccination rate")
plt.xlabel("time")
plt.ylabel("population")
plt.legend()
plt.savefig("SIR model with vaccination.png")
plt.show()





