nums = [1, 5, 3, 2, 8]
target = 6

def linear_search(nums, target):
    for num in nums:
        if num == target:
            return True
    return False 

print(linear_search(nums, target))
