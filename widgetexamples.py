from tkinter import *

window = Tk()
window.title("Tkinter Python")
window.minsize(width=600,height=600)

label = Label(text="my label")
label.config(bg="black")
label.config(fg="white")
label.config(padx=10, pady=10)
label.pack(pady=10)

def button_click():
    print("button clicked")
    print(text.get(1.0, END))

button = Button(text="Send", command=button_click)
button.config(padx=10, pady=10)
button.pack()

entry = Entry(width=20)
entry.pack()

text = Text(width=30, height=5)
text.pack()

# scale

def scale_selected(value):
    print(value)

my_scale = Scale(from_=0, to=50, command=scale_selected)
my_scale.pack()

# spinbox
def spinbox_selected():
    print(my_spinbox.get())
my_spinbox = Spinbox(from_=0, to=50, command=spinbox_selected)
my_spinbox.pack()

# checkbutton
def checkbutton_selected():
    print(check_state.get())
check_state=IntVar()
my_checkbutton = Checkbutton(text="Check", variable=check_state, command=checkbutton_selected)
my_checkbutton.pack()

# radiobutton
def radiobutton_selected():
    print(radio_checkstate.get())
radio_checkstate= IntVar()
my_radiobutton= Radiobutton(text="condition 1", value=10, variable=radio_checkstate,command=radiobutton_selected)
my_radiobutton2= Radiobutton(text="condition 2", value=20, variable=radio_checkstate, command=radiobutton_selected)
my_radiobutton.pack()
my_radiobutton2.pack()

# listbox
def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox(window,selectmode=MULTIPLE)
name_list= ["Hakan", "Erikli", "ABC", "DEF", "GHI"]

for i in range(len(name_list)):
    my_listbox.insert(i, name_list[i])
my_listbox.bind('<<ListboxSelect>>',listbox_selected)
my_listbox.pack()


window.mainloop()