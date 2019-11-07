import pandas as pd 
import numpy as np 
import math
import xlrd

class GrayForecast:    
    def __init__(self,name):     #构造函数
        self.train_data=np.array(pd.read_excel(name))
        
        n=self.train_data.shape[0]
        self.x_0=np.zeros(n)
        self.x_1=np.zeros(n)             #1-ago生成值序列
    
    def level_check(self):       # 级比检验
        self.fag=True    #级比检验是否合格的标识，合格为真
        self.C_max=0
        n=self.train_data.shape[0]
        self.lambda_k=np.zeros(n-1)       #用法：zeros(shape, dtype=float, order='C')   返回：返回来一个给定形状和类型的用0填充的数组；
        for i in range(self.x_0.shape[0]):
               self.x_0[i]=self.train_data[i][1]
        flag=True
        for i in range(n-1):
            self.lambda_k[i]=self.train_data[i][1]/self.train_data[i+1][1]
            if self.lambda_k[i]<np.exp(-2/(n+1)) or self.lambda_k[i]>np.exp(2/(n+1)):
                flag=False
        print (np.exp(-2/(n+1)))
        print (np.exp(2/(n+1)))
        print("进行级比检验，并输出级比")
        print(self.lambda_k)
        if flag:
            print("级比检验成功，请继续")
        else:
            print("级比检验失败，请做变换处理")
            self.fag=False
            x_low=np.zeros(0)
            x_high=np.zeros(0)
            
            for i in range (n-1):
                if self.lambda_k[i]<np.exp(-2/(n+1)):  #求得级比小于np.exp(-2/(n+1))的值，并计算相应的最小平移量
                     x_low=np.append(x_low,(self.x_0[i]-np.exp(-2/(n+1))*self.x_0[i+1])/(np.exp(-2/(n+1))-1))
                    
                elif self.lambda_k[i]>np.exp(2/(n+1)):  #求得级比大于np.exp(2/(n+1))的值，并计算相应的最小平移量
                     x_high=np.append(x_low,(self.x_0[i]-np.exp(2/(n+1))*self.x_0[i+1])/(np.exp(2/(n+1))-1))
            a=np.max(x_low)
            
            self.C_max=a
            if x_high.shape[0]!=0:     #找到其中最大的平移量
                b=np.max(x_high)       #数组元素个数为0时不能用max()求取其最大值
                if a>=b:
                     self.C_max=a
                else:
                     self.C_max=b
            self.x_0=self.x_0+self.C_max
            print("输出最小平移量C值")
            print(self.C_max)
            print("输出平移后数据")
            print(self.x_0)
            flag=True
            for i in range(n-1):
                 self.lambda_k[i]=self.x_0[i]/self.x_0[i+1]
                 if self.lambda_k[i]<np.exp(-2/(n+1)) or self.lambda_k[i]>np.exp(2/(n+1)):
                     flag=False
            
            print("进行级比检验，并输出级比")
            print(self.lambda_k)
            if flag:
                 print("级比检验成功，请继续")

    def GM_11_parameter(self):    #计算模型参数
            #可用range（end）函数来生来包含多个整数的range对象，生成数范围为0-end-1，例如for i in range（2），生成0，1, for i in range(-2,2) 生成 -2，-1,0，1,
            for i in range(self.x_0.shape[0]): 
                for j in range(i+1):
                    self.x_1[i]=self.x_1[i]+self.x_0[j]    
               
            z_1=np.zeros(len(self.x_0)-1)              #紧邻均值生成序列
            for i in range(1,len(self.x_0)):
                z_1[i-1]=-0.5*(self.x_1[i]+self.x_1[i-1])
            B=np.append(np.array(np.mat(z_1).T),np.ones((z_1.shape[0],1)),axis=1)
            
            Y_0=np.zeros(self.x_0.shape[0]-1)   #因为Y是从第二个数开始，也即x_0[1]开始
            for i in range (1,self.x_0.shape[0]):
               Y_0[i-1]=self.x_0[i]
            Y=np.array(np.mat(Y_0).T)
            
            B=np.mat(B)
            Y=np.mat(Y)
            u=np.linalg.inv(B.T*B)*B.T*Y


            self.a=np.array(u.T)[0][0]
            self.b=np.array(u.T)[0][1]
            
    def GM_11_build(self,k):   #得出模型的最后预测公式
            x_forecast=(self.x_0[0]-self.b/self.a)*(1-np.exp(self.a))*np.exp(-self.a*(k))  #k=1,2,.......,n-1 为原始序列的拟合值，k>=n时是预报值
            return x_forecast     
    
    def forecast(self):
            x_0_forecast=np.zeros(self.x_1.shape[0]+3)
            
            for i in range(1,self.x_0.shape[0]+3):     
                 x_0_forecast[i]=self.GM_11_build(i)
            x_0_forecast[0]=self.x_0[0] 
            return x_0_forecast
    
    def relative_residual(self):
        n=self.train_data.shape[0]
        self.rt_residual=np.zeros(n)       
        flag=True
        for i in range(n):            #计算相对残差
            self.rt_residual[i]=(self.x_0[i]-x_01[i])/self.x_0[i]
        print("计算相对残差并输出")
        print(self.rt_residual)
        for i in range(n):
            if math.fabs(self.rt_residual[i])>=0.1:
                flag=False
        if flag:                      #没有值比0.1大
            print("模型精确度达到较高要求")
        else:                       #有值比0.1大
            flag=True
            for i in range(n):
                if math.fabs(self.rt_residual[i])>=0.2:
                    flag=False          #如果有值比0.2大，则精度不达标
            if flag:                    #如果flag为真，则没有数据比0.2大
                print("模型精确度达到一般要求") 
            else:
                print("模型精确度较低，不达标")
        p=(1-(1/(n))*np.sum(np.fabs(self.rt_residual)))
        print("输出精度")
        print(p)
    
    def jibi_piancha(self):
        n=self.train_data.shape[0]
        jibi_cha=np.zeros(n-1)       
        flag=True
        for i in range(n-1):            #计算级比偏差
            jibi_cha[i]=1-(1-0.5*self.a)/(1+0.5*self.a)*self.lambda_k[i]
        print("计算级比偏差并输出")
        print(jibi_cha)
        for i in range(n-1):
            if math.fabs(jibi_cha[i])>=0.1:
                flag=False
        if flag:                      #没有值比0.1大
            print("模型精确度达到较高要求")
        else:                       #有值比0.1大
            flag=True
            for i in range(n-1):
                if math.fabs(jibi_cha[i])>=0.2:
                    flag=False          #如果有值比0.2大，则精度不达标
            if flag:                    #如果flag为真，则没有数据比0.2大
                print("模型精确度达到一般要求") 
            else:
                print("模型精确度较低，不达标")
    

gf=GrayForecast("灰度预测data.xlsx") 
gf.level_check()        #进行级比检验
gf.GM_11_parameter()    #求得模型参数a,b
x_01=gf.forecast()      
print("输出模型预测值")
print (x_01)
if not gf.fag:
    x_01=x_01-gf.C_max    #将得到的预测值减去平移量C_max 
    gf.x_0=gf.x_0-gf.C_max
    print("由于进行了平移变化，输出变换之后得到的预测值对应的原始值")
    print(x_01)

gf.relative_residual()  #相对残差检验预测值
gf.jibi_piancha()       #级比偏差检验预测值



    
          
    
               
            
        
            
            

          
          
          
          


        

     