class Solution:
    def findMin(self, nums: List[int]) -> int:
        # naive way
        # mini = nums[0]
        # for i in nums:
        #     if i < mini:
        #         mini = i
        # return mini

        # binary search?
        # if sorted, mini should be minimum
        # 
        
        mini = nums[0]
        l = 0
        r = len(nums)-1
        # if mid is larger than 
        while(l <= r):
            mid = l+(r-l)//2
            if nums[mid] < mini:
                mini = nums[mid]
                r = mid-1
            else:
                l = mid+1

        return mini