import os
import math

def binary(low,high,num):
    mid = (low+high)/2
    print('Value of mid is...', int(mid))
    if(int(mid)==low & int(mid)==high):
        return ('Number was not found')
    elif(arr[int(mid)]==num):
        print('Number Found! Position: ', mid+1)
    elif (arr[int(mid)] > num):
        high = int(mid)-1
        binary(low,int(mid)-1,num)        
    else:
        low = int(mid)+1
        binary(int(mid)+1,high,num)
        

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
low = 0
high = len(arr)-1

print('enter the number to be search... \n')
num = input()
print('Number Entered is', num)

print('low is', num, ' and high is' ,high)
binary(low,high,int(num))





