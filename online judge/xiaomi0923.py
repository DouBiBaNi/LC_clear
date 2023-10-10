# -*-coding:utf-8 -*-
# @Time: 2023/9/23 15:45
# @Author: doubibani
# @File: xiaomi0923
# @Software: PyCharm
# TO DO:

# # 1.
n = int(input())

s = set()
for _ in range(n):
    num = int(input())
    s.add(num)

print(len(s))

# 2.
s = input().strip()

n = len(s)

if n == 1:
    print(1)
else:
    pre = cur = 1
    for i in range(2, n+1):
        if '10' <= s[i-2:i] <= '26':
            pre, cur = cur, pre + cur
        else:
            pre, cur = cur, cur
    print(cur)


if __name__ == '__main__':
    print('')
