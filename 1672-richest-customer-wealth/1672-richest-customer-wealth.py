class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth_sum = []

        for i in accounts:
            wealth_sum.append(sum(i))

        return max(wealth_sum)