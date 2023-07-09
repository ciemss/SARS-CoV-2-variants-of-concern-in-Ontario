import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Load data
output = pd.read_csv('output.csv')  # Adjust this to your actual data file

# Define dates and labels
dateticks = [60, 151, 243, 334, 425, 516, 608, 699, 790]
datelabels = ['Mar', 'Jun', 'Sep', 'Dec', 'Mar', 'Jun', 'Sep', 'Dec', 'Mar', 'Jun']

# Define population fractions
Stot = output['S'] + output['SVR']
Vtot = output['V1PF'] + output['V1AZ'] + output['V2PF'] + output['V2AZ']
Itot = output['IP'] + output['IPV'] + output['IPR'] + output['IA'] + output['IAV'] + output['IAR'] + output['ID'] + output['IDV'] + output['IDR']
Atot = output['AP'] + output['APR'] + output['AA'] + output['AAR'] + output['AD'] + output['ADR']
Rtot = output['RP'] + output['RA'] + output['RD'] + output['R2']

# Plotting
fig, axs = plt.subplots(3, 3)

# Subplot 1
axs[0, 0].plot(output['t'], np.ones(len(output['t'])), '-r', linewidth=2)
axs[0, 0].plot(output['t'], Vtot + Itot + Atot + Rtot, '-b', linewidth=2)
axs[0, 0].plot(output['t'], Itot + Atot + Rtot, '-g', linewidth=2)
axs[0, 0].plot(output['t'], Itot + Atot, '-k', linewidth=2)
axs[0, 0].fill_between(output['t'], np.ones(len(output['t'])), Vtot + Itot + Atot + Rtot, color='red', alpha=0.5)
axs[0, 0].fill_between(output['t'], Vtot + Itot + Atot + Rtot, Itot + Atot + Rtot, color='green', alpha=0.5)
axs[0, 0].fill_between(output['t'], Itot + Atot + Rtot, Itot + Atot, color='blue', alpha=0.5)
axs[0, 0].fill_between(output['t'], Itot + Atot, 0 * Rtot, color='green', alpha=0.5)
axs[0, 0].legend(['S', 'V', 'R', 'I+A'])
axs[0, 0].set_xticks(dateticks)
axs[0, 0].set_xticklabels(datelabels)
axs[0, 0].set_ylabel('Population fraction')
axs[0, 0].set_title('(i)')

# ... Continue with other subplots

plt.show()
