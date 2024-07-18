## This is course material for Introduction to Python Scientific Programming
## Example code: matplotlib_basic_plot.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import matplotlib.pyplot as plt
import numpy as np

# generate a basic sample point array on x-axis
x = [1,2,3.0]
# Create a sin function sample
y0 = [2,4,0.0]
plt.plot(x, y0)
plt.title("Sample graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()