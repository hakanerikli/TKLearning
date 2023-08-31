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


window.mainloop()