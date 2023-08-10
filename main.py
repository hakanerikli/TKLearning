import tkinter

window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(700, 500)

def click_button():
    print("Button Clicked!")


# label
my_label = tkinter.Label(text="Hello Tkinkter", font=("Arial",30, "normal"))
# my_label.config(bg="black", fg="white")
my_label.pack()

# Button
my_button = tkinter.Button(text="Gönder", command=click_button)
my_button.pack()


window.mainloop()
