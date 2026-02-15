class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p3 = len(nums1) - 1
        while p1 >= 0 or p2 >= 0:
            if p1 >= 0 and p2 >= 0:
                if nums1[p1] > nums2[p2]:
                    nums1[p3] = nums1[p1]
                    p1 -= 1
                else:
                    nums1[p3] = nums2[p2]
                    p2 -= 1
            elif p1 >= 0:
                nums1[p3] = nums1[p1]
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p2 -= 1
            p3 -= 1


"""
Linear solution, O(2n + 2m) "double because final answer is copied into nums1

length = m + n
        answer = [0] * length
        p1 = p2 = p3 = 0
        while p1 < m or p2 < n:
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    answer[p3] = nums1[p1]
                    p1 += 1
                else:
                    answer[p3] = nums2[p2]
                    p2 += 1
            elif p1 < m:
                answer[p3] = nums1[p1]
                p1 += 1
            else:
                answer[p3] = nums2[p2]
                p2 += 1
            p3 += 1
        nums1[:] = answer.copy()
"""
    
