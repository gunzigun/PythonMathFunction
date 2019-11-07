import numpy as np
import matplotlib.pyplot as plt

#定义x散点坐标
x = [36.9,46.7,63.7,77.8,84.0,87.5]
x = np.array(x)
print('x is :\n',x)

#定义y散点坐标
num = [181,197,235,270,283,292]
y = np.array(num)
print('y is :\n',y)

#用1次多项式拟合
f1 = np.polyfit(x, y, 1)
print('f1 is :\n',f1)
p1 = np.poly1d(f1)
print('p1 is :\n',p1)
#用拟合的曲线，求值
yvals=np.polyval(f1, x)
print('yvals1 is :\n', yvals)

#绘图
plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('polyfitting')
plt.show()