
"""

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.


Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false


"""


def rotateString(s: str, goal: str) -> bool:

    for n in range(0,len(s)):
        s = s[1:] + s[0]
        if s == goal:
            return True
    return False

print(rotateString(s = "abcde", goal = "cdeab"))
#True

