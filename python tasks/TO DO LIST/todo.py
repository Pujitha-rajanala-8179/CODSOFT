import os

FILENAME = "tasks.txt"
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return file.read().splitlines()
    return []
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task +"\n")
def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour TO-DO List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}.{task}")
def main():
    tasks = load_tasks()

    while True:
        print("\n---TO DO LIST---")
        print("1. Add Task")
        print("2. View Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5):")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added successfully!")

        elif choice =="2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                num = int(input("Enter task number to update:"))
                if 1 <=num <= len(tasks):
                    new_task = input("Enter new task: ")
                    tasks[num -1] = new_task
                    save_tasks(tasks)
                    print("Task updated! ")
                else:
                    print("Invalid task number.")
        elif choice == "4":
            show_tasks(tasks)
            if tasks:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <=len(tasks):
                    tasks.pop(num - 1)
                    save_tasks(tasks)
                    print("Task deleted!")
                else:
                    print("Invalid task number.")

        elif choice == "5":
            print("Exiting TO-DO List. Bye!")
            break

        else:
            print("Invalid choice. Please enter 1-5.")
        
if __name__ == "__main__":
    main() 
                        