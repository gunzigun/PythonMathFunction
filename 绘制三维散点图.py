from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#在vmin-vmax范围，随机生成n个数值
def randrange(n, vmin, vmax):
    return (vmax - vmin) * np.random.rand(n) + vmin


def scatter3D(xs, ys, zs, color='r', marker='o'):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs, ys, zs, c=color, marker=marker)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()


#生成一系列点
n = 100
xs = randrange(n, 23, 32)
ys = randrange(n, 0, 100)
zs = randrange(n, -50, -25)

#color表示颜色 'r', 'b'
color = 'r'
#marker表示标志 'o', '^'
marker = '^'

scatter3D(xs, ys, zs, color=color, marker=marker)