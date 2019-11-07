import math

N_ALL_STACK = 25      #一共最多25个槽
one = [0] * (N_ALL_STACK+1) #one[i],表示有i个槽，第一个槽深度为1（1打头）的钥匙个数，1打头的和6打头的数目相同，只用设置one数组
two = [0] * (N_ALL_STACK+1) #two[i],表示有i个槽，第一个槽深度为2（2打头）的钥匙个数，2,3,4,5打头的数目项目，只用设置two数组
lock = [0] * (N_ALL_STACK+1) #lock[i]表示i个槽时的钥匙个数，lock[i] = one[i]*2 + two[i]*4
#槽数小于等于3时，结果易知
one[1],one[2],one[3] = 0,0,16
two[1],two[2],two[3] = 0,0,18

for i in range (1,N_ALL_STACK+1):
    if i > 3:
        #（1打头）当前i个槽是钥匙，但是去掉第一个后，不再是钥匙    [(2,3)(2,4)(2,5)(3,4)(3,5)(4,5)]、[(2,6)(3,6)(4,6)(5,6)]
        a = (math.pow(2,(i-1))-2) * 6 + (math.pow(2,(i-2))-1) * 4
        one[i] = one[i-1] + two[i-1] * 4 + a 
        #（2打头）当前i个槽是钥匙，但是去掉第一个后，不再是钥匙    [(1,3)(1,4)(1,5)(3,4)(3,5)(3,6)(4,5)(4,6)(5,6)]
        b = (math.pow(2,(i-1))-2) * 9
        two[i] = one[i-1] * 2 + two[i-1] * 4 + b
    
    lock[i] = one[i]*2+two[i]*4
    print ("当有%i个槽时，钥匙数为%i" % (i,lock[i]))












