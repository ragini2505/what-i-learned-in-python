def get_full_name(first_name, last_name):
    ''' return the full name, in a neated format'''
    full_name = f'{first_name} {last_name}'
    return full_name
    #print(full_name)
    
name = get_full_name("gopal","raju") 
print(name)   

# return - send the valiue back to the function to the caller and just display the value on the console
# print - just print the value

"""
    function naming- meaningful
                    - avoid global variables
    """
    
# example
def sum(a,b):
    return a+b
a=10
b = 20
result = sum(a,b)
print(result)
    
