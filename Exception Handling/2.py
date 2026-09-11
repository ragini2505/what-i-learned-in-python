file = None  # Initialize to prevent NameError in finally block
try:
    # Added 'r' for raw string and fixed the open syntax
    file = open(r'C:\Users\hp\Desktop\python_revision\Exception Handling\errors.txt', mode='r')
    content = file.read()
    print(content)
    
except FileNotFoundError:
    print('File not found!')
    
finally:
    if file:  # Only close if the file was successfully opened
        file.close()  # Fixed typo 'clode'
    print('File operation completed')
