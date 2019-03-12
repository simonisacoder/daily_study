class Solution(object):
    def maxProduct(self, nums):
        if(len(nums) <= 0):
            return 0
        imin = nums[0]
        imax = nums[0]
        tmp_min = nums[0]
        tmp_max = nums[0]
        for i in range(1,len(nums)):
            tmp_min0 = min(nums[i],tmp_min*nums[i],tmp_max*nums[i])
            tmp_max = max(nums[i],tmp_min*nums[i],tmp_max*nums[i])
            tmp_min = tmp_min0
            imin = min(imin,tmp_min)
            imax = max(imax,tmp_max)
            print(tmp_min,tmp_max,imin,imax)
        return imax

if __name__ == "__main__":
    a = [2,3,-2,4]
    s = Solution()
    print(s.maxProduct(a))