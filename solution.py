'''
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
'''
"""
"""
# Solution 1
elementos = input("Ingrese los elementos para el array")
array = list(elementos)
rep_array = array
array.extend(rep_array)
print(array)

# Solution 2
array2 = list(elementos)
print(array2 * 2)
