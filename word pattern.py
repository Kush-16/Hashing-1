class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split(" ")
        if len(pattern) != len(word):
            return False

        patter_to_word = {}
        word_to_pattern = {}

        for ch, word in zip(pattern, word):
            if ch not in patter_to_word:
                if word not in word_to_pattern:
                    patter_to_word[ch] = word
                    word_to_pattern[word] = ch
                else:
                    return False
            else:
                if patter_to_word[ch] != word:
                    return False
        return True
    
    #TC = O(n)
