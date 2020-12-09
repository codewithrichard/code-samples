from typing import List
"""
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses
substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:

Input: s = ""
Output: 0

 
Constraints:

    0 <= s.length <= 3 * 104
    s[i] is '(', or ')'.

subproblems:
1) Which parentheses are valid? (matching)
left to right traversal
case "(": Don't know if part of matching pair
          must traverse remainder of string to know
case ")": immediately know if this is part of pair
          Would match a previous open paren

Strategy
Step 1: Identify which parens are part of matching pair
Step 2: Count longest group of matching parens

Examples:
Input   "(()())"
matching:TTTTTT

Input   "())(())("
matching:TTFTTTTF

left to right traversal
- Use stack to track open unmatched parens
- This stack will contain the index of the open paren
  in the original string
  This allows marking the corresponding position in
  matching to True when the open paren is found to be
  a match
- push all open parens' index to stack
- pop matched open parens off stack

matching FFFFFFFF
INPUT:  "())(())("
index=0  ^
stack = []
logic: open, push index onto stack

matching FFFFFFFF
INPUT:  "())(())("
index=1   ^
stack = [0]
logic: closed paren
        matches! pop off stack, mark matching parens

matching TTFFFFFF
INPUT:  "())(())("
index=2    ^
stack = []
logic: closed paren, no match (do nothing)

matching TTFFFFFF
INPUT:  "())(())("
index=3     ^
stack = []
logic: open, push index onto stack

matching TTFFFFFF
INPUT:  "())(())("
index=4      ^
stack = [3]
logic: open, push index onto stack

matching TTFFFFFF
INPUT:  "())(())("
index=5       ^
stack = [3, 4]
logic: closed, matches!
        pop matching open paren off stack
        marking matching parens in matching

matching TTFFTTFF
INPUT:  "())(())("
index=6        ^
stack = [3]
logic: closed, matches!
        pop matching open paren off stack
        marking matching parens in matching

matching TTFTTTTF
INPUT:  "())(())("
index=7         ^
stack = []
logic: open, push index onto stack

DONE

Step 2: find longest group of T in matching
TTFTTTTF

output = 4
"""
class Solution:

    def longestValidParentheses(self, s: str) -> int:
        
        # initialize to all false
        matching: List[bool] = []
        for i in range(0, len(s)):
            matching.append(False)

        # stack of index of open parens
        open_paren_stack: List[int] = []

        # left to right traversal
        for i in range(0, len(s)):
            if s[i] == "(":
                # add open paren's index to stack
                open_paren_stack.append(i)
            else:
                # closing paren
                if len(open_paren_stack) > 0:
                    # there's an unmatched open paren
                    # Found a match

                    # mark indexes of both open/closed paren
                    # mark open paren
                    matching[open_paren_stack[-1]] = True

                    # mark closed paren
                    matching[i] = True

                    #pop open paren from stack
                    del open_paren_stack[-1]
                
                else:
                    # There is no open paren
                    # this closing paren is unmatched
                    matching[i] = False # no-op

        # Count longest sequential matched parens
        # longest sequence of Trues in matching
        max_longest = 0
        longest_so_far = 0 
        for i in range(0, len(matching)):
            if (matching[i]):
                #found a matching paren
                longest_so_far += 1
                if longest_so_far > max_longest:
                    max_longest = longest_so_far
            else:
                # unmatched paren, reset counters
                longest_so_far = 0

        return max_longest   

