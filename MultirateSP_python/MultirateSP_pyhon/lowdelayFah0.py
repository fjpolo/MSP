from sympy import *
from numpy import *

N=4;
#init_printing()
z=symbols('z')
g=symbols('g:2')
h=symbols('h:8')
omega=symbols('omega');

#Fa=Matrix([[0, 1, 4, 0],[2, 0, 0, 3],[3, 0, 0, -2],[0, 4, -1, 0]])
Fa=Matrix([[0, -h[7], -h[3], 0],[-h[6], 0, 0, -h[2]],[-h[5], 0, 0, h[1]],[0, -h[4], h[0], 0]])
D=Matrix([[z**(-1), 0, 0, 0],[0, z**(-1), 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
G=Matrix([[g[0]*z**(-1), 0, 0, 1],[0, g[1]*z**(-1), 1, 0],[0, 1, 0, 0],[1, 0, 0,0 ]])

#Transform matrix T:
T=Matrix(zeros((N,N)));
for n in range(0,N):
   for k in range(0,N):
      T[n,k]=cos(pi/N*(n+0.5)*(k+0.5));

#Polyphase matrix H(z):
H=Fa*D*G*T;

H0n=H[:,0];

print(H0)

#upsampled H0:
H0nu=H0n.subs(z,z**4);
#phase delay vector:
ph=Matrix([[1/z**3,1/z**2,1/z,1]]);
#z-transform of subband filter 0:
H0=ph*H0nu;
H0omega=H0.subs(z,e**(1j*omega))


