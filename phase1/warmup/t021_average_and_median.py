def average(*nums):  
    return sum(nums)/len(nums)

def median(*nums):
    n = len(nums)
    return nums[n//2] if n%2 else (nums[n//2-1] + nums[n//2])/2


nums1 = [1,2,3,4]
print(average(*nums1), median(*nums1))

nums2 = [1,2,3,4,5]
print(average(*nums2), median(*nums2))

nums2 = [1]
print(average(*nums2), median(*nums2))