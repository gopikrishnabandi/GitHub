#probability density function

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
import scipy.stats

random_value_uniform=np.linspace(0.0,20.0,100)
normal_dist=scipy.stats.norm.pdf(random_value_uniform,random_value_uniform.mean())
fig,normal_plot=plt.subplots(figsize=(10,8))
normal_plot.set_xlabel("Random variable Values",fontname="Arial",fontsize=12)
normal_plot.set_ylabel("Normal distribution values",fontname="Arial",fontsize=12)
normal_plot.plot(random_value_uniform,normal_dist)
plt.show()