class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = {}
        for i in nums:
            count = 1
            if i in num_dict:
                num_dict[i] += 1
            else:
                num_dict[i] = count
        
        for k,v in num_dict.items():
            if v > (len(nums)/2):
                return k