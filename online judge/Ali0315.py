# -*-coding:utf-8 -*-
# @Time: 2023/3/22 14:04
# @Author: doubibani
# @File: Ali0315
# @Software: PyCharm
# TO DO:

## ============= T1 =============
# 给一个长度为 n 数组, 数字m，x。
# 给一个操作，指定m个数字加x, n-m个数字乘x, 求一次操作后数组之和的最大值

m, x = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
ans = sum(nums[:m]) + m * x + sum(nums[m:]) * x
print(ans)

## ============= T2 =============
# 给一个数字n，求x，y 。x^y = n(异或) 且 |x-y| 最小

n = int(input())

x = y = 0
while n:
    if n & (n-1) == 0:
        y = n
    else:
        x += n & (-n)
    n -= n & (-n)
print(y, x)

## ============= T3 =============
# 给一个二维矩阵，可以从任意一点出发走k步，
# 然后把这个 k 范围内的所有值加起来，问最大值是多少

