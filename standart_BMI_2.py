import tkinter
from multiprocessing.managers import Value

wn = tkinter.Tk()
wn.title("BMI CALCULATOR")
wn.minsize(width=400, height=500)

we_label = tkinter.Label(text="Enter Your Weight (kg)")
he_label = tkinter.Label(text="Enter Your Height (m)")
we_entry = tkinter.Entry(width=8)
he_entry = tkinter.Entry(width=8)

def button():
    weight = we_entry.get().strip()
    height = he_entry.get().strip()
    if  weight == "" and height == "":
        output = "Enter a number for weight and height!"
    elif weight == "":
        output = "Enter a number for weight"
    elif height == "":
        output = "Enter a number for height!"

    else:
        try:
            a = float(weight)
            b = float(height)
            bmi = a / (b*b)
            output = f"BMI: {bmi}"
            if bmi < 18.5:
                output_2 = "UNDERWEİGHT"
            elif bmi == 18.5:
                output_2 = "ON THE BORDER OF THE NORMAL WEİGHT"
            elif 18.5 < bmi < 25:
                output_2 = "NORMAL WEİGHT"
            elif 25 == bmi:
                output_2 = "ON THE BORDER OF THE OVERWEİGHT"
            elif 25 < bmi < 30:
                output_2 = "OVERWEİGHT"
            elif 30 == bmi:
                output_2 = "ON THE BORDER OF THE OBESİTY"
            elif 30 < bmi:
                output_2 = "OBESİTY"
        except ValueError:
            output = "Enter a NUMBER for weight and height!"

    output_label.config(text=output)
    output_bmi.config(text=output_2)

press_button = tkinter.Button(text="Press for your BMI", command=button)
output_label = tkinter.Label(text="")
output_bmi = tkinter.Label(text="")

we_label.pack()
we_entry.pack()
he_label.pack()
he_entry.pack()
press_button.pack()
output_label.pack()
output_bmi.pack()



wn.mainloop()