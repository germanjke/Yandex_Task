nums = [3,4,5,6,7,1,2] #SORTED BUT WITH BIAS ALARMOOO!
target = 4

#TLDR WE MUST USE BINARY SEARCH TO SORTED LIST, AND WE NEED USE BS TO FIND MINIMUM TO MAKE LIST SORTED (DOUBLE BS)

def search_min(nums):
    l = 0
    r = len(nums) - 1
    
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] < nums[mid-1]:
            return mid
        else:
            l = mid + 1 

def binary_search(nums, target):
    l = 0
    r = len(nums) - 1
    
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            r = mid - 1
        if nums[mid] < target:
            l = mid + 1

print(nums[search_min(nums):] + nums[:search_min(nums)])

print(binary_search((nums[search_min(nums):] + nums[:search_min(nums)]), target))

bs_sorted = binary_search((nums[search_min(nums):] + nums[:search_min(nums)]), target)
bs_bias = bs_sorted - len(nums[search_min(nums):])
print(bs_bias)

# input [1, 2, 3, 4, 5, 6, 7]
# output1
