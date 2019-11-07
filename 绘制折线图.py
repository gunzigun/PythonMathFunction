import matplotlib.pyplot as plt
from pylab import *                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']
 
names = ['None', 'Transfer', 'GAN', 'Transfer-GAN']
x = range(len(names))
fasterrcnn = [0.000000, 0.629852, 0.614311, 0.618061]
rfcn = [0.482297, 0.463448, 0.484668, 0.470273]
fpn = [0.642646, 0.680547, 0.566679, 0.636972]
plt.plot(x, fasterrcnn, marker='o', mec='r', mfc='w',label=u'Faster-RCNN')
plt.plot(x, rfcn, marker='*', ms=10,label=u'R-FCN')
plt.plot(x, fpn, marker='v', ms=10,label=u'FPN')

plt.legend() # 让图例生效
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"time(s)邻居") #X轴标签
plt.ylabel("mAP") #Y轴标签
plt.title("Diff Mode Compare") #标题
 
plt.show()