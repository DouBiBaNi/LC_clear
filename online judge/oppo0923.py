# -*-coding:utf-8 -*-
# @Time: 2023/9/23 13:38
# @Author: doubibani
# @File: oppo0923
# @Software: PyCharm
# TO DO:
import collections

# 1.
n, x = map(int, input().split())

res = 0
for _ in range(n):
    m, v = map(int, input().split())
    if x >= m:
        x -= m
        res += v

print(res)

# 2.
s = input().strip()
k = int(input())

n = len(s)
if n <= k:
    print('a'*(k-n)+s[::-1])

left = s[:n-k]
right = s[-(n-k):]

if left == left[::-1]:
    print(s[n-k:][::-1])
elif right == right[::-1]:
    print(s[:-(n-k)][::-1])
else:
    print(-1)


# 3.
class UnionFind:
    '''quickly find'''
    def __init__(self, n, rt=None):
        self.n = n
        self.root = [i for i in range(n)] if not rt else rt

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        for i in range(n):
            if self.root[i] == rooty:
                self.root[i] = rootx

    def is_connect(self, x, y):
        return self.find(x) == self.find(y)


n, m = map(int, input().split())
capied = set()
uncapied = set()

s = input().strip()
for i in range(n):
    if s[i] == '1':
        capied.add(i)
    else:
        uncapied.add(i)

g = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

uf = UnionFind(n)
for u in capied:
    for v in g[u]:
        if v in capied:
            uf.union(u, v)

res = 0
idx = n
for u in uncapied:
    uf_copy = UnionFind(n, rt=uf.root)
    for v in g[u]:
        if v in capied:
            uf_copy.union(u, v)
    city = collections.defaultdict(list)
    for i in range(n):
        if i == u or i in capied:
            city[uf_copy.root[i]].append(i)
    tmp = 0
    for v in city.values():
        k = len(v)
        if k >= 2:
            tmp += k * (k-1) // 2
    if tmp > res:
        res = tmp
        idx = u
    elif tmp == res:
        idx = min(idx, u)

print(" ".join([idx, res]))




if __name__ == '__main__':
    print('')
