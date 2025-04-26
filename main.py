import tkinter as tk 
from tkinter import messagebox
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "task.json"


def add_task():
    task=task_entery.get()
    if task:
        tasklist.insert(tk.END,task)
        task_entery.delete(0,tk.END)
        save_task()
    else:
        messagebox.showwarning("Warning","Please enter a task")
    

def delete_task():
    try:
        taskI=tasklist.curselection()[0]
        tasklist.delete(taskI) 
        save_task()
    except IndexError:
        messagebox.showwarning("Warning","Please Select a task to delete")

def complete_task():
    try:
        taskI=tasklist.curselection()[0]
        task=tasklist.get(taskI)
        if task.startswith("✓ "):
            task=task[2:]
        else:
            task="✓ "+task
        tasklist.delete(taskI)
        tasklist.insert(tk.END,task)
        save_task()
    except IndexError:
        messagebox.showwarning("Warning","Please select a task to mark completed")

def save_task():
    try:
        tasks=tasklist.get(0,tk.END)
        with file_path.open("w") as f:
            json.dump(tasks,f)
    except:
        pass

def load_task():
    try:
        with file_path.open("r") as f:
            tasks=json.load(f)
            for task in tasks:
                tasklist.insert(tk.END,task)

    except :
        pass


window=tk.Tk()

window.geometry("500x400")
window.title("Nikhil's Task Manager" )

to_do=tk.Label(window,text="Task Manager",font=("Arial",18))
to_do.pack(pady=10)

frame_1=tk.Frame(window)
frame_1.pack(pady=10)

task_entery=tk.Entry(frame_1,width=40)
task_entery.pack(side=tk.LEFT)

add_button=tk.Button(frame_1,text="Add Task",command=add_task)
add_button.pack(side=tk.LEFT,padx=10)

frame_2=tk.Frame(window)
frame_2.pack(pady=10,expand=True,fill=tk.BOTH)

scrollbar=tk.Scrollbar(frame_2)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

tasklist=tk.Listbox(frame_2,width=45,height=12,selectmode=tk.SINGLE,yscrollcommand=scrollbar.set)
tasklist.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)

scrollbar.config(command=tasklist.yview)

frame_3=tk.Frame(window)
frame_3.pack(pady=10)

delete=tk.Button(frame_3,text="Delete Task",command=delete_task)
delete.pack(side=tk.LEFT,padx=10)

complete=tk.Button(frame_3,text="Mark Completed",command=complete_task)
complete.pack(side=tk.LEFT,padx=10)

load_task()

window.mainloop()