
import matplotlib.pyplot as plt
import numpy as np
import math

np.random.seed()

mas_ravn = np.random.random(1000) 

a = 2
b = 9

mas_ravn_a_b=a+(b-a)*mas_ravn 

print(mas_ravn_a_b)

k=int(1.44*math.log(1000) + 1)

fig, ax = plt.subplots()

ax.hist(mas_ravn_a_b, bins=k, linewidth=0.5, edgecolor="white")

plt.show()