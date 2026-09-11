# - alias method
lst1 = [1,2,3]
lst2 = lst1

lst2[0] = 100
print(lst1, lst2)

# - copy method
a = [1,2,3]
b = a.copy()
b[0] = 100
print(a, b)