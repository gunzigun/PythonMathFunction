import numpy as np
import scipy.stats as ss
from statsmodels.graphics.api import qqplot
from matplotlib import pyplot as plt

#P值（P value）就是当原假设为真时所得到的样本观察结果或更极端结果出现的概率.
#如果P值很小,说明原假设情况的发生的概率很小,
#而如果出现了,根据小概率原理,我们就有理由拒绝原假设,
#P值越小,我们拒绝原假设的理由越充分.总之,P值越小,表明结果越显著


#1、正态分布检验
#创建一个20的正态分布的数据
norm_dist=ss.norm.rvs(size=20)
#normaltest基于偏度，和峰度的检验方法，检验是否符合正态分布
#输出:statistic统计值  pvalue  P值>0.05表示符合正态分布
pvalue = ss.normaltest(norm_dist)
print("正态分布检验结果：", pvalue)
#qq图
#散点图基本位于角平分线上说明符合正态分布
#plt.show(qqplot(ss.norm.rvs(size=100)))


#2、卡方检验
#输入：检验统计量，P值，自由度，理论分布
ss.chi2_contingency([[1,2],[1,2]])
#独立t分布检验（检验两组值是否有较大差异）
#输出：统计量statistic，P值 pvalues
pvalues = ss.ttest_ind(ss.norm.rvs(size=100),ss.norm.rvs(size = 200))
print("卡方检验结果：", pvalues)


#3、方差检验
#输出  统计量statistic，P值pvalue
pvalue = ss.f_oneway([49,50,39,40,43],[28,32,30,26,34])
print("方差检验结果：", pvalue)


#4、主成分分析（PCA）
data=np.array([np.array([2.5,0.5,2.2,1.9,3.1,2.3,2,1,1.5,1.1]),np.array([2.4,0.7,2.9,2.2,3,2.7,1.6,1.1,1.6,0.9])]).T
#sklearn模块的降维方法PCA(奇异值分解的方法)
from sklearn.decomposition import PCA
#降成1维
lower_dim=PCA(n_components=1)
lower_dim.fit(data)
#维度的重要性，降维后多少的信息量
print(lower_dim.explained_variance_ratio_)
#转化后的数值
print("主成分分析（PCA）结果:",lower_dim.fit_transform(data))
