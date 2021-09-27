"""
Filename: ps-1.py
-------------------------------
By: Marcus Forst

Base code credit: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
I used the above to see how to write sine graphs in python.

"""

# importing the required modules
import matplotlib.pyplot as plt
import numpy as np

# A_n Coefficients:
A_0 = 0 # This is unnecessary but interesting to note
        # that the average value is 0
A_1 = 1
A_2 = 1/2
A_3 = 1/3
A_4 = 1/4
A_5 = 1/5

# create list of coefficients
A_N_LIST = [A_1, A_2, A_3, A_4, A_5]

# setting the x - coordinates
x = np.arange(0, 2 , 0.01)
# setting the corresponding y - coordinates





y = 0
for n in range(5):
    y -= A_N_LIST[n] * np.sin(2*(np.pi) * (n+1) * x )

# poltting the points
plt.plot(x, y)

# function to show the plot
plt.show()
