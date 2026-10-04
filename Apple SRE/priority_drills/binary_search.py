# Given a sorted array arr[] and an integer x, find the index (0-based) of the largest element in arr[] 
# that is less than or equal to x. This element is called the floor of x. If such an element does not exist, 
# return -1. Note: In case of multiple occurrences of floor of x, return the index of the last occurrence.
# Examples Input: arr[] = [1, 2, 8, 10, 10, 12, 19], 
# x = 5 Output: 1 Explanation: Largest number less than or equal to 5 is 2, whose index is 1.

arr = [1, 2, 8, 10, 10, 12, 19]
x = 5

low = 0
high = len(arr)
ans = -1
mid = (low + high)// 2
print(mid)
while low <= high:
    mid = (low + high)// 2
    if arr[mid] <= x:
        ans = mid          # possible floor index
        low = mid + 1      # search right for last occurrence
    else:
        high = mid - 1     # search left
print(ans)