import numpy as np
import matplotlib.pyplot as plt

n = 10000 # took about 45 seconds, slow...
coords = primes(n)
fig = plt.figure()
ax = fig.add_subplot(projection = 'polar')
for val in coords:
    c = ax.scatter(val, val)
