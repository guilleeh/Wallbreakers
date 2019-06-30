from collections import OrderedDict


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = OrderedDict()

        for c in s:
            if c in char_dict:
                char_dict[c] = char_dict[c] + 1
            else:
                char_dict[c] = 1

        for key, value in char_dict.items():
            print(key, value)
            if value == 1:
                return s.find(key)
        return -1
