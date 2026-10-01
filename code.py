class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        s=0
        h=0
        for num in nums:
            
            s+=num
            h=min(h,s)
        return max(1,1-h)

        
