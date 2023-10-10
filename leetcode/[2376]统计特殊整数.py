# 如果一个正整数每一个数位都是 互不相同 的，我们称它是 特殊整数 。 
# 
#  给你一个 正 整数 n ，请你返回区间 [1, n] 之间特殊整数的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 20
# 输出：19
# 解释：1 到 20 之间所有整数除了 11 以外都是特殊整数。所以总共有 19 个特殊整数。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 5
# 输出：5
# 解释：1 到 5 所有整数都是特殊整数。
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 135
# 输出：110
# 解释：从 1 到 135 总共有 110 个整数是特殊整数。
# 不特殊的部分数字为：22 ，114 和 131 。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2 * 10⁹ 
#  
# 
#  Related Topics 数学 动态规划 👍 68 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from functools import cache

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        # 数位dp，dfs(i, mask, is_limit, is_num)
        s = str(n)

        @cache
        def dfs(i, mask, is_limit, is_num):
            if i == len(s):
                return int(is_num)
            res = 0
            if not is_num:
                res += dfs(i+1, mask, False, is_num)
            top = int(s[i]) if is_limit else 9
            for d in range(1-int(is_num), top+1):
                if (mask >> d) & 1 == 0:
                    res += dfs(i+1, mask | (1 << d), is_limit and d == top, True)
            return res

        return dfs(0, 0, True, False)

# leetcode submit region end(Prohibit modification and deletion)
