import math as m
import matplotlib.pyplot as plt

X = input("Input equation x(n):")
def xN(n):
    return eval(X)

def yN(n):
    if n == 0:
        e1 = -1.5*xN(n)+2*xN(n+1)-0.5*xN(n+2)
        return e1
    elif n > 0 and n <= 198:
        e2 = 0.5*xN(n+1)-0.5*xN(n-1)
        return e2
    elif n == 199:
        e3 = 1.5*xN(n)-2*xN(n-1)+0.5*xN(n-2)
        return e3
    
N = list(range(0,200))
x = [xN(n) for n in N]
y = [yN(n) for n in N] 

plt.plot(N,x,'y',label = 'x(n)')
plt.plot(N,y,'r',label = 'y(n)')
plt.xlabel('n')
plt.ylabel('x(n) and y(n)')
plt.title('Superimpose')
plt.legend()
plt.show()
