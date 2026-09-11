"""if condition:
    statements
   elif condition:
    statement
    .
    .
   else:
    statement 
"""
age = int(input('enter your age = '))
if (age>= 18 and age <75):
    print('you can vote')
elif age >= 75:
    print('what you are doing you should die....')    
elif age <= 0:
    print("invalid data")
else:
    print("Error.....")    