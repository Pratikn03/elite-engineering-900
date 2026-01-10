"""
Problem: Decode Ways
Count ways to decode digit string to letters (1=A, 26=Z).
Pattern: DP - dp[i] = dp[i-1] (if valid single) + dp[i-2] (if valid double).
Link: https://leetcode.com/problems/decode-ways/
"""

# TODO: Implement your solution here
