###
# Then, using ‘matplotlib’, draw a line in a diagram from position (1, 3) to position (8, 10).
#
#Hint: to use 'matplotlib' in your programs, first you have to install the module by using the 'pip' command (python package manager).
#

import matplotlib.pyplot as plt
xpoints = [1, 8]
ypoints = [3, 10]
plt.plot(xpoints, ypoints)
plt.show()