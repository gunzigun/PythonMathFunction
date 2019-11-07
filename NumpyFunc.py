import numpy as np

def function1():
    my_array = np.array([1,2,3,4,5])
    print(my_array)
    print(my_array.shape)
    print(my_array[0])
    print(my_array[1])
    my_array[0] = -1
    print(my_array)

    my_new_array = np.zeros((5))
    print (my_new_array)

    my_new2_array = np.zeros((2,3))
    print (my_new2_array)

    #取0-1的随机数
    my_randon_array = np.random.random((5))
    #变成0-10的随机数，trunc是取整函数，还有ceil和floor
    print (np.trunc(my_randon_array*10))

    my_array = np.array([[4, 5], [6, 1]])
    print(my_array[0][1])
    print(my_array.shape)

    #取出第1列
    print(my_array[:,1])
    #取出第1行
    print(my_array[1,:])

    a = np.array([[1.0, 2.0], [3.0, 4.0]])
    b = np.array([[5.0, 6.0], [7.0, 8.0]])
    sum = a + b
    difference = a - b
    product = a * b
    quotient = a / b

    print ("Sum = \n", sum)
    print ("“Difference = \n", difference)
    print ("“Product = \n", product)
    print ("“Quotient = \n", quotient)

    matrix_product = a.dot(b)
    print ("Matrix_Product = \n", matrix_product)

    TempArrayA = np.arange(25)
    TempArrayA = TempArrayA.reshape((5,5))
    print(TempArrayA)

    #指定0-100，间隔10
    a = np.arange(0,100,10)
    print (a) 
    #返回指定元素
    indices = [1,5,-1]
    b = a[indices]
    print (b)

    #根据范围定义数组
    array_avg = np.linspace(0,2*np.pi,5)
    print (array_avg)

    #python的bool屏蔽
    import matplotlib.pyplot as plt
    a = np.linspace(0,2*np.pi,50)
    b = np.sin(a)
    plt.plot(a,b)
    mask = b >= 0
    plt.plot(a[mask],b[mask],'bo')
    mask = (b >= 0) & (a <= np.pi/2)
    plt.plot(a[mask],b[mask],'go')
    plt.show()


#numpy使用说明
#function1()

epoch = 1
if epoch % 1 == 0 & epoch != 0: 
    print("进来了1")

if epoch % 1 == 0 and epoch != 0: 
    print("进来了2")
