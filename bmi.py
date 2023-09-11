import math
from tkinter import *
tk = Tk()
tk.title("BMI Calculation")
# tk.minsize(width=300,height=450)
bmi_values=[18.5,24.9, 29.9,34.9, 39.9, 40]
bmi_status=["Underweight","Normal", "Overweight", "Obesity (Class I)", "Obesity (Class II)", "Extreme Obesity"]
tk.geometry("300x400")
tk.eval('tk::PlaceWindow . center')

label_height = Label(text="Enter Your Height (cm)")
# label_height.config(fg="black")
label_height.config(padx=10, pady=10)
label_height.pack(pady=10)
entry_height = Entry(width=20)
entry_height.pack()
label_weight = Label(text="Enter Your Weight (kg)")
# label_height.config(fg="black")
label_weight.config(padx=10, pady=10)
label_weight.pack(pady=10)
entry_weight = Entry(width=20)
entry_weight.pack()
label_BMI = Label(text="Your BMI: ")
label_BMI.config(padx=10, pady=10)

def button_click():
    height_len = len(entry_height.get())
    weight_len = len(entry_weight.get())
    if height_len == 0 or weight_len == 0:
        label_BMI.config(text="Enter both weight and height")
    else:
        try:
            height=(float(entry_height.get())/100)**2
            weight=float(entry_weight.get())
            bmi=(weight/height)
            print(bmi)
            match bmi:
                case bmi if bmi < 18.5:
                    label_BMI.config(text=bmi_status[0])
                case bmi if bmi > bmi_values[0] and bmi < bmi_values[1]:
                    label_BMI.config(text=bmi_status[1])
                case bmi if bmi > bmi_values[1] and bmi < bmi_values[2]:
                    label_BMI.config(text=bmi_status[2])
                case bmi if bmi > bmi_values[2] and bmi < bmi_values[3]:
                    label_BMI.config(text=bmi_status[3])
                case bmi if bmi > bmi_values[3] and bmi < bmi_values[4]:
                    label_BMI.config(text=bmi_status[4])

                case bmi if bmi > bmi_values[5]:
                    label_BMI.config(text= str(math.floor(bmi)) + bmi_status[5])
        except:
            label_BMI.config(text="Enter a valid number")



button = Button(text="Calculate", command=button_click)
button.config(padx=10, pady=10)
button.pack()

label_BMI.pack(pady=10)
tk.mainloop()