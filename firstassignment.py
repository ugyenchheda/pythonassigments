from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkcalendar import Calendar
from tkinter.messagebox import showerror
from PIL import Image, ImageTk
import os

theme_color1 = "blue"
theme_color2 = "#3b474d"
theme_header = "#a9d2fe"
theme_color3 = "black"
theme_color4 = "white"
theme_color5 = "#3b474d"
theme_danger = "red"
transparent_theme = "FF0000AA"

window = Tk()
window.geometry('368x420')
window.title("Ugyen's Assignment")
window.configure(bg=theme_color4)
window.resizable(height=FALSE, width=FALSE)

top = Frame(window, width=368, height=100, bg=theme_color3)
top.grid(row=0, column=0)

main = Frame(window, width=368, height=300, bg=theme_color4)
main.grid(row=1, column=0)

script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, "images", "homelogin2.png")
image = Image.open(image_path)
new_size = (200, 200)
resized_image = image.resize(new_size)

top_background_image = Image.open(image_path)  
top_background_photo = ImageTk.PhotoImage(top_background_image)

top_background_label = Label(top, image=top_background_photo)
top_background_label.place(x=0, y=0, relwidth=1, relheight=1)

welcome = Label(main, text="Welcome", width=21, height=2, pady=10, anchor=CENTER, font=('Helvetica 16 bold'), bg=theme_color4, fg=theme_color3)
welcome.place(x=44, y=5)

login_text = Label(main, text="Login to Proceed", width=21, padx=4, anchor=CENTER, font=('Helvetica 11'), bg=theme_color4, fg=theme_color3)
login_text.place(x=80, y=55)

username_text = Label(main, text="Username:", width=21, padx=4, anchor=CENTER, font=('Helvetica 11'), bg=theme_color4, fg=theme_color3)
username_text.place(x=20, y=95)
username = ttk.Entry(main, width=21, justify=LEFT, font=("Helvetica 12"))
username.place(x=80, y=120)

Password_text = Label(main, text="Password:", width=21, padx=4, anchor=CENTER, font=('Helvetica 11'), bg=theme_color4, fg=theme_color3)
Password_text.place(x=20, y=150)
Password = ttk.Entry(main, width=21, justify=LEFT, font=("Helvetica 12"))
Password.place(x=80, y=175)

def user_dashboard():
    global global_username  
    user_name = "Ugyen"
    password = "a"
    username_entered = username.get()
    password_entered = Password.get()
    if not username_entered or not password_entered:
        showerror("Error", "Both Username and Password are required.")
        return

    if user_name != username_entered:
        showerror("Error", "User does not exist.")
        return
    if password_entered != password:
        showerror("Error", "Incorrect Password.")
        return

    global_username = username_entered
    notes_view()

note_date = None
note_subject = None
new_notes = None
notes_list = []

def get_selected_date(cal):
    global note_date 
    selected_date = cal.get_date()
    if note_date:
        note_date.delete("1.0", tk.END) 
        note_date.insert("1.0", selected_date) 
        cal.master.destroy()

def show_calendar(event):
    calendar_window = tk.Toplevel(window)
    calendar_window.title("Select Date")

    cal = Calendar(calendar_window, selectmode="day", year=2023, month=9, day=24)
    cal.pack()

    get_date_button = tk.Button(calendar_window, text="Get Selected Date", command=lambda: get_selected_date(cal))
    get_date_button.pack()

