import numpy as np
import matplotlib.pyplot as plt
from math import *
from os import path

def f(x):
    if -1 <= x < 0:
        return x+5.0/3
    elif 0 <= x < 2:
        return -x + 5.0/3
    elif 2<= x < 4:
        return 0
    elif x>=4:
        return f(x-5)
    elif x<=-1:
        return f(x+5)


def an (n):
    return (sin(n*pi/5)**2 * (45 + 30* cos(2*n*pi/5) + 4 *n * pi * sin(2*n*pi/5)))/(3 *n*n*pi*pi)
def bn(n):
    return (15 * (sin(2*(pi * n /5)) - sin(4*(pi * n /5))) + 4* pi * n * cos((pi * n /5)*2) + 2 * pi *n * cos((pi * n /5)*4))/(n*n * 6 * pi*pi)

a0 = 1/2
def make_trig_sum(an , bn , a0 , N):
    def func(x):
        retval = a0
        for i in range(1,N+1 , 1):
            retval += an(i) * cos(2*pi/5* i * x) + bn(i) * sin(2*pi/5* i * x)
        return retval
    return func

def sequence_print(n):
    for i in range(1,n+1,1):
        print(f"$$a_{{ {i} }} = {an(i)} , b_{{ {i} }} = {bn(i)}$$\n")

x= np.linspace(-1 ,4 , 20000)


y_original =  np.array(list(map(f, x)))
mse = []
for i in range(1,51,1):
    func = make_trig_sum(an,bn,a0,i)
    y_new =  np.array(list(map(func, x)))


    mse.append( np.mean( np.square(y_new - y_original) , axis=None) )

x = [i for i in range(1,51,1)]

fig , axs= plt.subplots(1 , figsize = (7,7))
axs.plot(x,mse)

plt.savefig("6-3.pdf")
plt.show()




