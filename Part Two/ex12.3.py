import numpy as np
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

bigarray = np.array([[0,1,2,3,4,5], [10,11,12,13,14,15], [20,21,22,23,24,25], [30,31,32,33,34,35], [40,41,42,43,44,45], [50,51,52,53,54,55]])
print(bigarray[0:5, 1])
print(bigarray[1, 2:4])
print(bigarray[2:4, 4:])
print(bigarray[0:,2])