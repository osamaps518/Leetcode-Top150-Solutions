class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = len(nums) - 1
        i = 0
        while i <= p:
            if nums[p] == val:
                p -= 1
                continue
            if nums[i] == val:
                nums[i] = nums[p]
                p -= 1
            i += 1
        return p + 1
