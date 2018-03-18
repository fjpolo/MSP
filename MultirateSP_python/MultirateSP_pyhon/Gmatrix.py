from sympy import *
from numpy import *

z=symbols('z')
#Coefficients
e=symbols('e:2')

#The zero-delay E matrix:
E=Matrix([[0, 0, 0, 1],[0, 0, 1, 0],[0, 1, e[0]*z**(-1), 0],[1, 0, 0,e[1]*z**(-1) ]])
print("E=");
print(E)

#...and its inverse:
Ei=E**(-1);
print("E^(-1)=")
print(Ei)
