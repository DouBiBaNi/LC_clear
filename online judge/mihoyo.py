# -*-coding:utf-8 -*-
# @Time: 2023/3/19 23:22
# @Author: doubibani
# @File: mihoyo
# @Software: PyCharm
# TO DO:

# REFERENCE: https://leetcode.cn/circle/discuss/Hg8TsQ/

## ============= T1 =============
# 对一个仅含小写字母的字符串s选择相邻位置的字符交换，返回字典序最大的那个
def solutionForT1():
    s = list(input())

    def swap(s):
        n = len(s)
        if n == 1:
            return s
        isSwap = False
        for i in range(n - 1):
            if s[i] < s[i + 1]:
                s[i], s[i + 1] = s[i + 1], s[i]
                isSwap = True
        if not isSwap:
            s[-1], s[-2] = s[-2], s[-1]
        return s

    s = swap(s)
    print("".join(s))


solutionForT1()


## ============= T2 =============
# 输入n，构造长为n的整数数列满足3个要求：
# 1. 每个数绝对值不大于3；
# 2. 相邻数的积小于0，和不等于0；
# 3. 整个数列和为0
def solutionForT2():
    n = int(input())

    def generate(n):
        """多组答案都能满足，随便返回一组即可"""
        lst = []
        tmp = [2, -1, 2, -3]  # 根据示例构造的
        mod1 = [2, -3, 2, -3, 2]
        mod2 = [1, -2, 1, -2, 3, -1]
        mod3 = [1, -2, 1]
        if n % 4 == 0:
            lst = tmp * (n // 4)
        elif n % 4 == 1:
            lst = tmp * (n // 4 - 1) + mod1
        elif n % 4 == 2:
            lst = tmp * (n // 4 - 1) + mod2
        elif n % 4 == 3:
            lst = tmp * (n // 4 - 1) + mod3
        return lst

    print(generate(n))


solutionForT2()


## ============= T3 =============
# 有一无穷长字符串s：1,2,3;4,5,6;7,8,9;10,11,12;13。。。
# 每个数字后面为逗号或分号，每三个数字后面一个分号，其余为逗号。
# 输入两个数字l,r 求s[l:r]之间的逗号分号数量
def solutionForT3():
    t = int(input())  # the number of queries

    # t <= 10**5，1<= l, r <= 10**9, simulate will be TLE
    def getNumbers(l, r):
        """
        一数字： 2 * 9 个字符； 两数字： 3 * 90 个字符； n位数：（n+1)*9*10**(n-1))
        :param l: 第l个字符：int
        :param r: 第r个字符：int
        :return: 逗号个数：int； 分号个数： int
        """
        # 可以二分做？
        # link: https://leetcode.cn/circle/discuss/RRskhE/
        d = f = 0
        pass
        return d, f

    while t:
        t -= 1
        l, r = map(int, input().split())
        print(getNumbers(l, r))


solutionForT3()
