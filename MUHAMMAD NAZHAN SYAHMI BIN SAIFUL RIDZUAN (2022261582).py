import tkinter
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

#Connect ke database
mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hotel"
)
mycursor= mydb.cursor()

# TERMINAL INFO #

def enter_data():
    #  put the info in terminal #
    first_name_label=first_name_entry.get()
    print("first name:", first_name_label)

    last_name_label=last_name_entry.get()
    print("last name:", last_name_label)

    contact_label=contact_entry.get()
    print("contact:",contact_label)

    room=room_spinbox.get()
    print("room:", room)

    email=reg_status_var.get()
    print("email status:", email)

    checkin_label=checkin_spinbox.get()
    print("check in date:", checkin_label)

    checkout_label=checkout_spinbox.get()
    print("check out date:", checkout_label)

    terms_check=accept_var.get()
    print("terms and condition:", terms_check)

    accepted = accept_var.get()

    if accepted=="Accepted":
        # User info #
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            contact = contact_entry.get()
            room = room_spinbox.get()
        

            # Registration info #
            email = reg_status_var.get()
            checkin = checkin_spinbox.get()
            checkout = checkout_spinbox.get()

            print("First name: ", firstname, "Last name: ", lastname)
            print("Contact: ", contact, "Room: ", room)
            print("# Check in date: ", checkin , "# Check out date: ", checkout)
            print("Email status", email)
            print("------------------------------------------")
        else:
            tkinter.messagebox.showwarning(contact="Error", message="First name and last name are required.")
    else:
        tkinter.messagebox.showwarning(contact= "Error", message="You have not accepted the terms")
    
    #Inserting data into a table
    sql = "INSERT INTO hotel (first_name_label, last_name_label, contact_label, room, email, checkin_label, checkout_label, terms_check) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (first_name_label, last_name_label, contact_label, room, email, checkin_label, checkout_label, terms_check)
    mycursor.execute(sql,val)
    mydb.commit()

root = tkinter.Tk()
root.title("Hotel Room Reservation")

frame = tkinter.Frame(root)
frame.pack()

# Saving User Info
user_info_frame =tkinter.LabelFrame(frame, text="WELCOME TO Skye Service")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

contact_label = tkinter.Label(user_info_frame, text="Contact")
contact_entry = tkinter.Entry(user_info_frame,)
contact_label.grid(row=0, column=2)
contact_entry.grid(row=1, column=2)

room = tkinter.Label(user_info_frame, text="Room")
room_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to=110)
room.grid(row=2, column=0)
room_spinbox.grid(row=3, column=0)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving date info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

email = tkinter.Label(courses_frame, text="Email")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not registered")

email.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

checkin_label = tkinter.Label(courses_frame, text= "# Check in date")
checkin_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
checkin_label.grid(row=0, column=1)
checkin_spinbox.grid(row=1, column=1)

checkout_label = tkinter.Label(courses_frame, text="# Check out date")
checkout_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
checkout_label.grid(row=0, column=2)
checkout_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

root.mainloop()
