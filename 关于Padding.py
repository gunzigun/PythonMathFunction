import tensorflow as tf
import numpy as np 

#1张10*10的3通道的图像
input = tf.Variable(tf.random_normal([1,10,10,3]))

# ksize=[1, 3, 3, 1] 表示 3*3的池化核
# strides=[1, 3, 3, 1] 表示 步长为3（横向）*3（纵向）
x1 = tf.nn.max_pool(input, ksize=[1, 3, 3, 1], strides=[1, 3, 3, 1], padding = 'VALID')
x2 = tf.nn.max_pool(input, ksize=[1, 3, 3, 1], strides=[1, 3, 3, 1], padding = 'SAME')

# [3,3,3,1] 表示 卷积核3*3，3通道，1个核
filter = tf.Variable(tf.random_normal([3,3,3,1]))
# strides=[1,2,2,1] 表示 步长为2（横向）*2（纵向）
y1 = tf.nn.conv2d(input, filter, strides=[1,2,2,1], padding='VALID')
y2 = tf.nn.conv2d(input, filter, strides=[1,2,2,1], padding='SAME')

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    a1,a2 = sess.run(x1),sess.run(x2)
    print("VALID池化后尺寸：", a1.shape, "\nSAME池化后尺寸：", a2.shape)
    b1,b2 = sess.run(y1),sess.run(y2)
    print("VALID卷积后尺寸：", b1.shape, "\nSAME卷积后尺寸：", b2.shape)  