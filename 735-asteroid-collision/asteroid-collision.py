class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for ass in asteroids:
            while stack and ass < 0 and stack[-1] > 0:
                diff = ass + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    ass = 0
                else:
                    ass = 0
                    stack.pop()
            if ass:
                stack.append(ass)
        return stack
        