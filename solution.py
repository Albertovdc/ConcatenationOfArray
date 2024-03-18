# Solution 1
elementos = input("Ingrese los elementos para el array")
array = list(elementos)
rep_array = array
array.extend(rep_array)
print(array)

# Solution 2
array2 = list(elementos)
print(array2 * 2)
