# -*-coding:utf-8 -*-
# @Time: 2023/9/23 09:20
# @Author: doubibani
# @File: BIT
# @Software: PyCharm
# TO DO:

class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n+1)

    @staticmethod
    def lowbit(x):
        return x & (-x)

    def query(self, x):
        ret = 0
        while x > 0:
            ret += self.tree[x]
            x -= BIT.lowbit(x)

        return ret

    def update(self, x, t):
        while x < self.n:
            self.tree[x] += t
            x += BIT.lowbit(x)

if __name__ == '__main__':
    print('')
