# Writing to a file
with open("task5.txt", "w") as file:
    file.write("Hello, this is Task 5.\n")
    file.write("This file is created using Python.\n")

# Reading from the file
with open("task5.txt", "r") as file:
    content = file.read()

# Display the content
print("File Content:")
print(content)