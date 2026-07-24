class Solution(object):
    def simplifyPath(self, path):
        stack = []
        paths = path.split("/")
        for current in paths:
            if current == "..":
                if stack:
                    stack.pop()
            elif current != "" and current != ".":
                stack.append(current)
        return "/" + "/".join(stack)
        