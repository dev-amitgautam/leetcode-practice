class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def createString(st):
            stack = []

            for i in st:
                if i == '#':
                    if len(stack):
                        stack.pop()
                else:
                    stack.append(i)
                
            return ''.join(stack)

        return createString(s) == createString(t)


        