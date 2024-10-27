from tkinter import *
from tkinter import messagebox

input = Tk()
input.geometry("600x500")

Label(input, text="Registration Form", font=("Arial", 20)).place(x=200, y=20)

user_name = Label(input, text="Full Name")
user_name.place(x=200, y=70)

age = Label(input, text="Age")
age.place(x=200, y=130)

address = Label(input, text="Address")
address.place(x=200, y=185)

e_name = Entry(input)
e_name.place(x=400, y=70)

e_age = Entry(input)
e_age.place(x=400, y=130)

e_address = Text(input, height=5, width=20)
e_address.place(x=400, y=185)


def on_submit():
    data = (
        f"Name: {e_name.get()} \n"
        f"Age: {e_age.get()} \n"
        f"Address: {e_address.get('1.0', END).strip()}"
    )
    messagebox.showinfo("Registration Details", data)
    e_name.delete(0, END)
    e_age.delete(0, END)
    e_address.delete("1.0", END)


submit_button = Button(input, text="Submit", bg="Black", fg="White", command=on_submit)
submit_button.place(x=265, y=350, width=100, height=30)

mainloop()
