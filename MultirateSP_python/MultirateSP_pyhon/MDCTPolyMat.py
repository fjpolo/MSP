
#MDCT Polyphase matrices with symbolic z's
import sympy 
from numpy import *
#init_printing()

z=sympy.symbols('z')
N=4



def Pa(h):
	#MDCT Polyphase matrix H. Since each column contains the time-reversed impulse response, 
	#we need the "N-1-n" instead of the "n":
	H=sympy.Matrix(zeros((N,N)));
	for n in range(0,N):
	   for k in range(0,N):
	      H[n,k]=h[N-1-n]*cos(pi/N*(N-1-n+N/2+0.5)*(k+0.5))+z**(-1) *h[2*N-1-n]*cos(pi/N*(2*N-1-n+N/2+0.5)*(k+0.5)) 
	return H

def Ps(g):
	G=sympy.Matrix(zeros((N,N)));
	for n in range(0,N):
	   for k in range(0,N):
	      G[k,n]=g[n]*cos(pi/N*(n-N/2+0.5)*(k+0.5))+z**(-1) *g[N+n]*cos(pi/N*(N+n-N/2+0.5)*(k+0.5)) 
	return G


if __name__ == '__main__':

	#baseband prototype filter h(n):
	#h=sympy.symbols('h:8');
	h=sin(pi/(2*N)*(arange(2*N)+0.5))
	print( "h=", h)
	H=Pa(h)
        print("H=")
	sympy.pprint( H.evalf(3,chop=True))
	g=h/(N/2.0)
	G=Ps(g)
	#Print the H matrix with 1 digit after the decimal point and replacement of very small number by 0:
	print( "G=")
	#sympy.pprint(H)
	sympy.pprint(G.evalf(3))
	#sympy.pprint(sympy.Float(G).round(3))
	#sympy.pprint(sympy.Float(G,3))
	D=diag(arange(4,0,-1))
	#D=eye(N)
	print(D)
	prod=H*D*G
	prod=prod.expand()
	#prod=prod.simplify()
	print("Prod=")
	sympy.pprint( prod.evalf(3,chop=True))

