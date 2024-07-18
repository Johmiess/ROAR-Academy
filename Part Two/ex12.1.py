import numpy as np
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection="3d")

v = np.array([2., 2., 4.]) 

ax.scatter3D(v[0], v[1], v[2], c=v[2], cmap='hsv')
plt.show()
