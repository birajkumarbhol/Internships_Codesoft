class Task:
    def __init__(self, title, description=''):
        self.title = title
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        return f"{'[X]' if self.completed else '[ ]'} {self.title}: {self.description}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=''):
        task = Task(title, description)
        self.tasks.append(task)

    def update_task(self, index, title=None, description=None, completed=None):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if title:
                task.title = title
            if description:
                task.description = description
            if completed is not None:
                task.completed = completed

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. Listout Tasks")
    print("5. Exit")

def main():
    task_manager = TaskManager()
    while True:
        display_menu()
        choice = input("Please choose an option: ")
        if choice == '1':
            title = input("Please enter task title: ")
            description = input("Please enter task description: ")
            task_manager.add_task(title, description)
        elif choice == '2':
            index = int(input("Please enter task index to update: "))
            title = input("Please enter new title (or leave blank): ")
            description = input("Please enter new description (or leave blank): ")
            completed = input("Mark as completed? (yes/no): ").lower() == 'yes'
            task_manager.update_task(index, title, description, completed)
        elif choice == '3':
            index = int(input("Please enter task index to delete: "))
            task_manager.delete_task(index)
        elif choice == '4':
            task_manager.list_tasks()
        elif choice == '5':
            break
        else:
            print("This is not a valid choice, please try again.")

if __name__ == "__main__":
    main()
