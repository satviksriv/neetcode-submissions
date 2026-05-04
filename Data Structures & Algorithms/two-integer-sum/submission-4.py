from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # prevMap = {} # value: index

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in prevMap:
        #         return [prevMap[diff], i]
        #     prevMap[n] = i
        
        # return

        value_index_map = defaultdict(int)

        for index, number in enumerate(nums):
            diff = target - number
            if diff in value_index_map:
                return [value_index_map[diff], index]
            value_index_map[number] = index
        
        return