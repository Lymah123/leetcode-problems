# 30. Substring With Concatenation Of All Words
# Difficulty level: Hard
# Top Interview 150

# You are given a string s and an aray of strings words. All the things of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab", "cd", "ef"], then "abcdef", "abefcd", "cdabed", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated because it is not the concatenation of any permutation of words.

# Return an array of the starting indices of all the concatenated substrings in s. You can retun the answer in any order.

# Example 1:
# Input: s = "barfoothefoobarman", words = ["foo", "bar"]
# Output: [0,9]
# Explanation: The substring starting at 0 is "barfoo". It is the concattenation of ["bar", "foo"] which is permutation of words. The  substring starting at 9 is "foobar". It is the concatenation of ["foo", "bar"] which is a permutation of words.

# Example 2:
# Input: s = "wordgoodgoodgoodbestword", words = ["word", "good", "word"]

# Output: []

# Explanation: There is no concatenated substring.

# Example 3:
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
# Explanation: The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

# Constraints:
# 1 <= s.length <= 10^4
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consist of lowercase English letters.
# The order of output does not matter.

# Solution
# 1. First we need to find the length of the words
# 2. Then we need to find the length of the words


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        # Get length information
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        # If total length exceeds string length, return empty
        if total_len > len(s):
            return []

        # Create a frequency map of words
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        result = []

        # Try each possible starting position
        for i in range(len(s) - total_len + 1):
            # Check if substring starting at i is a valid concatenation
            if self._is_valid_concatenation(s, i, word_len, word_count, word_freq):
                result.append(i)

        return result

    def _is_valid_concatenation(self, s: str, start: int, word_len: int, word_count: int, word_freq: dict) -> bool:
        # Create a local frequency map
        current_freq = {}

        # Check each word-length segment
        for i in range(word_count):
            pos = start + i * word_len
            word = s[pos:pos + word_len]

            # If not a valid word from our list
            if word not in word_freq:
                return False

            # Update current frequency
            current_freq[word] = current_freq.get(word, 0) + 1

            # If word appears more times than in our word list
            if current_freq[word] > word_freq[word]:
                return False

        return True
