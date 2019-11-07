import math

N_WELL_NUM = 12             #已有井的数目
N_REUSE_ACCURATE = 0.05     #可利用精确度
x = [0] * (N_WELL_NUM+1)    #记录y轴移动后的x坐标    
y = [0] * (N_WELL_NUM+1)    #记录x轴移动后的y坐标
x2 = [0] * (N_WELL_NUM+1)   #记录旋转后x坐标
y2 = [0] * (N_WELL_NUM+1)   #记录旋转后y坐标
D = [0] * (N_WELL_NUM+1)    #记录可利用的井编号

#函数，用于计算当前布局下有多少钻井可以被利用
def CanUseNum(n):
    nCount = 0   #临时变量，暂存可以利用的数目
    for k in range(1,n+1):
        #计算坐标距离最近坐标轴的相对位置
        dx = math.fabs(x2[k]-math.floor(x2[k]))
        dy = math.fabs(y2[k]-math.floor(y2[k]))
        dx = (1-dx) if dx > N_REUSE_ACCURATE else dx
        dy = (1-dy) if dy > N_REUSE_ACCURATE else dy
        #统计可以利用的数量
        if dx <= N_REUSE_ACCURATE and dy <= N_REUSE_ACCURATE:   #这行可以加快运算
            d = math.sqrt(dx*dx + dy*dy)
            if d > N_REUSE_ACCURATE:
                nCount = nCount + 1      #可利用数加1
                D[nCount] = k            #记录可利用编号
    return nCount

#输入初始旧井坐标和相关输入
a = [0,0.50,1.41,3.00,3.37,3.40,4.72,4.72,5.43,7.57,8.38,8.98,9.50] #[0] * (N_WELL_NUM+1)
b = [0,2.00,3.50,1.50,3.51,5.50,2.00,6.24,4.10,2.01,4.50,3.41,0.80] #[0] * (N_WELL_NUM+1) 
Angle = int(input("请输入坐标最多旋转的角度:\n"))
"""
print ("一共需要输入%i个旧井坐标:" % N_WELL_NUM)
for i in range(1,N_WELL_NUM+1):
    a[i] = float(input("请输入第%i个旧井x坐标:\n" % i))
    b[i] = float(input("请输入第%i个旧井y坐标:\n" % i))
"""
print ("已有矿井x坐标数组：", a)
print ("已有矿井y坐标数组：", b)

N_TEMP_MAX_NUM = 0   #暂存可利用的最大数目
N_XMOVE = 0          #暂存x坐标改变量
N_YMOVE = 0          #暂存y坐标改变量
N_ANGLE = 0          #暂存角度改变量
E = [0] * (N_WELL_NUM+1)   #暂存最大可利用的井编号
#y轴平移，x坐标改变
for xmove in range(1,100):
    for k in range(1,N_WELL_NUM+1):
        x2[k] = x[k] = a[k] + xmove/100.0   #每次x坐标增加0.01（1米），相当于y轴左移1米
    #x轴平移，y坐标改变
    for ymove in range(1,100):
        for k in range(1,N_WELL_NUM+1):
            y2[k] = y[k] = b[k] + ymove/100.0   #每次y坐标增加0.01（1米），相当于x轴下移1米
        #处理旋转      
        for alph in range(0,Angle+1):
            if alph > 0:
                for k in range(1,N_WELL_NUM+1):
                    L = math.sqrt(x[k]*x[k] + y[k]*y[k])
                    beta = math.atan2(y[k],x[k]) + alph*3.1415926535/180
                    x2[k] = L * math.cos(beta)
                    y2[k] = L * math.sin(beta)

            #统计最大值
            num = CanUseNum(N_WELL_NUM)
            if num > N_TEMP_MAX_NUM:
                N_TEMP_MAX_NUM = num
                N_XMOVE = xmove
                N_YMOVE = ymove
                N_ANGLE = alph
                E = D[:]

print ("最大可利用数目为：%i \n" % N_TEMP_MAX_NUM)
print ("x坐标偏移：%i \n " % N_XMOVE)
print ("y坐标偏移：%i \n" % N_YMOVE)
print ("旋转角度：%i \n" % N_ANGLE)
print ("可利用编号", E)      