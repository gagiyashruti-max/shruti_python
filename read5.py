# Append data
with open("filesh.txt", "a") as f:
    f.write("New line added.\n")

# Read file
with open("filesh.txt", "r") as f:
    print(f.read())