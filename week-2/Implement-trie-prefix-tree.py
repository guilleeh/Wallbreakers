class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict["#"] = "#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_dict = self.root
        for letter in word:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                return False
        if "#" in current_dict:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_dict = self.root
        for letter in prefix:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
