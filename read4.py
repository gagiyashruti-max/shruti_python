lines = ["Apple\n", "Banana\n", "Mango\n"]

# Write list of lines
with open("file2.txt", "w") as f:
    f.writelines(lines)

# Read line by line
with open("file2.txt", "r") as f:
    for line in f:
        print(line.strip())