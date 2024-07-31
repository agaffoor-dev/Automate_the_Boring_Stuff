import time

nums = [2,5,7,11,14,2,5,7,11,14,2,5,7,11,14,2,5,7,11,14,2,5,7,11,14,2,5,7,11,14,2,5,7,11,14,2,5,7,11,14,2,5,7,11,14,2,5,7,11,14,2,5,7,11,14,2,5,7,11,14,2,5,7,11,14,2,5,7,11,14,2,5,7,11,14,21,27,30,36]
target = 27

def binary_search(nums,target,low,high):
  if low > high:
    return False
  else:
    mid = (low + high)//2
    if nums[mid] == target:
      return True
    elif nums[mid] < target:
      return binary_search(nums,target,mid+1,high)
    else:
      return binary_search(nums,target,low,mid-1)

def linear_search(nums, target):
    for num in nums:
        if num == target:
            return True
    return False 

start = time.time()
print(binary_search(nums,target,0,len(nums)-1))
#print(linear_search(nums, target))
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
