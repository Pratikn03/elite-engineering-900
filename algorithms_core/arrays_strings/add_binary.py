"""67. Add Binary
Easy
Topics
premium lock icon
Companies
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
"""
67. Add Binary
https://leetcode.com/problems/add-binary/

Problem:
Given two binary strings a and b, return their sum as a binary string.

Key observation:
Binary addition works exactly like normal addition, but with base 2.
You add from the rightmost bit (least significant) to the leftmost,
and you keep a carry (0 or 1).

Example:
a =  "1010"
b =  "1011"
       1010
     + 1011
     -------
      10101

Rules per column:
total = bit_a + bit_b + carry
result_bit = total % 2
carry      = total // 2

Complexity:
- Time:  O(n) where n = max(len(a), len(b))
- Space: O(n) for the output string (required)

Constraints note:
length up to 1e4, so O(n) is perfect.
"""
from typing import List
class Solution:
    def addBinary(self, a:str, b:str) -> str:
        i = len(a)-1
        j= len(b)-1
        carry = 0
        # we will build answer fromm right -> left,then reverse at the end.
        out: List[str]=[]
        while i>=0 or j>-0 or carry:
            #If one string is shorter, treat missing bits as 0
            bits_a=1 if(i>=0 and a[i]=='1') else 0
            bits_b=1 if(j>=0 and b[j]=='1') else 0
            total=bits_a+bits_b+carry
            #total can be 0,1,2,3. The resulting bit is total % 2.
            out.append('1' if total % 2==1 else'0')
            #carry is 1 only when total >=2.
            carry=1 if total >=2 else 0
            i-=1
            j-=1
        #reverse the output list and join to form the final string.
        out.reverse()
        return ''.join(out)
if __name__ == "__main__":
    s= Solution()
    assert s.addBinary("11","1")=="100"
    assert s.addBinary("1010","1011")=="10101"     
    assert s.addBinary("0","0")=="0"     
    assert s.addBinary("1","0")=="1"

    print("All tests passed.")


