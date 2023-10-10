# 给你一个非负整数数组 nums 和一个整数 target 。 
# 
#  向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ： 
# 
#  
#  例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。 
#  
# 
#  返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1], target = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 20 
#  0 <= nums[i] <= 1000 
#  0 <= sum(nums[i]) <= 1000 
#  -1000 <= target <= 1000 
#  
# 
#  Related Topics 数组 动态规划 回溯 👍 1762 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTargetSumWays(self, nums: List[int], t: int) -> int:
        # p - (s - p) = t
        # 2 * p = t + s
        t += sum(nums)
        if t < 0 or t % 2:
            return 0
        t //= 2

        n = len(nums)

        cache = [[-1] * (t+1) for _ in range(n)]

        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            if cache[i][c] != -1:
                return cache[i][c]
            res = 0
            res += dfs(i-1, c)
            if c >= nums[i]:
                res += dfs(i-1, c-nums[i])
            cache[i][c] = res
            return res

        return dfs(n-1, t)

# leetcode submit region end(Prohibit modification and deletion)
