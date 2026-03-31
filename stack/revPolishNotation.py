""" class Solution:
    def __init__(self):
        self.stack = []
        self.result = 0
    
    def push(self,val:int) -> None:
        return self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def evalRPN(self, tokens: List[str]) -> int:
        hashMap = {
        '+':lambda a,b : a+b,
        '-':lambda a,b : a-b,
        '/': lambda a,b : int(a/b),
        '*': lambda a,b : int(a*b)
        }

        for token in tokens:
            if token not in hashMap:
                self.push(int(token))
            else:
                b = self.pop()
                a = self.pop()
                self.result = hashMap[token](a,b)
                self.push(self.result)
        return self.pop() """

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = {
            '+': lambda a,b: a+b,
            '-': lambda a,b: a-b,
            '*': lambda a,b: a*b,
            '/': lambda a,b: int(a/b)
        }

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[token](a,b))

        return stack[-1]
                

        