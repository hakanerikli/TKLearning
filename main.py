import tkinter

window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(700, 500)

def click_button():
    print(my_entry.get())


# label
my_label = tkinter.Label(text="Hello Tkinkter", font=("Arial",30, "normal"))
# my_label.config(bg="black", fg="white")
# my_label.pack(side="right")
# my_label.place(x=0, y=0)
my_label.grid(row=0, column=0)

# Button
my_button = tkinter.Button(text="Gönder", command=click_button, width=30)
# my_button.pack(side="right")
# my_button.place(x=100, y=100)
my_button.grid(row=1, column=1)

# Entry
my_entry = tkinter.Entry(width=20)
# my_entry.pack(side="right")
my_entry.grid(row=2, column= 2)

window.mainloop()
