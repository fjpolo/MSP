
#Example for the extraction of the Fa Matrix from the MDCT polyphase matrix
import sympy 
from numpy import *
#init_printing()

z=sympy.symbols('z')
N=4

#baseband prototype filter h(n):
#h=sympy.symbols('h:8');
h=sin(pi/(2*N)*(arange(2*N)+0.5))
print( "h=", h)

#MDCT Polyphase matrix H. Since each column contains the time-reversed impulse response, 
#we need the "N-1-n" instead of the "n":
H=sympy.Matrix(zeros((N,N)));
for n in range(0,N):
   for k in range(0,N):
      H[n,k]=h[N-1-n]*cos(pi/N*(N-1-n+N/2+0.5)*(k+0.5))+z**(-1) *h[2*N-1-n]*cos(pi/N*(2*N-1-n+N/2+0.5)*(k+0.5)) 


#Print the H matrix with 1 digit after the decimal point and replacement of very small number by 0:
print( "H=")
#sympy.pprint(H)
sympy.pprint( H.evalf(3,chop=True))


