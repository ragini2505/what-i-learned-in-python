lst = [1,2,3,4,5]
print(f'Before {lst}')
lst[0] = 'hello'
print(f'After update{lst}')

# -update using slicing
lst1 = [1,2,3,4,5]
lst1[0:3] = 10,20,30
print(lst1)