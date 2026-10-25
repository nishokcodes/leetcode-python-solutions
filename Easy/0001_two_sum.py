"""LeetCode #1: Two Sum.

Problem: https://leetcode.com/problems/two-sum/
Time: O(n) | Space: O(n)
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}

        for index, number in enumerate(nums):
            complement = target - number
            if complement in seen:
                return [seen[complement], index]
            seen[number] = index

        # LeetCode guarantees exactly one valid answer.
        raise ValueError("No two numbers add up to target")
