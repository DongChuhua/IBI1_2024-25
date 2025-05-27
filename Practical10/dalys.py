import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('D:\IBI\IBI1_2024-25\Practical9')
#import the data
dalys_data = pd.read_csv('dalys-rate-from-all-causes.csv')


#show the third column(the year) for the first 10 rows
print(dalys_data.iloc[0:10,2])
# the 10th year with DALYs data recorded in Afghanistan: 1999


#show DALYs for all countries in 1990
print(dalys_data.loc[dalys_data['Year'] == 1990, 'DALYs'])


#Examining the situation across countries
#computed the mean DALYs in the UK and France
uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", "DALYs"]
mean_DALYs_uk = uk.describe().loc['mean']
france = dalys_data.loc[dalys_data.Entity=="France", "DALYs"]
mean_DALYs_france = france.describe().loc['mean']
print(f"Mean DALYs in the UK: {mean_DALYs_uk}") 
print(f"Mean DALYs in France: {mean_DALYs_france}")
#the mean DALYs in the UK was greater than France

#plot the data for the UK over time
uk_copy = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["Year", "DALYs"]]
plt.plot(uk_copy.Year, uk_copy.DALYs, 'ro')
plt.title("DALYs in the UK over time")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(uk_copy.Year,rotation=-90)
plt.show()

#solution to my question
china = dalys_data.loc[dalys_data.Entity=="China", ["Year" , "DALYs"]]
plt.plot(china.Year, china.DALYs, 'bo', label="China")
plt.plot(uk_copy.Year, uk_copy.DALYs, 'ro', label="UK")
plt.title("DALYs in the UK and China over time")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(uk_copy.Year,rotation=-90)
plt.legend()
plt.show()



                       

