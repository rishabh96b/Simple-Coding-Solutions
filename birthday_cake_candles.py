'''
@Author: Rishabh(rishabhbohra10@gmail.com)
Problem Link: https://www.hackerrank.com/challenges/birthday-cake-candles
language: Python2
'''
#import collections module in python
import collections

def birthdayCakeCandles(n, ar):
    #count candles and how many of same height are present 
    cnt = collections.Counter(ar)
    
    max = -100000
    
    #find the max number of candles present.
    for i in cnt:
        if(max < cnt[i]):
            max = cnt[i]
    return max

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
