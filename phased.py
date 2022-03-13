from numpy import *
import matplotlib.pyplot as plt

def e(x, y, z, w): 
    # Wave propagation
    v = array([x, y, z])
    n = maximum(linalg.norm(v), 1)
    return cos((n + w) * 2 * pi) / n**2

# Simulation

n_elements = 4
pos = arange(n_elements)/2
pos -= mean(pos)
theta = 90
w = arange(0, n_elements/2, 0.5) * cos(radians(theta))
x, y = meshgrid(linspace(-10, 10, 300),  linspace(0, 20, 300))

plt.figure(figsize = (5, 5), dpi = 150)
e_tot = sum(e(x + pos[i], y, 0, w[i]) for i in range(len(pos)))
plt.scatter(x, y, s = 7, c = e_tot < 0.01, cmap = "Greys")
plt.xlim([-10, 10])
plt.ylim([0, 20])

## Theory

theta=linspace(0, 360, 1000)
f=1e9
c=3e8
l=c/f;
d=l/2;
n = arange(n_elements).reshape(n_elements, 1)

A=(n-1)*(1j*2*pi*d*tile(cos(radians(theta)), (n_elements, 1))/l)
X=exp(-A)
w=ones(n_elements).reshape(n_elements, 1)
r=w.T@X

plt.figure(figsize=(5, 5), dpi = 100)
plt.polar(radians(theta), abs(r).T)
plt.show()
