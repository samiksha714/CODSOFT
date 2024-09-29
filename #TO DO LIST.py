#TO DO LIST

class ToDoList:
    def __init__(self):
        self.tasks = {}

    def show_tasks(self):
        print("\nTo-Do List:")
        for task_id, task in self.tasks.items():
            status = "Done" if task["completed"] else "Pending"
            print(f"{task_id}. {task['name']} - {status}")

    def add_task(self):
        task_name = input("Enter task name: ")
        self.tasks[len(self.tasks) + 1] = {"name": task_name, "completed": False}
        print(f"Task '{task_name}' added successfully!")

    def delete_task(self):
        task_id = int(input("Enter task ID to delete: "))
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Task {task_id} deleted successfully!")
        else:
            print(f"Task {task_id} not found.")

    def update_task(self):
        task_id = int(input("Enter task ID to update: "))
        if task_id in self.tasks:
            task_name = input("Enter new task name: ")
            self.tasks[task_id]["name"] = task_name
            print(f"Task {task_id} updated successfully!")
        else:
            print(f"Task {task_id} not found.")

    def mark_completed(self):
        task_id = int(input("Enter task ID to mark completed: "))
        if task_id in self.tasks:
            self.tasks[task_id]["completed"] = True
            print(f"Task {task_id} marked completed!")
        else:
            print(f"Task {task_id} not found.")

    def run(self):
        while True:
            print("\nTo-Do List Menu:")
            print("1. Show Tasks")
            print("2. Add Task")
            print("3. Delete Task")
            print("4. Update Task")
            print("5. Mark Completed")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.show_tasks()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                self.update_task()
            elif choice == "5":
                self.mark_completed()
            elif choice == "6":
                print("Exiting To-Do List.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    todo = ToDoList()
    todo.run()
