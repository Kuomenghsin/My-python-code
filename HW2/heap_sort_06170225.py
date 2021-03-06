class Solution(object):
    def heap_sort(self,nums): 
        self.nums = nums
        SortedArray = Solution().SwapAndSiftDown(nums)
        return SortedArray
    #HeapSort為控制底下函數的大魔王，輸入list進去後，它會呼叫底下的函式幫它進行排序，最後return答案給使用者
    
    def BuildMaxHeap(self,nums):
    
        n = len(nums)
    
        for i in range((n//2)-1,-1,-1):
            Solution().Heapify(nums,n,i)
        return nums
    #BuildMaxHeap就是把未排序的array創建成最大堆
        
    def SwapAndSiftDown(self,nums):
    
        MaxHeapArray = Solution().BuildMaxHeap(nums)
    
        n = len(MaxHeapArray)
    
        for i in range(n-1,0,-1):
            nums[0],nums[i]=nums[i],nums[0]
            Solution().Heapify(MaxHeapArray,i,0)
        return nums
    #SwapAndSiftDown會先呼叫BuildMaxHeap，並且再用最大堆來進行Swap跟SiftDown
    
    def Heapify(self,nums,n,i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
    
        if left < n and nums[largest] < nums[left]:
            largest = left
    
        if right < n and nums[largest] < nums[right]:
            largest = right
    
        if largest != i:
            nums[largest],nums[i] = nums[i],nums[largest]
            Solution().Heapify(nums,n,largest)
    #主要的排序程序邏輯判斷
