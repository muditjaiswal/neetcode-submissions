class Solution:
    # 1,1,0,1,1
    # cur = 0 reset curr_length and check for max
    # curr = 1 increment currlength
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        curr_length = 0
        for num in nums:
            if num == 0:
                max_length = max(max_length,curr_length)
                curr_length = 0;
            else:
                curr_length +=1
        return max(max_length,curr_length)

            
        