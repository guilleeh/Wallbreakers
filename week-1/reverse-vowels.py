class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        str_as_list = list(s)

        i, j = 0, len(s) - 1

        while i < j:
            if str_as_list[i] not in vowels:
                i += 1
                continue

            if str_as_list[j] not in vowels:
                j -= 1
                continue

            str_as_list[i], str_as_list[j] = str_as_list[j], str_as_list[i]

            i += 1
            j -= 1
        return "".join(str_as_list)

