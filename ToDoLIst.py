## import modules
from tkinter import *
from tkinter import messagebox

## newTask()function
def newTask():
    task = my_entry.get()
    if task != "":
         ib.insert(END, task)
         my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "pleasse enter some task.")

#deleteTask()function
def deleteTask():
    ib.delete(ANCHOR)

## creat & configure window
ws = Tk()
ws.geometry("500x450+500+200")
ws.title("pythonGuides")
ws.config(bg="#223441")
ws.resizable(width=False, height=False)


## creating frame
frame = Frame(ws)
frame.pack(pady=10)

## Adding list box
ib = Listbox(
    frame,
    width=25,
    height =8,
    font=("Times", 18),
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none",

)
##id.pack(side=LEFT, fill=BOTH)

## adding dummy data
task_list = [
    "Eat apple",
    "drink water",
    "go gym",
    "write software",
    "prepare for exam",
    "write documentation",
    "take a nap",
    "Learn something",
    "play games",
]

for item in task_list:
    ib.insert(END, item)

## adding scrollbars
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

ib.config(yscrollcommand=sb.set)
sb.config(commannd=ib. yview)

## adding entry box
my_entry = Entry(
    ws,
    front=("times", 24)
)

my_entry.pack(pady=20)

# adding another frame for buttons
button_frame = Frame(ws)
button_frame.pack(pady=20)

# adding buttons 
addTask_btn = Button(
    button_frame,
    Text="delete Task",
    font=("time 14"),
    bg= "#ff8b61",
    padx=20,
    pady=10,
    command= deleteTask
)
"delTask_btn".pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()