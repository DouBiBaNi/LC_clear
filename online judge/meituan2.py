# -*-coding:utf-8 -*-
# @Time: 2023/3/20 16:39
# @Author: doubibani
# @File: tmp
# @Software: PyCharm
# TO DO:

## ============= T1 =============
# 数火车，其实就是一个栈，给一个入栈顺序，一个出栈顺序，问你这种情况是不是可能的
T = int(input())

while T:
    T -= 1
    n = int(input())
    stack_in = list(map(int, input().split()))
    stack_out = list(map(int, input().split()))
    stack = []
    j = 0
    for car in stack_in:
        stack.append(car)
        while stack and stack[-1] == stack_out[j]:
            stack.pop()
            j += 1
    if len(stack) == 0:
        print('Yes')
    else:
        print('No')


## ============= T2 =============
# 给出一列数，从中选取若干个，要求所选的任意两个数字的位置至少隔开2个位置，
# 也就是选取了i的话，i-2，i-1，i+1， i+2都不能选。
#
n = int(input())
candy = list(map(int, input().split()))
if n <= 3:
    print(max(candy))
else:
    dp = [0] * n
    for i in range(3):
        dp[i] = max(candy[:i+1])
    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2], dp[i-3] + candy[i])
    print(dp[-1])


## ============= T3 =============
# 给出一堆巧克力的边长，巧克力的重量是边长的平方。
# 给出若干个询问q，问在重量不超过q的前提下，最多能选多少块巧克力。

from itertools import accumulate
from bisect import bisect_right

n, m = map(int, input().split())
nums = list(map(int, input().split()))
bags = list(map(int, input().split()))

nums = [num ** 2 for num in nums]
nums.sort()
nums = list(accumulate(nums))
print(nums)
for i in range(m):
    bags[i] = bisect_right(nums, bags[i])
# print(bags) 得逐个输出
for i in range(n):
    print(bags[i], end=' ')



## ============= T4 =============
# 给出一串字符串，形如“key1=val1;key2=val2;key3=val;”，
# 然后给出q个询问，每个询问是一个字符串s，如果s有对应的key，则输出对应的value，如果有多个key对应，
# 则按照最后出现的那一组key value来输出，如果没有对应的则输出“EMPTY”。

from collections import defaultdict

mp = defaultdict(list)
s = input()
if s[-1] == ';':
    s = s[:-1]
s = list(s.split(';'))

for i in range(len(s)):
    k, v = s[i].split('=')
    mp[k].append(v)

q = int(input())
while q:
    q -= 1
    a = input().split() # 得去末端的空格或换行
    if a not in mp:
        print('EMPTY')
    else:
        print(mp[a][-1])


