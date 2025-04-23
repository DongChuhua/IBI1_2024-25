import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('D:\IBI\IBI1_2024-25\Practical9')
dalys_data = pd.read_csv('dalys-rate-from-all-causes.csv')
print(dalys_data.iloc[0:2,:])
print(dalys_data.head())