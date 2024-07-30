import tkinter as tk
from tkinter import messagebox

todo_list = []

def add_task():
    task = task_entry.get()
    if task:
        todo_list.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def update_task_list():
    task_list.delete(0, tk.END)
    for task in todo_list:
        task_list.insert(tk.END, task)

def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        index = selected_task[0]
        todo_list.pop(index)
        update_task_list()

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")


task_label = tk.Label(root, text="Enter a task",font=("open sans", 12, "bold"))
task_label.pack(pady=10)

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task,bg="green",fg="white")
add_button.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task,bg="red",fg="white")
remove_button.pack(pady=10)

task_list = tk.Listbox(root, width=50)
task_list.pack(pady=10)

update_task_list()


root.mainloop()