import numpy as np 
def set_array(L, rows, cols):
    total_elements = len(L)
    if rows * cols != total_elements:
        return ("unacceptable config of rows and cols")
    big_list = []
    iter_list = []
    print(L)
    for element in L: 
        print(element)
        iter_list.append(element)
        if len(iter_list) == cols: 
            big_list.append(iter_list)
            iter_list = []
    big_list = np.array(big_list)
    return big_list

listo = set_array(["1", "2", "3", "4","5","6"],2,3)
print(listo)
        
