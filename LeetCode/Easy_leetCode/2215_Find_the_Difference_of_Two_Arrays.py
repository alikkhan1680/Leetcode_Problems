def findDifference(nums1, nums2):
    return [
        list(set(nums1) - set(nums2)),
        list(set(nums2) - set(nums1))
    ]



print(findDifference([1, 2, 3], [2, 4, 4, 6]))