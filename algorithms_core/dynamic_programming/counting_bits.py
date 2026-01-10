"""
Problem: Counting Bits
Return array where ans[i] = number of 1s in binary of i.
Pattern: DP - ans[i] = ans[i >> 1] + (i & 1), or ans[i] = ans[i & (i-1)] + 1.
Link: https://leetcode.com/problems/counting-bits/
"""

# TODO: Implement your solution here
