import numpy as np
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
bigarray = np.array([[0,1,2,3,4,5], [10,11,12,13,14,15]])


def swap_rows(matrix : np.array,a : int, b:int):
    try:
        new_matrix = np.copy(matrix)
        a_row = new_matrix[a]
        b_row = new_matrix[b]
        # avoid how memory pointer causes duped arrays by making copy
        matrix[b] = a_row
        matrix[a] = b_row
    except ValueError:
        print("value error, please provide the correct arugments")
    except:
        print("Unkown error, please try again with indicated arugments")

def swap_col(matrix : np.array,a : int, b:int):
    try:
        new_matrix = np.copy(matrix)
        # avoid how memory pointer causes duped arrays by making copy
        for row in range(0,len(matrix)):
            matrix[row,a] = matrix[row,b]
            matrix[row,b] = new_matrix[row,a]

    except ValueError:
        print("value error, please provide the correct arugments")
    except:
        print("Unkown error, please try again with indicated arugments")


swap_col(bigarray,0,1)        
print(bigarray)