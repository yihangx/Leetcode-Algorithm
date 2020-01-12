s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]

def word_break_II(s, wordDict):
    res = []
    path = ""
    dfs(s, wordDict, path, res)
    return res

def dfs(s, wordDict, path, res):
    if word_break_I(s, wordDict):
        if not s:
            res.append(path[:-1])
            return
        for i in range(len(s) + 1):
            if s[:i] in wordDict:
                dfs(s[i:], wordDict, path + s[:i] + " ", res)

def word_break_I(s, wordDict):
    dp = [True] + [False] * len(s)
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            if dp[i] and s[i:j] in wordDict:
                dp[j] = True
    return dp[-1]

print(word_break_II(s, wordDict))
