class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
        morse = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]

        morse_mapping = {}
        transformation_set = set()

        for i in range(len(alphabet)):
            morse_mapping[alphabet[i]] = morse[i]

        for word in words:
            word_in_morse = ""
            for char in word:
                word_in_morse += morse_mapping[char]
            transformation_set.add(word_in_morse)

        return len(transformation_set)

