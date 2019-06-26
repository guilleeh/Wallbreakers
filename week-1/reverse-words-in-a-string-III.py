class Solution:
    def reverseWords(self, s: str) -> str:
        word_array = s.split(" ")
        new_array = []
        for word in word_array:
            new_array.append(word[::-1])
        return " ".join(new_array)

