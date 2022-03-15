from numpy import *
import matplotlib.pyplot as plt

f, phase_velocity, n, t, theta, d = 1, 1, 20, 5, radians(90), 100
pos = arange(n)/2 - mean(arange(n)/2)

plt.subplots(2, 2, figsize = (10, 5), dpi = 150)
for e, theta in enumerate(radians([45, 90, 135, 180])):
    for i in range(n):
        plt.subplot(2, 2, e+1); ax = plt.gca()
        radius = phase_velocity * (t - pos[i] * cos(theta)/phase_velocity)
        ax.add_artist(plt.Circle((pos[i], 0), radius , fill = False))
    x, y = [t*phase_velocity*cos(theta), [t*phase_velocity*sin(theta)]]
    plt.plot([x + d*sin(theta), x - d*sin(theta)], [y - d*cos(theta), y + d*cos(theta)], c = 'k', linewidth = 1)
    plt.xlim([-10, 10]); plt.ylim([0, 10])
    plt.tick_params(left=False,
                bottom=False,
                labelleft=False,
                labelbottom=False)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.01, hspace=0.02)