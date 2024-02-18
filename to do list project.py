import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Create a list to store tasks
        self.tasks = []

        # Create a listbox to display tasks
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
        self.listbox.pack(pady=10)

        # Entry widget for adding new tasks
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=5)

        # Buttons for adding, editing, and deleting tasks
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)

        edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        edit_button.pack(pady=5)

        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.pack(pady=5)

        # Populate listbox with existing tasks
        self.refresh_listbox()

    def add_task(self):
        new_task = self.task_entry.get().strip()
        if new_task:
            self.tasks.append(new_task)
            self.task_entry.delete(0, tk.END)  # Clear the entry widget
            self.refresh_listbox()

    def edit_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            edited_task = simpledialog.askstring("Edit Task", "Edit Task:", initialvalue=self.tasks[selected_index])
            if edited_task is not None:
                self.tasks[selected_index] = edited_task
                self.refresh_listbox()

    def delete_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            task_to_delete = self.tasks[selected_index]
            confirm = messagebox.askyesno("Delete Task", f"Delete '{task_to_delete}'?")
            if confirm:
                del self.tasks[selected_index]
                self.refresh_listbox()

    def refresh_listbox(self):
        # Clear the listbox and populate it with current tasks
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

# Create the main application window
root = tk.Tk()
app = TodoApp(root)

# Start the Tkinter event loop
root.mainloop()
