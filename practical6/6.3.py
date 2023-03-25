costs = [1, 8, 15, 7, 5, 14, 43, 40]
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Los Angeles 1984", "Seoul 1988", "Barcelona 1992", "Atlanta 1996", "Sydney 2000", "Athens 2003", "Beijing 2008", "London 2012"])
y = np.array([1, 8, 15, 7, 5, 14, 43, 40])

plt.bar(x,y, color="red")
plt.show()


