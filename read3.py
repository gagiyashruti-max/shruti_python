with open("file1.txt", "w") as f:
    f.write("Hello World!\nWelcome to Python file handling.")

# Read from file
with open("file1.txt", "r") as f:
    data = f.read()

print(data)