from JTSON import JTSON

class Todo:
    def __init__(self):
        self.db = JTSON('todo_db.jtson')

    def add_task(self, task):
        self.db.set(task, False)

    def mark_as_done(self, task):
        self.db.set(task, True)

    def remove_task(self, task):
        self.db.delete(task)

    def list_tasks(self):
        tasks = self.db.get_all()
        print((tasks))
        
        if not tasks:
            print("No tasks found!")
        else:
            print("Task List:")
            for task, done in tasks.items():
                done_str = "Done" if done == b'True' else "Not Done"
                print(f"\t{task}: {done_str}")
                
                # print(self.db.get(("cricket")))
                # print(self.db.get(task))

if __name__ == '__main__':
    todo = Todo()
    while True:
        print("\nTodo List Manager\n"
              "1. Add Task\n"
              "2. Mark as Done\n"
              "3. Remove Task\n"
              "4. List Tasks\n"
              "5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "2":
            task = input("Enter task: ")
            todo.mark_as_done(task)
        elif choice == "3":
            task = input("Enter task: ")
            todo.remove_task(task)
        elif choice == "4":
            todo.list_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
