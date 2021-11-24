def rotate(nums,k):
    return nums[-k:] + nums[:-k]

a1 = [1,2,3,4,5,6,7]
a2 = 3
#Output: [5,6,7,1,2,3,4]
print(rotate(a1,a2))