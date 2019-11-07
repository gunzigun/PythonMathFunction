import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn import preprocessing
 
 
#读取数据
train_data=np.array(pd.read_excel("xlsx-train.xlsx"))
test_data=np.array(pd.read_excel("xlsx-test.xlsx"))
 
#提取特征列,即X (共4列，代表4个变量)
train_feature=np.array(train_data[:,[1,2,3,4]])
#提取预测结果列，即Y
train_label=np.array(train_data[:,[5]])
#提取测试集特征列
test_x=np.array(test_data[:,[1,2,3,4]])
print(test_data.shape)
 
#搭建神经网络
#定义x y
x = tf.placeholder(tf.float32,[None,4])  #长度为4，代表4个特征
y = tf.placeholder(tf.float32,[None,1])   #长度为1，代表要预测的变量只有1个
train_feature=preprocessing.scale(train_feature)  #数据预处理，归一化
test_xs=preprocessing.scale(test_x)    #也对测试集进行预处理
print(test_xs.shape)
 
#定义神经网络隐藏层
 
#初始化权值。 为4*20矩阵  20代表20个神经元
Weights_L1 = tf.Variable(tf.random_normal([4,20]))
#偏置矩阵
biases_L1 = tf.Variable(tf.zeros([1,20]))
Wx_plus_b_L1 = tf.matmul(x,Weights_L1)+biases_L1
#激活函数私有tanh
L1 = tf.nn.tanh(Wx_plus_b_L1)

 
#定义神经网络输出层
Weights_L2 = tf.Variable(tf.random_normal([20,1]))
biases_L2 = tf.Variable(tf.zeros([1,20]))
Wx_plus_b_L2 = tf.matmul(L1,Weights_L2)+biases_L2
prediction = Wx_plus_b_L2
 
#代价函数
loss = tf.reduce_mean(tf.square(y-prediction))
saver = tf.train.Saver()
 
#定义优化器。使用动量法 也可以使用随机梯度下降法等
train_step = tf.train.MomentumOptimizer(0.05,0.05).minimize(loss)
with tf.Session() as sess:
    #初始化变量
    sess.run(tf.global_variables_initializer())
    #writer=tf.summary.FileWriter("gra",graph=tf.get_default_graph())
    print(sess.run(loss, feed_dict={x: train_feature, y: train_label}))
    for i in range(30000):
        sess.run(train_step, feed_dict={x: train_feature, y: train_label})
        print(i)
        #print(sess.run(L1,feed_dict={x: train_feature, y: train_label}))
        print(sess.run(loss,feed_dict={x: train_feature, y: train_label}))
    prd=sess.run(prediction, feed_dict={x:test_xs })  #获取对测试集的预测结果
    f = open('Tensorflow实现多元回归re.txt', 'w')
    #写到文件
    for i in range(test_data.shape[0]):
        f.writelines(str(prd[i][0])+"\n")
        #f.writelines(str(test_data[i][0])+","+str(prd[i][0])+"\n")
    f.close()
    #保存模型
    saver.save(sess, "Tensorflow实现多元回归model/my-model")
    print(test_data.shape)
    print(np.column_stack((test_data, prd[:,0])))
