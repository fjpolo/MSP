#import numpy as np
#from numpy import cos
#from scipy import *
#from pylab import plot, show, ylim, yticks
#from matplotlib import *
#from pprint import pprint
#from numpy import linalg as LA
import numpy as NP
from matplotlib import pyplot as plt
#import math


# description of the script


## Input data
# images that are to be recognized

X = NP.matrix("1 0; 1 0; 0 1; 0 1; 1 1")

# desired reactions for the images
d = NP.matrix("1;0")

M = 5 # four variables 

T = 100 # duration of the training sequence

alpha = 0.6 # learning speed



## Neuron model
# neural functions

def f_func(arg1):
    f = 1/(1+NP.exp(-arg1));
    return f;

def f_prime_func(arg1):
    f_prime = NP.exp(arg1)/(pow((1+NP.exp(arg1)), 2));
    return f_prime;

def summ_func(arg1, arg2):
    sum = NP.dot(arg1.T, arg2);
    return sum;


## Training set

w_0 = NP.random.random((M,1)) # initial value of the weighting vector

    
#Training sequence
sequence = NP.random.random_integers(2, size=(1,T))


## Training phase

delta_history = NP.zeros(shape=(T))

# histories of weights for plotting
w_history_1 = NP.zeros(shape=(T))
w_history_2 = NP.zeros(shape=(T))
w_history_3 = NP.zeros(shape=(T))
w_history_4 = NP.zeros(shape=(T))
w_history_5 = NP.zeros(shape=(T))

output_history = NP.zeros(shape=(T))

x_current = NP.zeros(shape=(5,1))


for i in xrange(0, T):

    
    for k in xrange(0, M):
        x_current[k, 0] = X[k,sequence[0, i] -1]
       #print x_current

    
    d_desired = d[sequence[0, i] -1, 0]
   #print d_desired

    output_history[i] = f_func(summ_func(x_current, w_0))
    #print output_history

    delta = f_func(summ_func(x_current, w_0)) - d_desired
   # print delta

    for k in xrange(0, M):
        delta_history[i] =  delta**2


## the last equation
 
    for k in xrange(0, M):
       w_0[k, 0] = w_0[k, 0] - alpha*delta*f_prime_func(summ_func(x_current, w_0))*x_current[k, 0]

    w_history_1[i] = w_0[0, 0]
    w_history_2[i] = w_0[1, 0]
    w_history_3[i] = w_0[2, 0]
    w_history_4[i] = w_0[3, 0]
    w_history_5[i] = w_0[4, 0]
    

#print delta_history

epoch=[]
for i in range(T):
 epoch.append(i)


plt.subplot(3, 1, 1)
plt.plot(epoch, delta_history, 'b')
plt.title('Delta^2 (Error squared)')

plt.subplot(3, 1, 2)
plt.plot(epoch, output_history, 'b')
plt.title('Outputs')

plt.subplot(3, 1, 3)
plt.plot(epoch, w_history_1, 'r', epoch, w_history_2, 'g',epoch, w_history_3, 'b',epoch, w_history_4, 'c',epoch, w_history_5, 'm',)
plt.title('Weights')
plt.xlabel('Epochs')

plt.show()

