# -*-coding:utf-8 -*-
# @Time: 2023/3/26 19:38
# @Author: doubibani
# @File: tmp
# @Software: PyCharm
# TO DO:


## =========== T1 ===========




#
#
# ## =========== T2 ===========
# import math
#
# T = int(input())
# while T:
#     T -= 1
#     a, b = map(int, input().split())
#     N = 500
#     delta_x = (b-a)/N
#     xi = list(a + delta_x * i for i in range(N+1))
#     prob = 0
#     for i in range(N):
#         prob += math.sin(math.sqrt(xi[i]))
#     prob = prob * delta_x / 5.68
#     if prob > 0.5:
#         print(1)
#     else:
#         print(0)
#
#
#
#
# ## =========== T3 ===========
# T = int(input())
#
# while T:
#     T -= 1
#     k, t = map(float, input().split())
#     k = int(k)
#     sigma = list(map(float, input().split()))
#     det = 1
#     for i in range(k):
#         det *= sigma[i]
#     tr = sum(sigma)
#     d_KL = (math.log(1/det) - k + tr)/2
#     if d_KL > t:
#         print(1)
#     else:
#         print(0)
#
#
#
#
# ## =========== T4 ===========
# from collections import Counter
#
# n, k = map(int, input().split())
# nums = list(map(int, input().split()))
# res = 0
# if k == 1:
#     print(n)
# else:
#     cnt = Counter()
#     for j in range(k, n):
#         s = sorted(nums[j-k:j])
#         if all(s[i+1] - s[i] == 1 for i in range(k-1)):
#             res += 1
#     print(res)






## =========== T5 ===========
H, W = map(int, input().split())
m = int(input())
pos = 0
neg = 0
pos_vis = set()
neg_vis = set()
res = 1
cut = list()

def get_k(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    b = y2 - k * x2
    c = (H - y2) / k + x2
    if k > 0:
        return 1, b, c
    else:
        return -1, b, c

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    k, b, c = get_k(x1, y1, x2, y2)
    if k == 1:
        if b not in pos_vis and -W < b < H:
            if not cut:
                res += 1
            else:
                if c >= cut[-1] or c <= cut[0]:
                    res += 1
                else:
                    res += 2
            cut.append(c)
            cut.sort()
        pos_vis.add(b)
    else:
        if b not in neg_vis and 0 < b < W + H:
            if not cut:
                res += 1
            else:
                if c >= cut[-1] or c <= cut[0]:
                    res += 1
                else:
                    res += 2
                cut.append(c)
                cut.sort()
            neg_vis.add(b)

print(res)
