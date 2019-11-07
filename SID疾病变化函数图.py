import scipy.integrate as spi
import numpy as np
import pylab as pl
 
#染病率
beta=20000
#死亡率
gamma=0.00263416
#年份间隔
TS=3.0
#开始年份
Start = 2007.0
#结束年份
End = 2022.0
#健康人口比
S0=0.99912192
#发病人口比
I0=0.00087424
#死亡人口比
D0=0.00000384
#初始输入
INPUT = (S0, I0, D0)

def diff_eqs(INP,t):
    '''The main set of equations'''
    Y=np.zeros((3))
    V = INP
    Y[0] = - beta * V[0] * V[1]
    Y[1] = beta * V[0] * V[1] - gamma * V[1]
    Y[2] = gamma * V[1]
    return Y   # For odeint
 
t_start = Start; t_end = End; t_inc = TS
t_range = np.arange(t_start, t_end+t_inc, t_inc)
RES = spi.odeint(diff_eqs,INPUT,t_range)

print(RES)


Y2004 = np.array([[0.200001388,0.19938914,0.037303733]])
Y2007 = np.array([[0.199971721,0.239189743,0.132681709]])
Y2010 = np.array([[0.199997218,0.203719162,0.210668608]])
Y2013 = np.array([[0.200009896,0.18585821,0.277633358]])
Y2016 = np.array([[0.200019778,0.171843745,0.341712592]])
RES1 = np.row_stack((Y2004, Y2007))
RES1 = np.row_stack((RES1, Y2010))
RES1 = np.row_stack((RES1, Y2013))
RES1 = np.row_stack((RES1, Y2016))
print(RES1)


#Ploting
pl.plot(RES1[:,0], '-bs', label='Susceptibles')  # I change -g to g--  # RES[:,0], '-g',
pl.plot(RES1[:,2], '-g^', label='Deads')  # RES[:,2], '-k',
pl.plot(RES1[:,1], '-ro', label='Infectious')
pl.legend(loc=0)
pl.title('SIR epidemic without births or nature deaths')
pl.xlabel('Year')
pl.ylabel('Susceptibles Deads Infectious')
pl.savefig('2.1-SIR-high.png', dpi=900) # This does, too
pl.show()