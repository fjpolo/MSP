#Example for the extraction of the Fa Matrix from the MDCT polyphase matrix
import sympy 
from numpy import *

z=sympy.symbols('z')
N=4

#baseband prototype filter h(n):
h=sympy.symbols('h:8');
print( "h=")
print(h)

#MDCT Polyphase matrix H. Since each column contains the time-reversed impulse response, 
#we need the "N-1-n" instead of the "n":
H=sympy.Matrix(zeros((N,N)));
for n in range(0,N):
   for k in range(0,N):
      H[n,k]=h[N-1-n]*cos(pi/N*(N-1-n+N/2+0.5)*(k+0.5))+z**(-1) *h[2*N-1-n]*cos(pi/N*(2*N-1-n+N/2+0.5)*(k+0.5)) 

#Transform matrix T:
T=sympy.Matrix(zeros((N,N)));
for n in range(0,N):
   for k in range(0,N):
      T[n,k]=cos(pi/N*(n+0.5)*(k+0.5));

#Compute the sparse Fa matrix:
Fa= H*(T**(-1))

#Print the H matrix with 1 digit after the decimal point and replacement of very small number by 0:
print( "H=")
print( H.evalf(1,chop=True))

#Print the Fa matrix with 1 digit after the decimal point and replacement of very small number by 0:
print( "Fa=")
print( Fa.evalf(1,chop=True))
#print(sympy.N(Fa,2))
print(sympy.Float(Fa,2))
