class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            stack.append(ch)
            # print("b4 process: ", stack)
            process(stack)
            # print("after process: ", stack)
        return (len(stack) == 0)
            
def process(stack):
    def isPair(s):
        return (s == ['(',')'] or s == ['[',']'] or s== ['{','}'])
    if isPair(stack[-2:]):
        del stack[-2:]
        process(stack)
