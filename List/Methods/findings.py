a = [3,9,0,5,8,3,90,23]

# - finding minimum
print(min(a))

# - finding maximum
print(max(a))

# - finding common in two list
x = [12,5,6,21,45]
y = [12,90,46,73,4,5,6]

#first we w'll covert to set
s1 = set(x)
s2 = set(y)

s3 = s1.intersection(s2)
print(s3)
