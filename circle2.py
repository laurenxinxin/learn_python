import math

print("你好，请输入要计算的最大半径，我们将从半径为0开始输出")
r = int(input())
i=0
pie=3.14
print("半径  整数乘法  小数乘法  周长    面积")

while i <= r:
    print(round(i,2), round(pie*i,2),round(pie*i/10,3),round(2*pie*i,2), round(pie*math.pow(i,2),2))
    i=i+1
