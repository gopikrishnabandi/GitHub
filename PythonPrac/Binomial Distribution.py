#Prbability Mass Function

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom

no_of_exp=10
prob_success=0.5
prob_out_range=range(0,11) #probable_outcomes_for_5_heads,in 10 experiments anywhere from 0 to 10 times


#Probabilities
prob=binom.pmf(prob_out_range,no_of_exp,prob_success)
fig,binom_plot=plt.subplots(figsize=(10,8))
binom_plot.set_xlabel("Number of Heads",fontsize=16)
binom_plot.set_ylabel("Probability",fontsize=16)
binom_plot.vlines(prob_out_range, 0, prob, colors='r', lw=5, alpha=0.5)
binom_plot.plot(prob_out_range,prob)
plt.show()

# no_exp=10
# prob_event=0.5
# no_of_heads=range(0,11)
#
# prob=binom.pmf(no_of_heads,no_exp,prob_event)
# plt.plot(no_of_heads,prob)
# plt.show()










