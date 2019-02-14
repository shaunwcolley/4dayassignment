
def display_menu():
    print("Press 1 to add task")
    print("Press 2 to delete task")
    print("Press 3 to view all tasks")
    print("Press q to quit")

tasks = []

def add_task():
    task = {}
    title = input("Please enter a task: \n")
    priorty = input("High, med, or low priorty?\n")
    task["title"] = title
    task["priority"] = priorty
    tasks.append(task)

def view_tasks():
    for task in tasks:
        for key in task.keys():
            print(task[key])

user_input = ""
while user_input != "q":
    display_menu()
    user_input = input(">> ")
    if user_input == "1":
        add_task()
    elif user_input == "2":
        print("2")#del_task()
    elif user_input == "3":
        view_tasks()
    elif user_input != "q":
        print("Invalid input, please press the following:")
