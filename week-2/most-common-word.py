from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for i in ",.!?;'":
            paragraph = paragraph.replace(i, " ")

        new_paragraph = paragraph.lower().split(" ")

        for i in range(len(new_paragraph)):
            new_paragraph[i] = new_paragraph[i].strip("")

        common_words = Counter(new_paragraph)
        print(common_words)

        for word in common_words.most_common():
            if word[0] not in banned and word[0] != "":
                return word[0]
