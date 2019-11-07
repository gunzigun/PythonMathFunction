import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 计算均值,要求输入数据为numpy的矩阵格式，行表示样本数，列表示特征    
# axis=0表示依照列来求均值。假设输入list,则axis=1
def meanX(dataX, axis=0):
    return np.mean(dataX,axis=0)

"""
參数：
    - XMat：传入的是一个numpy的矩阵格式，行表示样本数，列表示特征    
    - k：表示取前k个特征值相应的特征向量
返回值：
    - finalData：參数一指的是返回的低维矩阵，相应于输入參数二
    - reconData：參数二相应的是移动坐标轴后的矩阵
"""
def pca(XMat, k):
    average = meanX(XMat, axis=0) 
    m, n = np.shape(XMat)

    #average = np.array([1,2,3,4])
    #average是每一列的均值，然后复制4（m）行
    #np.tile(average,(4,1))
    #array([[1, 2, 3, 4],
    #       [1, 2, 3, 4],
    #       [1, 2, 3, 4],
    #       [1, 2, 3, 4]])
    data_adjust = []
    avgs = np.tile(average, (m, 1))

    data_adjust = XMat - avgs      #原矩阵去均值化    
    covX = np.cov(data_adjust.T)   #计算协方差矩阵
    featValue, featVec=  np.linalg.eig(covX)  #求解协方差矩阵的特征值和特征向量
    index = np.argsort(-featValue) #依照featValue进行从大到小排序
    finalData = []
    if k > n:
        print ("k must lower than feature number")
        return
    else:
        #注意特征向量时列向量。而numpy的二维矩阵(数组)a[m][n]中，a[1]表示第1行值
        selectVec = np.matrix(featVec.T[index[:k]]) #所以这里须要进行转置
        finalData = data_adjust * selectVec.T 
        reconData = (finalData * selectVec) + average  
    return finalData, reconData


#加载文件函数
def loaddata(datafile):
    return np.array(pd.read_csv(datafile,sep="\t",header=-1)).astype(np.float)

#界面显示
def plotBestFit(data1, data2):    
    dataArr1 = np.array(data1)
    dataArr2 = np.array(data2)

    m = np.shape(dataArr1)[0]
    axis_x1 = []
    axis_y1 = []
    axis_z1 = []
    axis_x2 = []
    axis_y2 = []
    axis_z2 = []
    
    for i in range(m):
        axis_x1.append(dataArr1[i,0])
        axis_y1.append(dataArr1[i,1])
        axis_z1.append(dataArr1[i,2])
        axis_x2.append(dataArr2[i,0]) 
        axis_y2.append(dataArr2[i,1])
        axis_z2.append(dataArr2[i,2]) 

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(axis_x1, axis_y1, axis_z1, c='red', marker='s')
    ax.scatter(axis_x2, axis_y2, axis_z2, c='blue',  marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

if __name__ == "__main__":
    
    datafile = "PCAdata.txt"
    XMat = loaddata(datafile)
    finalData, reconMat = pca(XMat, k=3)

    #蓝色部分为重构后的原始数据，红色则是提取后的二维特征！
    plotBestFit(finalData, reconMat)