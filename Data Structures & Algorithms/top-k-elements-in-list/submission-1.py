from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int) # number -> count

        for number in nums:
            count_map[number] += 1
        
        # print(count_map)
        
        # count_list = list(count_map.values())

        # print(count_list)

        sorted_dict = dict(sorted(count_map.items(), key=lambda item: item[1], reverse=True))

        # print(sorted_dict)

        return list(sorted_dict.keys())[0:k]

        