def create_note():
    global note_date
    global note_subject
    global new_notes
    global global_username

    create_view = Frame(window, width=368, height=300, bg=theme_color4)
    create_view.grid(row=1, column=0)

    note_view_text = Label(create_view, text=f"Create Notes for {global_username}", width=21, padx=4, anchor=CENTER, font=('Helvetica 12'), bg=theme_color4, fg=theme_color3)
    note_view_text.place(x=80, y=10) 

    date_label = tk.Label(create_view, text="Date: ", font=('Helvetica 12'), bg=theme_color4, fg=theme_color3)
    date_label.place(x=5, y=50)
    
    note_date = tk.Text(create_view, font=("Helvetica 12"), height=1, width=31, highlightbackground="grey", highlightthickness=1)
    note_date.place(x=75, y=50)
    note_date.bind("<Button-1>", show_calendar)
    
    note_subject_label = Label(create_view, text="Subject:", width=21, padx=4, anchor='w', font=('Helvetica 10'), bg=theme_color4, fg=theme_color3)
    note_subject_label.place(x=5, y=80)

    note_subject = tk.Text(create_view,  font=("Helvetica 12"), height=1, width=31, highlightbackground="grey", highlightthickness=1)
    note_subject.place(x=75, y=80)
    
    new_notes_label = Label(create_view, text="Add Notes:", width=21, padx=4, anchor='w', font=('Helvetica 10'), bg=theme_color4, fg=theme_color3)
    new_notes_label.place(x=5, y=110)
    
    new_notes = tk.Text(create_view,  font=("Helvetica 12"), height=4, width=31, highlightbackground="grey", highlightthickness=1)
    new_notes.place(x=75, y=110)
    
    button_create =tk.Button(create_view, text="Save", width=15, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12, "bold"), justify=CENTER, command=save_note)
    button_create.place(x=10, y=230)
    
    button_cancel =tk.Button(create_view, text="Cancel", width=15, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12, "bold"), justify=CENTER,command=user_dashboard)
    button_cancel.place(x=182, y=230)
    
    copy_right = Label(create_view, text="© 2023 Ugyen. All rights reserved.", width=42, padx=4, anchor=CENTER, font=('Helvetica 9'), bg=theme_color4, fg=theme_color3)
    copy_right.place(x=25, y=280)

def save_note():    
    global note_date
    global note_subject
    global new_notes
    global notes_list
    note_content = new_notes.get("1.0", "end-1c")

    if not note_date.get("1.0", "end-1c"):
        showerror("Error", "Please select a date.")
        return
    
    if not note_subject.get("1.0", "end-1c"):
        showerror("Error", "Please enter subject.")
        return     
    
    if not note_content:
        showerror("Error", "Please enter notes content.")
        return 
    
    notes_list.append({"Date": note_date.get("1.0", "end-1c"), "Subject": note_subject.get("1.0", "end-1c"), "Notes": note_content})

    note_date.delete("1.0", tk.END)
    note_subject.delete("1.0", tk.END)
    new_notes.delete("1.0", tk.END)

    create_view = Frame(window, width=368, height=300, bg=theme_color4)
    create_view.grid(row=1, column=0)

    new_notes = tk.Label(create_view, text="Notes Saved",  font=("Helvetica 12"), height=6, width=38, highlightbackground="grey", highlightthickness=1)
    new_notes.place(x=10, y=80)

    button_create =tk.Button(create_view, text="Add Another", width=15, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12, "bold"), justify=CENTER, command=create_note)
    button_create.place(x=10, y=230)
    
    button_cancel =tk.Button(create_view, text="Dashboard", width=15, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12, "bold"), justify=CENTER,command=user_dashboard)
    button_cancel.place(x=182, y=230)
    
    copy_right = tk.Label(create_view, text="© 2023 Ugyen. All rights reserved.", width=42, padx=4, anchor=CENTER, font=('Helvetica 9'), bg=theme_color4, fg=theme_color3)
    copy_right.place(x=25, y=280)

def logout():
    option_view = Frame(window, width=368, height=300, bg=theme_color4)
    option_view.grid(row=1, column=0)

    note_view_text = Label(option_view, text="Log Out", width=21, padx=4, anchor=CENTER, font=('Helvetica 12'), bg=theme_color4, fg=theme_color3)
    note_view_text.place(x=80, y=40)
    
    new_notes = ttk.Entry(option_view,  font=("Helvetica 12"), width=30)
    new_notes.place(x=10, y=80)

