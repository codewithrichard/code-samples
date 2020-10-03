from typing import List
"""

LeetCode #20 Valid Parentheses (Easy)

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.


    Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([)]"
Output: false

Example 5:

Input: s = "{[]}"
Output: true

 

Constraints:

    1 <= s.length <= 10**4
    s consists of parentheses only '()[]{}'.


s, stack
return True when both s and stack are empty
always add open paren to stack
closing paren must match top open paren on stack

s, stack
"()"    []      # always add open paren to stack
")"     ["("]   # closing paren must match top open paren on stack
""      []      # return True


"({})"  []          # always add open paren to stack
"{})"   ["("]       # always add open paren to stack
"})"    ["(", "{"]  # closing paren must match top open paren on stack
")"     ["("]       # closing paren must match top open paren on stack
""      []          # True


"()["   []          # always add open paren to stack
")["    ["("]       # closing paren must match top open paren on stack
"["     []          # always add open paren to stack
""      ["["]       # False



return True when both s and stack are empty
always add open paren to stack
closing paren must match top open paren on stack
"""

class Solution:
    def __init__(self):
        self.open_parens = {"(": True, "{": True, "[": True}
        self.matched_parens = {"()": True, "{}": True, "[]": True}

    def isValid(self, s: str) -> bool:
        return self.isValidRecursive(s, [])

    def isValidRecursive(self, s: str, stack: List[str]) -> bool:
        
        # return True when both s and stack are empty
        if not s:
            # s is empty
            return len(stack) == 0
        else:
            # There exists at least one paren to process
            next_paren = s[0]   # open? ({[
            
            # is open or closed?
            if next_paren in self.open_parens:
                # always add open paren to stack and recurse
                return self.isValidRecursive(s[1:], stack + [next_paren])

            else: 
                # closed
                # closing paren must match top open paren on stack
                # is there an item on the stack?
                if not stack:
                    # no open parens on stack, but next_paren is closed
                    return False
                else:
                    latest_open_paren = stack[-1]
                    # do next_paren and latest_open_paren match "()", "{}", "[]"
                    potential_matched_parens = latest_open_paren + next_paren
                    if (potential_matched_parens in self.matched_parens):
                        # they match! and recurse
                        return self.isValidRecursive(s[1:], stack[0:-1])
                    else:
                        return False





