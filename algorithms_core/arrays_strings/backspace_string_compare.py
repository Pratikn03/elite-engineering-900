"""
LeetCode 844. Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/

Goal:
Given two strings s and t, where '#' means backspace,
return True if they are equal after applying the backspaces.

Human explanation:
Instead of building the final strings (which needs extra memory),
we can walk from the END of each string.

Why from the end?
A backspace deletes a character BEFORE it.
If we go right-to-left, we can keep a counter of how many characters
should be skipped (deleted) and jump over them.

Algorithm:
- i points to end of s, j points to end of t
- skip_s counts how many chars to skip in s due to backspaces
- skip_t counts how many chars to skip in t due to backspaces
- Find the next "real" character in each string and compare them.
If any mismatch -> False. If we finish -> True.

Time:  O(n) where n = len(s) + len(t)
Space: O(1)
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1

        skip_s = 0
        skip_t = 0

        # Continue until both strings are fully processed
        while i >= 0 or j >= 0:

            # Move i to the next valid character in s
            while i >= 0:
                if s[i] == "#":
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    # This character is deleted by a previous '#'
                    skip_s -= 1
                    i -= 1
                else:
                    break

            # Move j to the next valid character in t
            while j >= 0:
                if t[j] == "#":
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break

            # Compare current valid characters
            ch_s = s[i] if i >= 0 else None
            ch_t = t[j] if j >= 0 else None

            if ch_s != ch_t:
                return False

            # Move left after comparison
            i -= 1
            j -= 1

        return True


if __name__ == "__main__":
    sol = Solution()

    # Provided-style examples
    assert sol.backspaceCompare("ab#c", "ad#c") is True  # "ac" == "ac"
    assert sol.backspaceCompare("ab##", "c#d#") is True  # "" == ""
    assert sol.backspaceCompare("a#c", "b") is False     # "c" != "b"

    # Extra checks
    assert sol.backspaceCompare("a##c", "#a#c") is True  # "c" == "c"
    assert sol.backspaceCompare("####", "") is True      # "" == ""

    print("All tests passed ✅")
