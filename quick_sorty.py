"""Divide and conquer. 
Get yourself a pivot point (arr[0] for simplicity)
iterate through the list.
if i < pivot, add it to a lessthan list
if i > pivot, add it to a greater than list
call sort again and pass it less than list + pivot + greater than list

find your base case to end recursion
thats a 2 item list or less. it's already going to be sorted if thats the case
"""

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        less = []
        greater = []
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            if i > pivot:
                greater.append(i)
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
print(quick_sort([17, 2, 4, 20]))