def all_note_lists():
    option_view = Frame(window, width=368, height=300, bg=theme_color4)
    option_view.grid(row=1, column=0)

    note_view_text = Label(option_view, text="My Notes", width=21, padx=4, anchor=CENTER, font=('Helvetica 16 bold'), bg=theme_color4, fg=theme_color3)
    note_view_text.place(x=40, y=30)   

    if not notes_list:
        no_notes_label = Label(option_view, text="No note has been added yet.", font=("Helvetica", 12, "bold"), bg=theme_color4, fg=theme_danger)
        no_notes_label.place(x=80, y=110) 

        button_create =tk.Button(option_view, text="Add", width=15, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12, "bold"), justify=CENTER, command=create_note)
        button_create.place(x=10, y=230)
        
        button_cancel =tk.Button(option_view, text="Cancel", width=15, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12, "bold"), justify=CENTER,command=user_dashboard)
        button_cancel.place(x=182, y=230)
    else:
        note_position = 80
        note_number = 1
        for note in notes_list:
            note_title = note[:25]
            notes_label = tk.Label(option_view, text=f"{note_number}) {note_title}", font=("Helvetica", 12), bg=theme_color4, fg=theme_color3)
            notes_label.place(x=10, y=note_position)
            notes_label.bind("<Button-1>", lambda event, content=note: display_full_note(content))
            note_position += 30
            note_number += 1

            button_cancel =tk.Button(option_view, text="Go to Dashboard", width=15, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12, "bold"), justify=CENTER,command=user_dashboard)
            button_cancel.place(x=98, y=230)   
 
    copy_right = Label(option_view, text="© 2023 Ugyen. All rights reserved.", width=42, padx=4, anchor=CENTER, font=('Helvetica 9'), bg=theme_color4, fg=theme_color3)
    copy_right.place(x=25, y=280)

def display_full_note(note_content):
    note_view = Frame(window, width=368, height=300, bg=theme_color4)
    note_view.grid(row=1, column=0)

    note_view_text = Label(note_view, text="Single Note Page", width=21, padx=4, anchor=CENTER, font=('Helvetica 14 bold'), bg=theme_color4, fg=theme_color3)
    note_view_text.place(x=40, y=30)   

    note_text = tk.Label(note_view, text=note_content, wraplength=300, font=('Helvetica 12'), bg=theme_color4)
    note_text.place(x=10, y=80)
    
    button_edit =tk.Button(note_view, text="Edit", width=10, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12, "bold"), justify=CENTER, command='')
    button_edit.place(x=10, y=230)
    
    button_delete =tk.Button(note_view, text="Delete", width=10, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12, "bold"), justify=CENTER,command='')
    button_delete.place(x=120, y=230)
    
    button_done =tk.Button(note_view, text="Done", width=10, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12, "bold"), justify=CENTER,command=user_dashboard)
    button_done.place(x=230, y=230)
    
    copy_right = Label(note_view, text="© 2023 Ugyen. All rights reserved.", width=42, padx=4, anchor=CENTER, font=('Helvetica 9'), bg=theme_color4, fg=theme_color3)
    copy_right.place(x=25, y=280)

def notes_view():
    option_view = Frame(window, width=368, height=300, bg=theme_color4)
    option_view.grid(row=1, column=0)

    note_view_text = Label(option_view, text="Choose Option", width=21, padx=4, anchor=CENTER, font=('Helvetica 12'), bg=theme_color4, fg=theme_color3)
    note_view_text.place(x=80, y=40)

    button =Button(option_view, text="1. Create a note", padx=5, justify=LEFT, height=1, bg=theme_color4,borderwidth=0, font=("Helvetica 11"), command=create_note)
    button.place(x=50, y=90)

    button =Button(option_view, text="2. Retrieve a note", padx=5, justify=LEFT, height=1, bg=theme_color4,borderwidth=0, font=("Helvetica 11"), command=all_note_lists)
    button.place(x=50, y=130)

    button =Button(option_view, text="3. Logout", padx=5, height=1, justify=LEFT, bg=theme_color4,borderwidth=0, font=("Helvetica 11"))
    button.place(x=50, y=170)

    copy_right = Label(option_view, text="© 2023 Ugyen. All rights reserved.", width=42, padx=4, anchor=CENTER, font=('Helvetica 9'), bg=theme_color4, fg=theme_color3)
    copy_right.place(x=25, y=280)

button =Button(main, text="Continue", width=25, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica 12 bold"), justify=CENTER,command=user_dashboard)
button.place(x=50, y=230)
copy_right = Label(main, text="© 2023 Ugyen. All rights reserved.", width=42, padx=4, anchor=CENTER, font=('Helvetica 9'), bg=theme_color4, fg=theme_color3)
copy_right.place(x=25, y=280)



window.mainloop()
