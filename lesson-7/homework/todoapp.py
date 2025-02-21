import json

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

class ToDoApp:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self):
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD, optional): ") or None
        status = input("Enter Status (Pending/In Progress/Completed): ")
        
        task = Task(task_id, title, description, due_date, status)
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("Tasks:")
        for task in self.tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input("Enter new Title: ") or task.title
                task.description = input("Enter new Description: ") or task.description
                task.due_date = input("Enter new Due Date (YYYY-MM-DD, optional): ") or task.due_date
                task.status = input("Enter new Status (Pending/In Progress/Completed): ") or task.status
                print("Task updated successfully!")
                return
        print("Task ID not found.")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                return
        print("Task ID not found.")

    def filter_tasks(self):
        status = input("Enter status to filter by (Pending/In Progress/Completed): ")
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if not filtered_tasks:
            print("No tasks found with this status.")
            return
        print("Filtered Tasks:")
        for task in filtered_tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file)
        print("Tasks saved successfully!")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks_data = json.load(file)
                self.tasks = [Task(**data) for data in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def run(self):
        while True:
            print("\nWelcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")
            
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_tasks()
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                self.load_tasks()
            elif choice == "8":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ToDoApp()
    app.run()
