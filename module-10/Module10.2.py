import tkinter as tk
from tkinter import Menu

# Function to delete a task (right-click)
def delete_task(event):
    event.widget.delete(tk.ANCHOR)

# Main window
root = tk.Tk()
root.title("Drew's To Do List")   # <-- Updated title

# Menu setup with complementary colors
menubar = Menu(root, bg="lightblue", fg="darkorange")

# File menu with Exit option
file_menu = Menu(menubar, tearoff=0, bg="lightblue", fg="darkorange")
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

root.config(menu=menubar)

# Instructions label
label = tk.Label(root, text="Right-click a task to delete it", fg="red")
label.pack()

# Frame to hold the three listboxes
frame = tk.Frame(root)
frame.pack(pady=10)

# First box
tasks1 = tk.Listbox(frame, height=10, width=25, bg="lightyellow", fg="black")
tasks1.grid(row=0, column=0, padx=5)
tasks1.bind("<Button-3>", delete_task)

# Second box
tasks2 = tk.Listbox(frame, height=10, width=25, bg="lightgreen", fg="black")
tasks2.grid(row=0, column=1, padx=5)
tasks2.bind("<Button-3>", delete_task)

# Third box
tasks3 = tk.Listbox(frame, height=10, width=25, bg="lightblue", fg="black")
tasks3.grid(row=0, column=2, padx=5)
tasks3.bind("<Button-3>", delete_task)

# Add your tasks
tasks1.insert(tk.END, "Do the dishes")
tasks2.insert(tk.END, "Finish homework")
tasks3.insert(tk.END, "Fold the laundry")

root.mainloop()
