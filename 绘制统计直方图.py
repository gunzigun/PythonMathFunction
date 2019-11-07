import matplotlib.pyplot as plt
import numpy as np
import sys

print (sys.argv)


x = np.random.randn(1000)
#print ('生成的数据:\n', x)

plt.hist(x,20,rwidth=0.85)

plt.show()