class Solution:
	#O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(0, len(nums)):
            dict1[nums[i]] = dict1.get(nums[i], i)
            if dict1.get(target-nums[i], None) != None and i != dict1.get(target-nums[i], 0):
                list1 = [dict1[target-nums[i]], i]
                return list1




#O(n^2)
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(0, len(nums)):
    #         count = i + 1
    #         while count < len(nums):
    #             if nums[i] + nums[count] == target:
    #                 list1 = [i, count]
    #                 return list1
    #             count = count + 1