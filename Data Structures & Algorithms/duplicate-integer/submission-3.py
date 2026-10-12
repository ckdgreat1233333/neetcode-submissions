class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k = []
        for i in range(len(nums)): 
            if nums[i] in k:
                return True
            else:
                k.append(nums[i])
        else:
            return False
        