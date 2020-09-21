class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_len=len(nums)
        n_len=n_len/2
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i] +=1
        for i in nums:
            if dic[i]>n_len:
                return i
            