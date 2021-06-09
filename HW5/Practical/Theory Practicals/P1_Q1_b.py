import numpy as np
import matplotlib.pyplot as plt
from math import *

def f(x):
    if 0 <= x < pi/2:
        return 1
    elif pi/2 <= x < pi:
        return 0
    elif -pi <= x < 0:
        return 0


def an (n):
    return sin(n * pi /2.0) / (n * pi)

def bn(n):
    return (2* sin(n * pi /4) * sin(n * pi /4))/(n * pi)

a0 = 1/4
def make_trig_sum(an , bn , a0 , N):
    def func(x):
        retval = a0
        for i in range(1,N+1 , 1):
            retval += an(i) * cos(i * x) + bn(i) * sin(i * x)
        return retval
    return func

x= np.linspace(-pi , pi , 10000)

f2 = make_trig_sum(an , bn , a0 , 2)
f5 = make_trig_sum(an , bn , a0 , 5)
f20 = make_trig_sum(an , bn , a0 , 20)
f50 = make_trig_sum(an , bn , a0 , 50)


fig, axs = plt.subplots(5 , figsize=(7,7))
fig.suptitle('Amirmahdi Namjoo')
axs[0].set_title("f(x)")
axs[1].set_title("N=2")
axs[2].set_title("N=5")
axs[3].set_title("N=20")
axs[4].set_title("N=50")
axs[0].plot(x, np.array(list(map(f, x))))
axs[1].plot(x, np.array(list(map(f2, x))))
axs[2].plot(x, np.array(list(map(f5, x))))
axs[3].plot(x, np.array(list(map(f20, x))))
axs[4].plot(x, np.array(list(map(f50, x))))

fig.tight_layout()

plt.show()