class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        queue1=deque()
        queue2=deque()
        left=0
        long=0
        for i in range(len(nums)):
            while(queue1 and queue1[-1]<nums[i]):
                queue1.pop()
            queue1.append(nums[i])
            while(queue2 and queue2[-1]>nums[i]):
                queue2.pop()
            queue2.append(nums[i])
            while(queue1[0]-queue2[0]>limit):
                if(queue1[0]==nums[left]):
                    queue1.popleft()
                if(queue2[0]==nums[left]):
                    queue2.popleft()
                left+=1
            long=max(long,i-left+1)
        return long


     

       




            
            

        