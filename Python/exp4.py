# WAP to perform searching activity using linear search and binary search

def LinearSearch(x, target):
    for i in x:
        if target == i:
            print("Yes")
        else:
            print("No")

def BinarySearch(x, target):
    left = 0
    right = len(x) - 1
    while left <= right:
        mid = (left-right)//2
        if x[mid] == target:
            return mid
        elif x[mid] > target:
            right = mid - 1
        else:
            left = mid - 1

list1 = [1,2,3,10]
target = 3
LinearSearch(list1, target)
ans = BinarySearch(list1, target)
print(ans)