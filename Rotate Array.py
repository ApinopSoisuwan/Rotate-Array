def rotate(nums,k):
    from collections import deque
    nums = deque(nums)
    nums.rotate(k)
    return list(nums)





a1 = [1,2,3,4,5,6,7]
a2 = 3
#Output: [5,6,7,1,2,3,4]
print(rotate(a1,a2))