from datetime import date

class Task:
    def __init__(self, name: str, description: str, status: str, create_date: str, end_date: str):
        self.name = name
        self.description = description
        self.status = status
        self.create_date = create_date
        self.end_date = end_date

class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, name: str, description: str, status: str, create_date: str, end_date: str):
        task = Task(name, description, status, create_date, end_date)
        self.tasks.append(task)
        print(f"Task '{name}' created.")

    def update_task(self, name: str, status: str):
        for task in self.tasks:
            if task.name == name:
                task.status = status
                print(f"Task '{name}' updated.")
                return
        print(f"Task '{name}' not found.")

    def delete_task(self, name: str):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                print(f"Task '{name}' deleted.")
                return
        print(f"Task '{name}' not found.")

    def watch_all_tasks(self):
        if self.tasks:
            print("List of tasks:")
            for task in self.tasks:
                print(f"Name: {task.name}, Description: {task.description}, Status: {task.status}")
        else:
            print("No tasks found.")

    def filter_tasks(self, status: str):
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if filtered_tasks:
            print(f"Tasks with status '{status}':")
            for task in filtered_tasks:
                print(f"Name: {task.name}, Description: {task.description}")
        else:
            print(f"No tasks found with status '{status}'.")

task_manager = TaskManager()
task_manager.create_task("grocery_list", "bread, butter, milk", "new", date.today(), "2023-12-31")
task_manager.create_task("clean_house", "vacuum, mop the floor", "in progress", date.today(), "2023-12-30")
task_manager.create_task("write_report", "prepare sales report", "completed", date.today(), "2023-12-25")

task_manager.watch_all_tasks()

task_manager.update_task("grocery_list", "in progress")
task_manager.update_task("non_existing_task", "completed")

task_manager.filter_tasks("new")
task_manager.filter_tasks("completed")

task_manager.delete_task("clean_house")
task_manager.delete_task("non_existing_task")