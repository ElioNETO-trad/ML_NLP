import numpy as np
import matplotlib.pyplot as plt

#Problem: Model which can predict housing prices given the since of the house.
# 2 data points (size (.100m2), price(.1000€))) = house_1 = (1, 300), house 2 = (2, 500)

x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])


#Let's use the cost function = J(w,b) = 1/2m E v2m ^m-1(fw,b(x(i) - y(i)))2

#Where = J(w,b) = cost function
# 1/2m = 1 divided by 2 times the number of training examples
# E v2m ^ m-1 = The sum of all functions of the training examples - 1 (Python starts from 0)
# fwb(x(i)) = Function f = wx + b
# i = current iteration
# y = label


def compute_cost (x, y, w, b):
    """
    Algorithm to compute the cost function (linear regression)

    Args:
    x (ndarray (m, )) = Data, m examples
    y (ndarray (m,)) = target values (label)
    w,b (scalar) = parameters of the model (weight and bias)

    It's going to return:
    total_cost(in float) = the cost of using w,b as the parameters for linear regression in order to fit the data points in x and y
    """

    #number of training examples
    m = x.shape[0] #our x features will be here to sum all the features

    cost_sum = 0 #initial value that will be updated

    for i in range(m): #loop in the total number of features
        f_wb = w * x[i] + b #f_wb function [i] = number of iteration loop
        cost = (f_wb - y[i]) ** 2 # the rest of the cost function
        cost_sum = cost_sum + cost # the sum of the current cost function + the initial cost function
        total_cost = (1 / (2 * m)) * cost_sum #the remaining cost function after sum has been calculated
        
        return total_cost
    

# let's try compute cost:


test_1 = compute_cost(x_train, y_train, 0.8, 2)


print(test_1)