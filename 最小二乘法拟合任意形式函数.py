import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#自定义函数（可以任意指定 x是输入,a,b,c是需要求解的参数）
def func(x, a, b, c):
    return a*np.sqrt(x)*(b*np.square(x)+c)

#定义x、y散点坐标
x = [36.9,46.7,63.7,77.8,84.0,87.5]
x = np.array(x)
num = [181,197,235,270,283,292]
y = np.array(num)

#非线性最小二乘法拟合（一个函数搞定，popt里面是求出的参数值）
popt, pcov = curve_fit(func, x, y)
yvals = func(x,popt[0],popt[1],popt[2]) #拟合y值
print(popt)
print('系数pcov:', pcov)
print('系数yvals:', yvals)

#绘图
plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('curve_fit')
plt.show()

