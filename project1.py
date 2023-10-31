import tkinter as tk

class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

def add_task():
    description = description_entry.get()
    due_date = due_date_entry.get()
    priority = priority_entry.get()
    if description:
        task = Task(description, due_date, priority)
        tasks.append(task)
        update_task_list()
        clear_entry_fields()

def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        del tasks[selected_task[0]]
        update_task_list()

def mark_completed():
    selected_task = task_list.curselection()
    if selected_task:
        tasks[selected_task[0]].completed = True
        update_task_list()

def update_task_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        if not task.completed:
            task_list.insert(tk.END, f"Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority}")

def clear_entry_fields():
    description_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)
    priority_entry.delete(0, tk.END)

# Create the main window
app = tk.Tk()
app.title("To-Do List App")

# Entry widgets for task details
description_label = tk.Label(app, text="Description:")
description_label.pack()
description_entry = tk.Entry(app, width=40)
description_entry.pack()

due_date_label = tk.Label(app, text="Due Date:")
due_date_label.pack()
due_date_entry = tk.Entry(app, width=40)
due_date_entry.pack()

priority_label = tk.Label(app, text="Priority:")
priority_label.pack()
priority_entry = tk.Entry(app, width=40)
priority_entry.pack()

# Buttons to add, remove, and complete tasks
add_button = tk.Button(app, text="Add Task", command=add_task)
remove_button = tk.Button(app, text="Remove Task", command=remove_task)
complete_button = tk.Button(app, text="Mark as Completed", command=mark_completed)
add_button.pack()
remove_button.pack()
complete_button.pack()

# Listbox to display tasks
task_list = tk.Listbox(app, selectmode=tk.SINGLE, width=60, height=15)
task_list.pack(pady=10)

# List to store tasks
tasks = []

# Start the GUI application
app.mainloop()
