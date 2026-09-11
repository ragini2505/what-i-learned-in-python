"""
    in - True / False
    not in - opposite
    """
    
lst1 = [1,2,3,4,5]
check = int(input('enter a no to check = '))   
if check in lst1:
    print('found')
else:
    print('not found')  
    
lst2 = [1,2,3,4,5]
check = int(input('enter a no to check = '))   
if check not in lst2:
    print('yes not found')
else:
    print('found')         