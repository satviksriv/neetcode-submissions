from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        # for word in strs:
        #     sorted_word = tuple(sorted(word))
        #     anagram_map[sorted_word].append(word)

        for word in strs:
            count = [0] * 26 # for a to z

            for char in word:
                count[ord(char) - ord('a')] += 1
            
            anagram_map[tuple(count)].append(word)
        
        return list(anagram_map.values())