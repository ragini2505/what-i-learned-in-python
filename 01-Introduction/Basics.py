"""String"""
text = "this is a string"
print(type(text))




"""List - elements in list are mutable"""
my_list= ['data1', 'data2','data3']
print(my_list)




"""tuple - element in tuple are immutable"""
my_tuple = ('data1', 'data2', 'data3')
print(my_tuple)




"""Set type - unordered collection of unique items
    set(mutable)
    frozenset(immutable)
"""
unique_number = {1,2,3,3,4,5,5,6}
print(unique_number)

immutable_set = frozenset([1,2,3,3,4,4,5])
print(immutable_set)




"""Mapping datatypes -
    Dictionary-
    pair
    key:value, key1:value2
    curly braces
"""
person = {
    'name': 'gopal', 'age':20
}
print(person)