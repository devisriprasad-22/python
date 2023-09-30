# Create an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added:", task)

# Function to view all tasks in the list
def view_tasks():
    if len(tasks) == 0:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to remove a task from the list
def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print("Task removed:", removed_task)
    else:
        print("Invalid task index. No task removed.")

# Main loop
while True:
    print("\nOptions:")
    print("Enter 'add' to add a task")
    print("Enter 'view' to view your to-do list")
    print("Enter 'remove' to remove a task")
    print("Enter 'quit' to quit the program")

    user_input = input(": ").lower()

    if user_input == "quit":
        break
    elif user_input == "add":
        task = input("Enter the task: ")
        add_task(task)
    elif user_input == "view":
        view_tasks()
    elif user_input == "remove":
        view_tasks()
        task_index = int(input("Enter the task number to remove: "))
        remove_task(task_index)
    else:
        print("Invalid input. Please try again.")
