def find(nums, target):
    left = 0;
    right= len(nums)-1;
 
    while left<=right:
        mid = left + (right-left)/2
        if target==nums[mid]:
            return mid
 
        if nums[left] <= nums[mid]:
            if nums[left] <= target and target < nums[mid]:
                right=mid-1
            else:
                left=mid+1

        else:
            if nums[mid]<target and target<=nums[right]: 
            	left=mid+1
            else:
                right=mid-1
        

 
    return -1;


print find([4, 5, 6, 1, 2], 1)
print find([4, 5, 6, 1, 2], 2)
print find([4, 5, 6, 1, 2], 3)
print find([4, 5, 6, 1, 2], 4)
print find([4, 5, 6, 1, 2], 5)
print find([4, 5, 6, 1, 2], 6)


print find([4, 5, 5, 6, 2], 6)

print find([4, 5, 0, 1, 2], 4)
print find([4, 5, 0, 1, 2], 5)

print find([4, 5, 0, 1, 2], 1)
print find([4, 5, 0, 1, 2], 2)

print find([1, 2, 3, 4, 5, 6], 6)
print find([1, 2, 3, 4, 5, 6], 1)
