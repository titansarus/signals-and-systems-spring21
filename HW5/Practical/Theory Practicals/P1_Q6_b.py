import numpy as np
import matplotlib.pyplot as plt
from math import *

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

sequence_print(50)

x= np.linspace(-10 ,10 , 20000)

f1 = make_trig_sum(an , bn , a0 , 1)
f4 = make_trig_sum(an , bn , a0 , 4)
f9 = make_trig_sum(an , bn , a0 , 9)
f23 = make_trig_sum(an , bn , a0 , 23)
f47 = make_trig_sum(an , bn , a0 , 47)




fig, axs = plt.subplots(6 , figsize=(7,7))
fig.suptitle('Amirmahdi Namjoo')
axs[0].set_title("f(x)")
axs[1].set_title("N=1")
axs[2].set_title("N=4")
axs[3].set_title("N=9")
axs[4].set_title("N=23")
axs[5].set_title("N=47")
axs[0].plot(x, np.array(list(map(f, x))))
axs[1].plot(x, np.array(list(map(f1, x))))
axs[2].plot(x, np.array(list(map(f4, x))))
axs[3].plot(x, np.array(list(map(f9, x))))
axs[4].plot(x, np.array(list(map(f23, x))))
axs[5].plot(x, np.array(list(map(f47, x))))

fig.tight_layout()

plt.show()

fig , axs= plt.subplots(5 , figsize = (7,7))
axs[0].set_title("N=1")
axs[1].set_title("N=4")
axs[2].set_title("N=9")
axs[3].set_title("N=23")
axs[4].set_title("N=47")

axs[0].plot(x, np.array(list(map(f, x))))
axs[0].plot(x, np.array(list(map(f1, x))))

axs[1].plot(x, np.array(list(map(f, x))))
axs[1].plot(x, np.array(list(map(f4, x))))

axs[2].plot(x, np.array(list(map(f, x))))
axs[2].plot(x, np.array(list(map(f9, x))))

axs[3].plot(x, np.array(list(map(f, x))))
axs[3].plot(x, np.array(list(map(f23, x))))

axs[4].plot(x, np.array(list(map(f, x))))
axs[4].plot(x, np.array(list(map(f47, x))))

fig.tight_layout()

plt.savefig("6-2.pdf")
plt.show()