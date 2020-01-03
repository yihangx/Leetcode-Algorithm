start = "hit"
end = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
import collections
def word_ladder(start, end, wordList):
    wordList = set(wordList)
    deq = collections.deque([(start, 1)])
    visited = set()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    while deq:
        word, length = deq.popleft()
        if word == end:
            return length
        for i in range(len(word)):
            for ch in alpha:
                new_word = word[:i] + ch + word[i+1:]
                if new_word in wordList and new_word not in visited:
                    deq.append((new_word, length + 1))
                    visited.add(new_word)
    return 0
print(word_ladder(start, end, wordList))
