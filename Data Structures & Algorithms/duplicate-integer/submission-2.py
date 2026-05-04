from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashset = set()

        # for i in nums:
        #     if i in hashset:
        #         return True
        #     hashset.add(i)
        # return False

        hashset = defaultdict(list)

        for i in nums:
            if i in hashset:
                return True
            hashset[i]
        
        return False