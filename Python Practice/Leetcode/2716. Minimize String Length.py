
"""
Given a string s, you have two types of operation:

Choose an index i in the string, and let c be the character in position i.
    Delete the closest occurrence of c to the left of i (if exists).

Choose an index i in the string, and let c be the character in position i.
    Delete the closest occurrence of c to the right of i (if exists).

Your task is to minimize the length of s by performing the above operations zero or more times.

Return an integer denoting the length of the minimized string.



Example 1:
Input: s = "aaabc"
Output: 3
Explanation:
Operation 2: we choose i = 1 so c is 'a', then we remove s[2] as it is closest 'a' character to the right of s[1].
s becomes "aabc" after this.
Operation 1: we choose i = 1 so c is 'a', then we remove s[0] as it is closest 'a' character to the left of s[1].
s becomes "abc" after this.

Example 2:
Input: s = "cbbd"
Output: 3
Explanation:
Operation 1: we choose i = 2 so c is 'b', then we remove s[1] as it is closest 'b' character to the left of s[1].
s becomes "cbd" after this.
"""


def minimizedStringLength(s: str) -> int:
    pass












