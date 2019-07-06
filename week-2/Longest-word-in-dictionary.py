class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=len)
        candidate = words[0]
        existing = dict()
        for word in words:
            if len(word) == 1:
                existing[word] = 1
            if existing.get(word[:-1]):
                existing[word] = 1
                if len(candidate) < len(word) or (
                    len(candidate) == len(word) and word < candidate
                ):
                    candidate = word
        return candidate
