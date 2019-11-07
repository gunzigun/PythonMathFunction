import scipy.stats

#pearson相关是最常见的相关公式，用于计算连续数据的相关
#比如计算班上学生数学成绩和语文成绩的相关可以用Pearson相关。

#spearman相关是专门用于分析顺序数据的，就是那种只有顺序关系，但并非等距的数据
#比如计算班上学生数学成绩排名和语文成绩排名的关系。

a = [1,2,3,4,5]
b = [1,2,3,4,5]

#参数（Pearson相关系数）
PearsonR = scipy.stats.pearsonr(a, b)
#非参数（Spearman相关系数）
#SpearmanR = scipy.stats.spearmanr(a, b)

print("Pearson相关系数", PearsonR)
#print("Spearman相关系数", SpearmanR)

