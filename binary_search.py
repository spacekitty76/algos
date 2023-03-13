"""
Array has to already be sorted.
Base case is one element.
Find low value (0).
Find high value(length of array - 1).
Find middle value. (low plus high)

If requested number is less than middle, make the HIGH value 1 less than your guess(-1 from your middle)                  
If requested number is more than the middle, make the LOW value 1 more than your guess ( +1 to your middle)
"""

# parray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # pshort = [1, 2, 3]
# larray = [11, 12, 13, 14, 15]

# def binary_search(num, plist):
#     """
#     num: The number you want to find
#     """
#     low = 0
#     high = len(plist) - 1
#     while low <= high:
#         mid = low + high
#         guess = plist[mid]
#         if num == guess:
#             return mid
#         if num < guess:
#             high -= 1
#         else:
#             low += 1
#     return None

# # print(binary_search(2, pshort))
# # print(binary_search(5, parray))
# print(binary_search(15, larray))

pracca = [11, 12, 13]
pracca2 = [24, 25, 26, 27, 28, 29, 50, 52, 79, 80, 99, 115]

def binary_search(num, dalist):
    low = 0
    high = len(dalist) - 1
    while low <= high:
        mid = low + high
        guess = dalist[mid]
        if guess == num:
            return mid
        elif guess < num:
            low += 1
        else:
            high -= 1
    # if the number isn't in the list
    return None

print(binary_search(24, pracca2))