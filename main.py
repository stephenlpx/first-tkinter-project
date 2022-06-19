from tkinter import *


#UI setup
window = Tk()
window.title("My First GUI Program")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

#gets the miles input and converts to km and replaces label with answwer
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.69
    km_result_label["text"] = f"{km}"


#inputs
miles_input = Entry(width=5)
miles_input.grid(column=3, row=1)

#labels
miles_label = Label(text="Miles")
miles_label.grid(column=5, row= 1)
equal_label = Label(text="is equal to: ")
equal_label.grid(column=1, row=4)
km_result_label = Label(text="0")
km_result_label.grid(column=3, row=4)
km_label = Label(text="km")
km_label.grid(column=5, row=4)

#buttons
calculate_btn = Button(text="Calculate", command=miles_to_km)
calculate_btn.grid(column=3, row=9)



window.mainloop()