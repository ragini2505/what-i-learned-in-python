with open(r'C:\Users\hp\Desktop\python_revision\File Handling\files.txt', 'a') as file:
    content = input('enter content to append = ')
    file.write(content)  # Changed .append() to .write()
    print('appended successfully!')