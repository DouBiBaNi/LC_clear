# -*-coding:utf-8 -*-
# @Time: 2023/3/19 14:00
# @Author: doubibani
# @File: main
# @Software: PyCharm
# TO DO:
import math
import bisect
from collections import Counter
from collections import deque
from collections import defaultdict
from functools import cache
from typing import List, Deque


class Solution:
    def main(self):
        temperatureA = [21, 18, 18, 18, 31]
        temperatureB = [34, 32, 16, 16, 17]
        print(self.temperatureTrend(temperatureA, temperatureB))

    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        n = len(temperatureA)
        for i in range(n - 1):
            if temperatureA[i] > temperatureA[i + 1]:
                temperatureA[i] = -1
            elif temperatureA[i] == temperatureA[i + 1]:
                temperatureA[i] = 0
            else:
                temperatureA[i] = 1
            if temperatureB[i] > temperatureB[i + 1]:
                temperatureB[i] = -1
            elif temperatureB[i] == temperatureB[i + 1]:
                temperatureB[i] = 0
            else:
                temperatureB[i] = 1
        i = j = ans = 0
        while j < n - 1:
            while j < n - 1 and temperatureA[i] == temperatureB[i]:
                j += 1
            ans = max(ans, j - i)
            while j < n - 1 and temperatureA[i] != temperatureB[i]:
                j += 1
            i = j
        return ans

    @cache
    def dfs(self, i, j):
        pass

if __name__ == '__main__':
    Solution().main()
