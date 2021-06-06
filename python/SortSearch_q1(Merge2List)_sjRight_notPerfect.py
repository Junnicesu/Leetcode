class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for id in range(n):
                nums1[id] = nums2[id]
            return 
        
        if n == 0:
            return
        
        newNums = []
        idy = 0
        idx = 0
        while idx < m:
            if idy == n or nums1[idx] < nums2[idy] :
                newNums += [nums1[idx]]
                idx += 1

            while idy < n :  
                print("nums1[%d]: %d, nums2[%d]: %d" % (idx, nums1[idx], idy, nums2[idy])) #sjdb             
                if idx< m and nums1[idx] < nums2[idy]: #sj!!!!!!
                    break
                else:
                    print("To add nums2[%d] : %d " % (idy, nums2[idy]))
                    newNums += [nums2[idy]]
                    idy += 1
                        
        print(newNums) #sjdb
        for id in range(n+m):
            nums1[id] = newNums[id]
        
                