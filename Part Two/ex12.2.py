import numpy as np
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# question 1
dos = 2
matrix1 = np.array([[6,-9, 1], [4,24,8]]) 
print(matrix1 * 2)

# q 2
matrix2 = np.array([[1,0], [0,1]]) 
matrix3 = np.array([[6,-9, 1], [4,24,8]]) 
print(np.matmul(matrix2, matrix3))

# q 3
matrix2 = np.array([[4,3], [3,2]]) 
matrix3 = np.array([[-2, 3], [3,-4]]) 
print(np.matmul(matrix2, matrix3))