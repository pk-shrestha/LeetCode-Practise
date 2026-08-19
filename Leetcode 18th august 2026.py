# Find the largest almost missing integer
# https://leetcode.com/problems/find-the-largest-almost-missing-integer

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        subArrays = []
        subNum = 0
        while subNum + k <= len(nums):
            subArrays.append(nums[subNum:subNum + k])
            subNum += 1
        
        counts = []
        for j in range(len(nums)):
            count = 0            
            for l in range(len(subArrays)):
                if nums[j] in subArrays[l]:
                    count += 1
            counts.append(count)

        minAppear = 1
        if minAppear not in counts:
            return -1
        index = None
        tempIndex = []
        for m in range(len(nums)):
            if counts[m] == minAppear:
                tempIndex.append(m)
        if len(tempIndex) > 1:
            bigger = -1
            for n in range(len(tempIndex)):
                if nums[tempIndex[n]] >= bigger:
                    bigger = nums[tempIndex[n]]
                    index = tempIndex[n]
        else:
            index = tempIndex[0]
        return nums[index]
