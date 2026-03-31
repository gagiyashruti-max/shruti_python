tasks = ["Buy groceries", "Complete homework", "Call friend"]

with open("tfile1.txt", "a") as file:
    for task in tasks:
        file.write(task + "...\n")

print("Tasks appended!")