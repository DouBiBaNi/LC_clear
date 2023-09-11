# -*-coding:utf-8 -*-
# @Time: 2023/3/20 00:00
# @Author: doubibani
# @File: meituan
# @Software: PyCharm
# TO DO:
from collections import Counter

# REFERENCE: https://leetcode.cn/circle/discuss/wSvfXt/
## ============= T1 =============
# 小美在玩一项游戏。该游戏的目标是尽可能抓获敌人。
# 敌人的位置将被一个二维坐标 (x, y) 所描述。
# 小美有一个全屏技能，该技能能一次性将若干敌人一次性捕获。
# 捕获的敌人之间的横坐标的最大差值不能大于 A，
# 纵坐标的最大差值不能大于 B
# 现在给出所有敌人的坐标，你的任务是计算小美一次性最多能使用技能捕获多少敌人。
#
# input: N, A, B 表示敌人数量，全屏技能参数A，B
# output：单次可捕获敌人的最多数量

n, a, b = map(int, input().split())
mp = [[0] * 1001 for _ in range(1001)] # 坐标不超过1000
for i in range(n):
    x, y = map(int, input().split())
    mp[x][y] += 1
# 二维前缀和初始化
for i in range(1, 1001):
    for j in range(1, 1001):
        mp[i][j] += mp[i-1][j] + mp[i][j-1] - mp[i-1][j-1]
ans = 0
# 枚举右下端点
for i in range(a + 1, 1001):
    for j in range(b+1, 1001):
        t = mp[i][j] - mp[i-a-1][j] - mp[i][j-b-1] + mp[i-a-1][j-b-1]
        ans = max(ans, t)
print(ans)

## ============= T2 =============
# 小美现在有一串彩带，假定每一厘米的彩带上都是一种色彩
# 因为任务的需要，小美希望从彩带上截取一段，使得彩带中的颜色数量不超过K种。
# 显然，这样的截取方法可能非常多。于是小美决定尽量长地截取一段你的任务是帮助
# 小美截取尽量长的一段，使得这段彩带上不同的色彩数量不超过K种。
#
# input: 第一行两个整数 N,K，以空格分开，分别表示彩带有N厘米长，
# 你截取的一段连续的彩带不能超过K种颜色。接下来一行
# N个整数，每个整数表示一种色彩，相同的整数表示相同的颜色
#
# output：一行，一个整数，表示选取的彩带最大长度
def solutionForT2():
    n, k = map(int, input().split())
    nums = list(input().split())

    res = i = 0
    cnt = Counter()
    for j in range(n):
        cnt[nums[j]] += 1
        while len(cnt) > k:
            cnt[nums[i]] -= 1
            if cnt[nums[i]] == 0:
                del cnt[nums[i]]
            i += 1
        res = max(res, j - i + 1)
    print(res)

solutionForT2()

## ============= T3 =============
# 现在小美获得了一个字符串。小美想要使得这个字符串是回文串。
# 小美找到了你。你可以将字符串中至多两个位置故为任意小写英文字符 'a' - 'z'
# 你的任务是帮助小美在当前制约下，获得字典序最小的回文字符串，数据保证能在题目限制下形成回文字符串。
#

s = list(input())
n = len(s)
cnt = 0
for i in range(n // 2):
    if s[i] != s[n - i - 1]:
        cnt += 1
if cnt == 0:
    for i in range (n):
        if s[i] != 'a':
            s[i] = 'a'
            s[n - i - 1] = 'a'
            break
elif cnt == 1:
    for i in range (n):
        if s[i] != s[n - i - 1]:
            if s[i] == 'a' or s[n - i - 1] == 'a':
                if n % 2 == 1:
                    s[n // 2] = 'a'
            s[i] = 'a'
            s[n - i - 1] = 'a'
else:
    for i in range (n):
        if s[i] != s[n - i - 1]:
            s[i] = min(s[i] , s[n - i - 1])
            s[n - i - 1] = s[i]
print ("".join(s))


## ============= T4 =============
# 在商店里有N个物品，每个物品有原价和折扣价小美相要购买商品。
# 小美拥有X元，一共Y张折扣券。
# 小美需要最大化购买商品的数量，并在所购商品数量尽量多的前提下，尽置减少花费。
# 你的任务是帮助小美求出最优情况下的商品购买数量和花费的钱数。

n, x, y = map(int, input().split())
dp = [[0] * (y + 1) for _ in range(x+1)]
for i in range(n):
    cur, disc = map(int, input().split())
    for j in range(x, -1, -1):
        for k in range(0, y+1):
            if j >= cur:
                dp[j][k] = max(dp[j][k], dp[j-cur][k] + 1)
            if k and j >= disc:
                dp[j][k] = max(dp[j][k], dp[j-disc][k-1] + 1)

mx = dp[x][y]
for j in range(x + 1):
    for k in range(y+1):
        if dp[j][k] == mx:
            print(mx, j)
            break
    else:
        continue
    break
