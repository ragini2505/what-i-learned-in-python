num1 = float(input('enter number 1 = '))
num2 = float(input('enter number 2 = '))

choice = input('Tell me your choice as per your requirement.. +, -, *, /, //, %, **, = : ')

if choice == '+':
    print(f'Addition: {num1 + num2}')
elif choice == '-':
    print(f'Subtraction: {num1 - num2}')
elif choice == '*':
    print(f'Multiplication: {num1 * num2}')
elif choice == '/':
    print(f'Division: {num1 / num2}')
elif choice == '%':
    print(f'Modulo: {num1 % num2}')    
elif choice == '//':
    print(f'Floor Division: {num1 // num2}')
elif choice == '**':
    print(f'Exponent: {num1 ** num2}') 
elif choice == '=':
    print(f'Equals: {num1 == num2}') 
else:
    print("In-valid choice")              
                