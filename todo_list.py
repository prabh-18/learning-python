"""
Command-Line To-Do List App
A beginner-friendly app that lets you add, view, remove, and mark tasks as complete.
"""

# This list holds all our tasks. Each task is a string.
# Completed tasks will have "[DONE] " at the start.
tasks = []


def show_menu():
    """Display the main menu and return the user's choice."""
    print("\n" + "=" * 40)
    print("         TO-DO LIST MENU")
    print("=" * 40)
    print("1. Add task")
    print("2. View all tasks")
    print("3. Remove task")
    print("4. Mark task as complete")
    print("5. Exit")
    print("=" * 40)
    choice = input("Enter your choice (1-5): ").strip()
    return choice


def add_task():
    """Ask the user for a new task and add it to the list."""
    task = input("Enter the task to add: ").strip()
    if task == "":
        print("  [!] Task cannot be empty. Nothing added.")
        return
    tasks.append(task)
    print(f"  ✓ Added: '{task}'")


def view_tasks():
    """Display all tasks with their numbers. Shows [DONE] for completed ones."""
    if not tasks:
        print("  No tasks yet. Add one with option 1!")
        return
    print("\n  Your tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"    {i}. {task}")


def remove_task():
    """Show tasks, ask for a number, and remove that task. Handles invalid input."""
    if not tasks:
        print("  No tasks to remove. Add some first!")
        return
    view_tasks()
    try:
        num_str = input("\n  Enter the number of the task to remove: ").strip()
        if not num_str:
            print("  [!] No number entered. Cancelled.")
            return
        num = int(num_str)
        if num < 1 or num > len(tasks):
            print(f"  [!] Please enter a number between 1 and {len(tasks)}.")
            return
        # Convert to 0-based index and remove
        removed = tasks.pop(num - 1)
        print(f"  ✓ Removed: '{removed}'")
    except ValueError:
        print("  [!] Please enter a valid number.")


def mark_complete():
    """Show tasks, ask for a number, and add [DONE] prefix to that task."""
    if not tasks:
        print("  No tasks to mark. Add some first!")
        return
    view_tasks()
    try:
        num_str = input("\n  Enter the number of the task to mark complete: ").strip()
        if not num_str:
            print("  [!] No number entered. Cancelled.")
            return
        num = int(num_str)
        if num < 1 or num > len(tasks):
            print(f"  [!] Please enter a number between 1 and {len(tasks)}.")
            return
        idx = num - 1
        task = tasks[idx]
        if task.startswith("[DONE] "):
            print("  That task is already marked complete.")
            return
        tasks[idx] = "[DONE] " + task
        print(f"  ✓ Marked complete: '{task}'")
    except ValueError:
        print("  [!] Please enter a valid number.")


def main():
    """Run the app: show menu in a loop until user chooses Exit."""
    print("Welcome to the To-Do List App!")
    while True:
        choice = show_menu()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_complete()
        elif choice == "5":
            print("\nGoodbye! Have a productive day.")
            break
        else:
            print("  [!] Invalid choice. Please enter 1, 2, 3, 4, or 5.")


# This runs the app when you execute this file (e.g. python todo_list.py)
if __name__ == "__main__":
    main()
