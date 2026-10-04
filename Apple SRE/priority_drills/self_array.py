238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:


        n = len(nums)

        #intialize array with values 1 the size of the input nums 
        ans = [1] * n
         
         # start from  letft pointer 1 on the ans array and multiple the previous its element with previous element of nums 
        for i in range(1 ,n):
            ans[i] = ans[i-1] * nums[i-1]
        
        #initizale the variable called right to 1 and we need to start the multiple but this time from right 
        rightproduct = 1 

        # run the loop from right and multiple the ans element with the right product and update the ans of [i] 
        for i in range(n-1 ,-1 ,-1):
            ans[i] = ans[i] * rightproduct 

            #and then mutliple the right product with the element of nums and update the right prodcut 
            rightproduct = rightproduct * nums[i]
        
        return ans
        
