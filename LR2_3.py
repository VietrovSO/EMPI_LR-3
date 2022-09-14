# нормальний закон розподілу
import matplotlib.pyplot as plt
import numpy as np
import math

n = 1000
np.random.seed()

x = 2+np.random.normal(2, 1.5, n)
 #генєрування елементи за нормальним законом функції(мат.спод,середнє ариф.відх.,кіл.ел)
k=int(1.44*math.log(n)+1)
 #кількість інтервалів для гістограми

print("k= ", k)
print(x)

fig, ax = plt.subplots()

ax.hist(x, bins=k, linewidth=0.5, edgecolor="white")

plt.show()
