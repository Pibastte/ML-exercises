#Finds a decision boundary for data x using the perceptron learning algorithm
#author: Baptiste Florentin     goal: find the answer of an exercise on brilliant.org

import numpy as np

w = np.array([0,0])     # learning weights
b = 0       # bias

#data set:
x = np.array([[-1, 1], [0,-1], [10,1]])     #inputs
y = np.array([[1], [-1], [1]])      #outputs

success = 0
k = 0

def increment(k):
    if (k >= x.shape[0] - 1):
        return 0
    else:
        return k + 1

while (success < 3):
    print(k)
    print("x(" + str(x[k][0]) + "," + str(x[k][1]) + ")")
    print("w(" + str(w[0]) + "," + str(w[1]) + ")")
    print(k)

    if (y[k] * (np.dot(w,x[k]) + b) > 0):
        print("success")
        success = success + 1
        k = increment(k)
    else:
        print("fail")
        success = 0
        w = w + y[k] * x[k]
        b = b + y[k]
        k = increment(k)


print("Success ! w(" + str(w[0]) + "," + str(w[1]) + ") with bias b = " + str(b) + " is a good wheight vector")
