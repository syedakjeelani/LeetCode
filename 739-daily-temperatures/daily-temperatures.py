class Solution(object):
    def dailyTemperatures(self, temperatures):
        answers = [0] * len(temperatures)
        stack = [] #we save [index, temperature]
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                answers[stack_index] = (index - stack_index)
            stack.append([temp, index])
        return answers
        