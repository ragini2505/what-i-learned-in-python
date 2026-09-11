"""ask user to skip a number"""

start = int(input('enter start = '))
end = int(input('enter end = '))

if start > end:
    print("in-valid input: Your start number cannot be greater than your end number!")
elif start == end:
    print("in-valid input: Start and end numbers cannot be identical!")

else:
    skip = int(input('enter number you want to skip = '))

    print("Result:")
    for i in range(start, end + 1):
        if i == skip:
            continue
        print(i, end=" ")
    print()