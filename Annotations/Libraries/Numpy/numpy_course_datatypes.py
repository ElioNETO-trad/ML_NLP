#Tutorial: https://www.youtube.com/watch?v=8Y0qQEh7dJg
import numpy as np
import matplotlib.pylab as plt
from numpy import random #to create random arrays


                                         #01 - Datatypes
#1 dimensional list
list_1 = [1, 2, 3, 4, 5] #This is a standard Python list
np_arra_1 = np.array(list_1, dtype = np.int8) #convert a standard Python list to a numpy array


print(f"This is a one-dimensional Numpy array:\n {np_arra_1}\n")

#multi-dimensional list
m_list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_m_arr_1 = np.array(m_list_1 )


print(f"This is a multi-dimensional Numpy array:\n {np_m_arr_1}\n")

#Create a list with start value, end value and the step value

np_list_start_end_step = np.arange(1, 10, 2)
print(f"This is a new Numpy array with a start value, an end value with a step value:\n {np_list_start_end_step}\n")




# Create a float list with np
np_list_float = np.linspace(0, 5, 7)

print(f"This is a float Numpy array with a start value, an end value with a step value:\n {np_list_float}\n")


# Create an array filled up with zeros or ones

np_list_zeros = np.zeros(4) #Created 4 values of zeros) = [0. 0. 0. 0.]
np_list_ones = np.ones(4)

print(f"This is a float Numpy array filled with zeros:\n {np_list_zeros}\n")
print(f"This is a float Numpy array filled with ones:\n {np_list_ones}\n")


#Create a multi-dimensional array filled up with zeros or ones
np_m_list_zeros = np.zeros((2, 3))
np_m_list_ones = np.ones((2, 3))

print(f"This is a float Numpy array filled with zeros:\n {np_m_list_zeros}\n")
print(f"This is a float Numpy array filled with ones:\n {np_m_list_ones}\n")


#See the size of the Numpy array

size_np_array = np_m_list_ones.size

print(f"This is the size of Numpy array:\n {size_np_array}\n")

#You can check the type of the array

size_np_array_type = np_m_list_ones.dtype

print(f"This is the type of this Numpy array:\n {size_np_array_type}\n")

#This is the types of Numpy arrays :
# Boolean = np.bool_
# Char = np.byte
# Short = np.short
# Integer = np.int_
# Float = np.single & np.float32
# Double = np.double & np.float64
# And more


#Generate random arrays:

np_list_random = np.random.randint(10, 50, 5) #Create a Numpy array between 10-50 with 5 values in it

print(f"This is a random array:\n {np_list_random}\n")



