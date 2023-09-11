# -*-coding:utf-8 -*-
# @Time: 2023/3/26 15:28
# @Author: doubibani
# @File: Ali0322
# @Software: PyCharm
# TO DO:

## ============= T1 =============
# 给定两个长度为 n 的数组 a 和 b，你需要对 a 数组进行重排，
# 使得 a 与 b 对应位置上的元素的绝对值之差之和最小。请你输出一个最优解。

n = int(input().strip())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pairs = [[v, i] for i, v in enumerate(b)]
a.sort()
pairs.sort()
for i in range(n):
    idx = pairs[i][1]
    b[idx] = a[i]
print(*b, sep=' ')

## ============= T2 =============


if __name__ == '__main__':
    print('')
