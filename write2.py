with open("tfile2.txt", "a") as file:
    for i in range(3):
        task = input(f"Enter task {i+1}: ")
        file.write(task + "...\n")

print("User tasks appended!")