from tkinter import *

window = Tk()
window.title("Mile to Kilo Converter")
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(miles_input.get())
    kilo = miles * 1.60934
    kilo_result["text"] = f"{kilo:.2f}"

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="Is equal to")
is_equal_label.grid(column=0, row=1)

kilo_result = Label(text="0")
kilo_result.grid(column=1, row=1)

kilo_label = Label(text="Km")
kilo_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)










window.mainloop()