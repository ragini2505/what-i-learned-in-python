"""
syntax -
[expression for item in iterable if condition]
e - x*2
item -
iterable - range(1,11)
condition optional

"""

# traditional way
"""squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares) """   

# - using list comprehension
squares = [i**2 for i in range(1,11)]
print(squares)