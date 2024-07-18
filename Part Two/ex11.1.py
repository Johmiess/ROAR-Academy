## This is course material for Introduction to Python Scientific Programming
## Example code: extract_ETF.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import os

source_filename = 'motto.txt'

# Obtain current python file's path
path = os.path.dirname(os.path.abspath(__file__))
# Open source file and the result file
source_handle = open(path+'/'+source_filename,'w')
source_handle.write("fiat lux!")
source_handle.close()
source_handle = open(path+'/'+source_filename,'a+')
print(source_handle.readline)
source_handle.write('\n')
source_handle.write('let there be light!')
source_handle.close()
