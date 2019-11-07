import numpy as np 

#用于记录每个判断矩阵一致性检验时的CI、RI
CI_list=[]
RI_list=[]

#得到最大特征值特征值和对应的特征向量
def get_tezheng(mat):          
    n=mat.shape[0]     
    te_value,te_vectors=np.linalg.eig(mat)         #此时te_vectors为矩阵形式
    list1=list(te_value)                           
    max_value=np.max(list1)
    index=list1.index(max_value)                   #根据值找到在列表中的索引      # numpy中array不能根据值来找索引，所以必须以列表形式
    max_vector_mat=te_vectors[:,index]             #max_vector为矩阵形式 
    max_vector_array=np.array(max_vector_mat.T)    #max_vector_array为求得特征向量的数组形式，以行排列 ； 因为数组由矩阵生成，所以是[[]]形式（两个[])，shape为（1，n）
    max_vector_array=max_vector_array[0]           #将[[]]形式的array变成[]的array
    print("特征值为：",max_value)
    return n,max_value,max_vector_array

#检验   
def single_check(n,value):    
    CI=(value-n)/(n-1)
    RI=[0,0,0.58,0.90,1.12,1.24,1.32,1.41,1.45] 
    CR=CI/RI[n-1]
    print("CR:",CR)
    if CR<0.1:
        print("满足一致性")
    else:
        print("不满足一致性，请进行修改")
    CI_list.append(CI)
    RI_list.append(RI[n-1])


#归一化处理
def normalisze_vector(max_vector):
    vector_sum=np.sum(max_vector)
    vector_normalize=[]                        #vector_normalize为一个列表
    for i in range(max_vector.shape[0]):
         vector_normalize.append(max_vector[i]/vector_sum)
    print("该级指标的权重为：",vector_normalize,"\n")
    return vector_normalize                        #函数以列表形式返回
             

#对于单个成对比判断矩阵，进行层次单排序
def single_paixu(mat_single):
    n,max_value,max_vector=get_tezheng(mat_single)
    single_check(n,max_value)
    normalise_single=normalisze_vector(max_vector)
    return normalise_single

#层次总排序
def all_paixu(normalarray):
    B_1=[]
    for i in range(1,(normalarray.shape[0])):
        normalarray[i]=normalarray[i]*normalarray[0]
        B_1.append(np.sum(normalarray[i]))
    return B_1                                     #返回一个列表

#B层总排序随机一致性检验
def all_check():                                  
    del CI_list[0]           #移除A层x_0作一致性检验时产生的CI、RI
    del RI_list[0]
    CR_all=np.sum(np.array(CI_list)*np.array(x_0))/np.sum(np.array(RI_list)*np.array(x_0))     #列表相加[1,2]+[3,4]产生[1,2,3,4] 列表重复[1,2]*2产生[1,2,1,2]
    if CR_all<0.1:                                                                             #python中的广播不适用于列表，用于数组和矩阵
        print("总排序满足一致性")                                                               #利用Python时，行和列必须有一个相同才行
    else:
        print("总排序不满足一致性，请进行修改")
    print("CR_all: ",CR_all)
     
x_0=np.mat([[1,1,1,4,1,1/2],[1,1,2,4,1,1/2],[1,1/2,1,5,3,1/2],[1/4,1/4,1/5,1,1/3,1/3],[1,1,1/3,3,1,1],[2,2,2,3,3,1]])
a=np.mat([[1,1/4,1/2],[4,1,3],[2,1/3,1]])
b=np.mat([[1,1/4,1/5],[4,1,1/2],[5,2,1]])
c=np.mat([[1,3,1/3],[1/3,1,1/7],[3,7,1]])
d=np.mat([[1,1/3,5],[3,1,7],[1/5,1/7,1]])
e=np.mat([[1,1,7],[1,1,7],[1/7,1/7,1]])
f=np.mat([[1,7,9],[1/7,1,1],[1/9,1,1]])
x_0=single_paixu(x_0)
a=single_paixu(a)     #a为列表形式   
b=single_paixu(b)
c=single_paixu(c)
d=single_paixu(d)
e=single_paixu(e)
f=single_paixu(f)
res_1=np.array(x_0)     #使用列表组成数组
res_2=np.array(np.mat(np.array([a,b,c,d,e,f])).T)   #使用列表组成数组,然后利用矩阵转置
res_3=np.vstack((res_1,res_2))    #将数组res_1和res_2垂直堆叠到一起。
ret=all_paixu(res_3)              #ret为一个列表
print("总排序权值: ",ret)
all_check()


    

