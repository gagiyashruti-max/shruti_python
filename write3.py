def add_tasks(task_list):
    with open("tfile3.txt", "a") as file:
        for task in task_list:
            file.write(task + "...\n")

tasks = ["Read book", "Go jogging", "Study Python"]
add_tasks(tasks)

print("Tasks added using function!")