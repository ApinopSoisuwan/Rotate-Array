def rotate(nums,k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

a1 = [1,2,3,4,5,6,7]
a2 = 3
#Output: [5,6,7,1,2,3,4]
print(rotate(a1,a2))