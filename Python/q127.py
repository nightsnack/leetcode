import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        L = len(beginWord)
        if endWord not in wordList:
            return 0

        all_combo_dict = collections.defaultdict(list)

        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i]+'*'+word[i+1:L]].append(word)

        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord:True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                pat = current_word[:i]+'*'+current_word[i+1:]
                for word in all_combo_dict[pat]:
                    if word == endWord:
                        return level+1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word,level+1))
                all_combo_dict[pat] = []
        return 0

s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(s.ladderLength(beginWord, endWord, wordList))
exit(0)


