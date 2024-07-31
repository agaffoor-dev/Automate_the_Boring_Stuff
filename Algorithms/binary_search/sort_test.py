array = [7,3,41,2,7,9,1,3,2,0,5]
array.sort()
print(array)
target = 2
total = len(array)
element = total - 1
mid = int(element / 2)
if array[mid] == target:
    print("target found")
if array[mid] > target:
    print("target is in lower half")
if array[mid] < target:
    print("target is in upper half")
