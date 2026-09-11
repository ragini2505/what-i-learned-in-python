# yield keyword used

def count_down(num):
    while num > 0:
        yield num  #yield values one at a time
        num -= 1
        
#using the generator
for number in count_down(5):
    print(number)
    
"""
Difference between decorator and generator 

Decorator - use to modify and enhance function without
            changing actual code of that function
            basically they wrap another function


Generator - use to egnerate a sequence of value over time
            so that ek value pe ek baar me jb aap oerate krte h to 
            yani ki ek baar me ek value pe operate krte ho
            sario itterator pura memory consume nhi krta
"""
    