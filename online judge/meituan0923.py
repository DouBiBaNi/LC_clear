# -*-coding:utf-8 -*-
# @Time: 2023/9/23 09:27
# @Author: doubibani
# @File: meituan0923
# @Software: PyCharm
# TO DO:
import collections

# 1.

n = int(input())
nums = list(map(int, input().split()))

hi = lo = nums[0]
res = 0

for num in nums[1:]:
    if num > hi:
        hi = num
        res += 1
    elif num < lo:
        lo = num
        res += 1

print(res)

# 2.

day = 24 * 60

h, m = map(int, input().strip().split(':'))
time = h * 60 + m
n = int(input())
for _ in range(n):
    ch, delta = input().split()
    op = 1 if ch == '+' else -1
    time = (time + op * int(delta)) % day

h, m = time // 60, time % 60
res = ''
if h < 10:
    res += '0'
res += str(h) + ':'
if m < 10:
    res += '0'
res += str(m)
print(res)


# 3.
mod = int(1e9+7)

n = int(input())
res = 0

def countk(n):
    k = 1
    while k * k +k <= 2 * n:
        k += 1
    return k-1

k = countk(n)
delta = n - k * (k+1) // 2
res = (k * (k+1) * (2*k+1)//6 + k*(k+1)//2)//2


res += delta * (2*(k+1)-delta+1)//2
res %= mod
print(res)

# 4.
n, q = map(int, input().split())
nums = list(map(int, input().split()))

def primeFactor(num):
    """分解质因数"""
    s = set()
    i = 2
    while i * i <= num:
        while num % i == 0:
            s.add(i)
            num //= i
        i += 1
    if num > 1:
        s.add(num)
    return s

def helper(num):
    for y in primeFactor(num):
        while num % (y * y) == 0:
            num //= y * y
    return primeFactor(num)

mp = collections.defaultdict(set)
for i in range(n):
    mp[i].add(helper(nums[i]))

for _ in range(q):
    l, r, x = map(int, input().split())
    for i in range(l-1, r):
        if not all(p in mp[i] for p in helper(x)):
            print(nums[i])
            break
    else:
        print(-1)






if __name__ == '__main__':
    print('')
