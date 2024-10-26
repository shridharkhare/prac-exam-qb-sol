from tkinter import *  # Import the Tkinter module and alias it as tk

root = Tk()  # Create the main application window
root.title("Simple Tkinter App")  # Set the title of the window
root.geometry("900x900")

user_name = Label(root, text="Full Name", bg="Black", fg="White")

user_name.place(x=200, y=70)
feedback = Label(root, text="Feedback", bg="Black", fg="White")

feedback.place(x=200, y=130)

e_user_name = Entry(root)
e_user_name.place(x=400, y=70)

e_feedback = Text(root)
e_feedback.place(x=400, y=130)


def on_submit():
    usr_name = e_user_name.get()
    feed_back = e_feedback.get("1.0", END).strip()

    file = open("exp19.txt", "a")
    file.write(f"\n Name: {usr_name} \n Feedback: {feed_back}")
    file.close()

    e_user_name.delete(0, END)
    e_feedback.delete("1.0", END)


submit_button = Button(root, text="Submit", bg="Black", fg="White", command=on_submit)
submit_button.place(x=200, y=190, width=100, height=40)

root.mainloop()
