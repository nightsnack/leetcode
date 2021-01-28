class Solution:
    def simplifyPath(self, path: str) -> str:
        pathlist = path.split('/')
        stack = []
        for p in pathlist:
            if p in ['', '.']:
                continue
            elif p == '..' and not stack:
                continue
            elif p == '..' and stack:
                stack.pop()
            else:
                stack.append(p)
        return '/'+'/'.join(stack)

s = Solution()
path = "/a/./b/../../c/"
print(s.simplifyPath(path))
exit(0)