import numpy as np
import matplotlib.pyplot as plt
from functions import *

n = 10000 # took about 45 seconds, slow...
coords = primes(n)
fig = plt.figure()
ax = fig.add_subplot(projection = 'polar')
for val in coords:
    c = ax.scatter(val, val)
