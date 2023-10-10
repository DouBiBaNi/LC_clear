# -*-coding:utf-8 -*-
# @Time: 2023/9/23 09:15
# @Author: doubibani
# @File: UnionFind
# @Software: PyCharm
# TO DO:

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.root = [i for i in range(n)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        root_x = self.root[x]
        root_y = self.root[y]
        for i in range(self.n):
            if self.root[i] == root_y:
                self.root[i] = root_x

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

if __name__ == '__main__':
    print('')
