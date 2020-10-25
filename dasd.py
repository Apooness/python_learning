import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
"""
x = np.linspace(0,2,100)
y = x ** 2
z = x ** 3
t = x ** 4

fig , ax = plt.subplots(4)
ax[0].plot(x,x,color = "r",label = "linear")

ax[1].plot(x,y,color = "b",label = "Square")

ax[2].plot(x,z,color = "y",label = "Cube")

ax[3].plot(x,t,color = "g",label = "Fourable")
plt.tight_layout()
plt.legend()
plt.show()
"""

x = np.linspace(0,2,100)

fig , ax = plt.subplots()
ax.plot(x,x,color = "red",label = "Linear",marker = "x")
ax.plot(x,x**2,color = "green",label = "Square",marker = "o")
ax.plot(x,x**3,color = "blue",label = "Cube",marker = ".")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
plt.title("Başlık")
ax.legend()
plt.show()
