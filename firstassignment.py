import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.messagebox import showerror, showinfo

from PIL import Image, ImageTk

theme_color1 = "blue"
theme_color2 = "red"
theme_header = "green"
theme_color3 = "black"
theme_color4 = "white"
theme_color5 = "lightblue"
theme_danger = "red"
transparent_theme = "grey"

window = Tk()
window.geometry("368x420")
window.title("Ugyen's First Assignment")
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

users = {"Ugyen": "a", "user1": "pass1", "user2": "pass2", "user3": "pass3"}
current_user = None


def login_page():
    global current_user
    global username
    global Password
    current_user = None
    global main  
    if main:
        main.destroy() 

    main = Frame(window, width=368, height=300, bg=theme_color4)
    main.grid(row=1, column=0)
    welcome = Label(
        main,
        text="Welcome",
        width=21,
        height=2,
        pady=10,
        anchor=CENTER,
        font=("Helvetica 16 bold"),
        bg=theme_color4,
        fg=theme_color3,
    )
    welcome.place(x=44, y=5)

    login_text = Label(
        main,
        text="Login to Proceed",
        width=21,
        padx=4,
        anchor=CENTER,
        font=("Helvetica 11"),
        bg=theme_color4,
        fg=theme_color3,
    )
    login_text.place(x=80, y=55)

    username_text = Label(
        main,
        text="Username:",
        width=21,
        padx=4,
        anchor=CENTER,
        font=("Helvetica 11"),
        bg=theme_color4,
        fg=theme_color3,
    )
    username_text.place(x=20, y=95)
    username = ttk.Entry(main, width=21, justify=LEFT, font=("Helvetica 12"))
    username.place(x=80, y=120)

    Password_text = Label(
        main,
        text="Password:",
        width=21,
        padx=4,
        anchor=CENTER,
        font=("Helvetica 11"),
        bg=theme_color4,
        fg=theme_color3,
    )
    Password_text.place(x=20, y=150)
    Password = ttk.Entry(main, width=21, justify=LEFT, font=("Helvetica 12"))
    Password.place(x=80, y=175)

    button = Button(
        main,
        text="Continue",
        width=25,
        padx=5,
        height=1,
        bg=theme_color3,
        fg=theme_color4,
        font=("Helvetica 12 bold"),
        justify=CENTER,
        command=user_authentication,
    )
    button.place(x=50, y=230)

    copy_right = Label(
        main,
        text="© 2023 Ugyen. All rights reserved.",
        width=42,
        padx=4,
        anchor=CENTER,
        font=("Helvetica 9"),
        bg=theme_color4,
        fg=theme_color3,
    )
    copy_right.place(x=25, y=280)


def user_authentication():
    global current_user
    global username
    global Password

    username_entered = username.get()
    password_entered = Password.get()

    if not username_entered or not password_entered:
        showerror("Error", "Both Username and Password are required.")
        return

    if username_entered not in users:
        showerror("Error", "User does not exist.")
        return

    if users[username_entered] != password_entered:
        showerror("Error", "Incorrect Password.")
        return

    current_user = username_entered
    dashboard()


def dashboard():
    global main
    if main:
        main.destroy()
    option_view = Frame(window, width=368, height=300, bg=theme_color4)
    option_view.grid(row=1, column=0)

    note_view_text = Label(
        option_view,
        text="Choose Option",
        width=21,
        padx=4,
        anchor=CENTER,
        font=("Helvetica 12"),
        bg=theme_color4,
        fg=theme_color3,
    )
    note_view_text.place(x=80, y=40)

    button = Button(
        option_view,
        text="1. Create a note",
        padx=5,
        justify=LEFT,
        height=1,
        bg=theme_color4,
        borderwidth=0,
        font=("Helvetica 11"),
        command=create_note,
    )
    button.place(x=50, y=90)

    button = Button(
        option_view,
        text="2. Find a note",
        padx=5,
        justify=LEFT,
        height=1,
        bg=theme_color4,
        borderwidth=0,
        font=("Helvetica 11"),
        command=retrieve_note,
    )
    button.place(x=50, y=130)

    button = Button(
        option_view,
        text="3. Show all notes",
        padx=5,
        justify=LEFT,
        height=1,
        bg=theme_color4,
        borderwidth=0,
        font=("Helvetica 11"),
        command=all_note_lists,
    )
    button.place(x=50, y=170)

    button_log_out = tk.Button( option_view, text="4. Log Out", width=10, padx=5, height=1, bg=theme_color4, borderwidth=0, font=("Helvetica 11"),
        justify=CENTER, command=log_out, )
    button_log_out.place(x=50, y=230)

    copy_right = Label( option_view, text="© 2023 Ugyen. All rights reserved.", width=42, padx=4, anchor=CENTER, font=("Helvetica 9"), bg=theme_color4,
        fg=theme_color3,
    )
    copy_right.place(x=25, y=280)


note_date = None
note_subject = None
new_notes = None
user_notes = {
    "Ugyen": [
        {
            "Date": "2023-09-28",
            "Subject": "Complete IOT Assignment",
            "Notes": "Fourth lab needs to be written by ugyen..",
        },
        {
            "Date": "2023-10-28",
            "Subject": "Helsinki",
            "Notes": "Go to Helsinki for some good time.",
        },
        {
            "Date": "2023-10-25",
            "Subject": "Helsinki",
            "Notes": "papaya is taste in Helsinki.",
        },
    ],
    "user1": [
        {
            "Date": "2023-10-28",
            "Subject": "Meeting Notes",
            "Notes": "Meeting with the team to discuss project updates.",
        },
        {
            "Date": "2023-10-02",
            "Subject": "To-Do List",
            "Notes": "1. Complete the report\n2. Send out the invoices",
        },
        {
            "Date": "2023-09-29",
            "Subject": "Python homework",
            "Notes": "1. Complete the report\n2. Send out the invoices",
        },
        {
            "Date": "2023-09-30",
            "Subject": "Gym",
            "Notes": "1. Complete the report\n2. Send out the invoices",
        },
        {
            "Date": "2023-10-29",
            "Subject": "Another one",
            "Notes": "1. Complete the report\n2. Send out the invoices",
        },
    ],
    "user2": [
        {
            "Date": "2023-09-30",
            "Subject": "Ideas",
            "Notes": "Brainstorming session:\n- New product ideas\n- Marketing strategies",
        }
    ],
    "user3": [],
}
keyword = None
current_note_index = None


def all_note_lists():
    global current_user
    option_view = Frame(window, width=368, height=300, bg=theme_color4)
    option_view.grid(row=1, column=0)
    if current_user not in user_notes or not user_notes[current_user]:
        showinfo("Info", "No notes found for this user.")
        return

    note_view = Frame(window, width=368, height=300, bg=theme_color4)
    note_view.grid(row=1, column=0)

    note_view_text = Label(
        note_view,
        text=f"All Notes for {current_user}",
        width=21,
        padx=4,
        anchor=CENTER,
        font=("Helvetica 16 bold"),
        bg=theme_color4,
        fg=theme_color3,
    )
    note_view_text.place(x=40, y=30)

    note_position = 80
    note_number = 1
    for note_index, note in enumerate(user_notes[current_user]):
        subject = note["Subject"][:25]
        notes_label = tk.Label(
            note_view,
            text=f"{note_number}) {subject}",
            font=("Helvetica", 12),
            bg=theme_color4,
            fg=theme_color3,
        )
        notes_label.place(x=10, y=note_position)
        notes_label.bind(
            "<Button-1>",
            lambda event, index=note_index: display_full_note(
                index, note["Date"], note["Subject"], note["Notes"]
            ),
        )
        note_position += 30
        note_number += 1

    button_cancel = tk.Button(
        note_view,
        text="Go to Dashboard",
        width=15,
        padx=5,
        height=1,
        bg=theme_color2,
        fg=theme_color4,
        font=("Helvetica", 12, "bold"),
        justify=CENTER,
        command=dashboard,
    )
    button_cancel.place(x=98, y=230)

    copy_right = Label(
        note_view,
        text="© 2023 Ugyen. All rights reserved.",
        width=42,
        padx=4,
        anchor=CENTER,
        font=("Helvetica 9"),
        bg=theme_color4,
        fg=theme_color3,
    )
    copy_right.place(x=25, y=280)

    button_show_all_notes = Button(
        option_view,
        text="5. Show All Notes",
        padx=5,
        justify=LEFT,
        height=1,
        bg=theme_color4,
        borderwidth=0,
        font=("Helvetica 11"),
        command=all_note_lists,
    )
    button_show_all_notes.place(x=50, y=250)


def create_note():
    global note_date
    global note_subject
    global new_notes

    create_view = Frame(window, width=368, height=300, bg=theme_color4)
    create_view.grid(row=1, column=0)

    note_view_text = Label(
        create_view,
        text=f"Create Notes for {current_user}",
        width=21,
        padx=4,
        anchor=CENTER,
        font=("Helvetica 12"),
        bg=theme_color4,
        fg=theme_color3,
    )
    note_view_text.place(x=80, y=10)

    date_label = tk.Label(
        create_view,
        text="Date: ",
        font=("Helvetica 12"),
        bg=theme_color4,
        fg=theme_color3,
    )
    date_label.place(x=5, y=50)

    note_date = tk.Text(
        create_view,
        font=("Helvetica 12"),
        height=1,
        width=31,
        highlightbackground="grey",
        highlightthickness=1,
    )
    note_date.place(x=60, y=50)

    subject_label = tk.Label(
        create_view,
        text="Subject: ",
        font=("Helvetica 12"),
        bg=theme_color4,
        fg=theme_color3,
    )
    subject_label.place(x=5, y=80)

    note_subject = tk.Text(
        create_view,
        font=("Helvetica 12"),
        height=1,
        width=31,
        highlightbackground="grey",
        highlightthickness=1,
    )
    note_subject.place(x=80, y=80)

    notes_label = tk.Label(
        create_view,
        text="Notes: ",
        font=("Helvetica 12"),
        bg=theme_color4,
        fg=theme_color3,
    )
    notes_label.place(x=5, y=110)

    new_notes = tk.Text(
        create_view,
        font=("Helvetica 12"),
        height=8,
        width=31,
        highlightbackground="grey",
        highlightthickness=1,
    )
    new_notes.place(x=60, y=110)

    button = Button(
        create_view,
        text="Save",
        padx=5,
        height=1,
        justify=LEFT,
        bg=theme_color2,
        borderwidth=0,
        font=("Helvetica 11"),
        command=save_note,
    )
    button.place(x=120, y=250)

    button = Button(
        create_view,
        text="Back to Dashboard",
        padx=5,
        height=1,
        justify=LEFT,
        bg=theme_color4,
        borderwidth=0,
        font=("Helvetica 11"),
        command=dashboard,
    )
    button.place(x=190, y=250)


def save_note():
    global note_date
    global note_subject
    global new_notes
    global user_notes

    date = note_date.get("1.0", END).strip()
    subject = note_subject.get("1.0", END).strip()
    notes = new_notes.get("1.0", END).strip()

    if not date or not subject or not notes:
        showerror("Error", "Date, Subject, and Notes are required.")
        return

    if current_user not in user_notes:
        user_notes[current_user] = []

    user_notes[current_user].append({"Date": date, "Subject": subject, "Notes": notes})
    showinfo("Success", "Note has been saved successfully!")

    note_date.delete("1.0", END)
    note_subject.delete("1.0", END)
    new_notes.delete("1.0", END)


def retrieve_note():
    global keyword

    retrieve_view = Frame(window, width=368, height=300, bg=theme_color4)
    retrieve_view.grid(row=1, column=0)

    note_view_text = Label(
        retrieve_view,
        text=f"Retrieve Notes for {current_user}",
        width=21,
        padx=4,
        anchor=CENTER,
        font=("Helvetica 12"),
        bg=theme_color4,
        fg=theme_color3,
    )
    note_view_text.place(x=80, y=10)

    keyword_label = tk.Label(
        retrieve_view,
        text="Search by Subject: ",
        font=("Helvetica 12"),
        bg=theme_color4,
        fg=theme_color3,
    )
    keyword_label.place(x=5, y=50)

    keyword = tk.Entry(
        retrieve_view,
        font=("Helvetica 12"),
        width=31,
        highlightbackground="grey",
        highlightthickness=1,
    )
    keyword.place(x=170, y=50)

    button = Button(
        retrieve_view,
        text="Search",
        padx=5,
        height=1,
        justify=LEFT,
        bg=theme_color2,
        borderwidth=0,
        font=("Helvetica 11"),
        command=search_by_subject,
    )
    button.place(x=120, y=90)

    button = Button(
        retrieve_view,
        text="Back to Dashboard",
        padx=5,
        height=1,
        justify=LEFT,
        bg=theme_color4,
        borderwidth=0,
        font=("Helvetica 11"),
        command=dashboard,
    )
    button.place(x=190, y=90)


def search_by_subject():
    global keyword, matching_notes  # Make matching_notes global

    keyword_text = keyword.get()

    if not keyword_text:
        showerror("Error", "Please enter a keyword to search.")
        return

    if current_user not in user_notes:
        showinfo("Info", "No notes found for this user.")
        return

    matching_notes = []
    for index, note in enumerate(user_notes[current_user]):
        if keyword_text.lower() in note["Subject"].lower():
            matching_notes.append((index, note))

    if not matching_notes:
        showinfo("Info", "No matching notes found.")
        return

    global current_note_index
    current_note_index = 0
    display_note_details(matching_notes)


def display_note_details(matching_notes):
    global current_note_index

    retrieve_view = Frame(window, width=368, height=300, bg=theme_color4)
    retrieve_view.grid(row=1, column=0)

    note_view_text = Label(
        retrieve_view,
        text=f"Retrieve Notes for {current_user}",
        width=21,
        padx=4,
        anchor=CENTER,
        font=("Helvetica 12"),
        bg=theme_color4,
        fg=theme_color3,
    )
    note_view_text.place(x=80, y=10)

    note_details = matching_notes[current_note_index][1]

    date_label = tk.Label(
        retrieve_view,
        text="Date: ",
        font=("Helvetica 12"),
        bg=theme_color4,
        fg=theme_color3,
    )
    date_label.place(x=5, y=50)

    date = note_details["Date"]
    date_text = tk.Label(
        retrieve_view,
        text=date,
        font=("Helvetica 12"),
        bg=theme_color4,
        fg=theme_color3,
    )
    date_text.place(x=80, y=50)

    subject_label = tk.Label(
        retrieve_view,
        text="Subject: ",
        font=("Helvetica 12"),
        bg=theme_color4,
        fg=theme_color3,
    )
    subject_label.place(x=5, y=80)

    subject = note_details["Subject"]
    subject_text = tk.Label(
        retrieve_view,
        text=subject,
        font=("Helvetica 12"),
        bg=theme_color4,
        fg=theme_color3,
    )
    subject_text.place(x=80, y=80)

    notes_label = tk.Label(
        retrieve_view,
        text="Notes: ",
        font=("Helvetica 12"),
        bg=theme_color4,
        fg=theme_color3,
    )
    notes_label.place(x=5, y=110)

    notes = note_details["Notes"]
    notes_text = tk.Label(
        retrieve_view,
        text=notes,
        font=("Helvetica 12"),
        bg=theme_color4,
        fg=theme_color3,
        wraplength=300,
        justify=LEFT,
        anchor=NW,
    )
    notes_text.place(x=80, y=110)

    prev_button = Button(
        retrieve_view,
        text="Previous",
        padx=5,
        height=1,
        justify=LEFT,
        bg=theme_color4,
        borderwidth=0,
        font=("Helvetica 11"),
        command=prev_note,
    )
    prev_button.place(x=50, y=250)

    next_button = Button(retrieve_view,text="Next",padx=5,
        height=1,
        justify=LEFT,
        bg=theme_color4,
        borderwidth=0,
        font=("Helvetica 11"),
        command=next_note,
    )
    next_button.place(x=200, y=250)

    back_button = Button( retrieve_view,text="Back to Dashboard",padx=5,height=1,justify=LEFT,bg=theme_color4,borderwidth=0,font=("Helvetica 11"),
        command=dashboard,
    )
    back_button.place(x=125, y=280)


def edit_note():
    global current_user, current_note_index

    if current_user not in user_notes:
        showerror("Error", "User not found in user_notes.")
        return

    user_notes_list = user_notes[current_user]

    if 0 <= current_note_index < len(user_notes_list):
        note_edit_window = tk.Toplevel(window)
        note_edit_window.title("Edit Note")
        note_edit_window.configure(bg=theme_color4)

        current_note = user_notes_list[current_note_index]
        current_date = current_note["Date"]
        current_subject = current_note["Subject"]
        current_content = current_note["Notes"]

        date_label = tk.Label(note_edit_window, text="Date:")
        date_label.pack()
        date_entry = tk.Entry(note_edit_window)
        date_entry.insert(0, current_date)
        date_entry.pack()

        subject_label = tk.Label(note_edit_window, text="Subject:")
        subject_label.pack()
        subject_entry = tk.Entry(note_edit_window)
        subject_entry.insert(0, current_subject)
        subject_entry.pack()

        content_label = tk.Label(note_edit_window, text="Content:")
        content_label.pack()
        content_text = tk.Text(note_edit_window, wrap=tk.WORD, height=10, width=40)
        content_text.insert(tk.END, current_content)
        content_text.pack()

        def save_edited_note():
            global current_note_index

            if 0 <= current_note_index < len(user_notes_list):
                new_date = date_entry.get()
                new_subject = subject_entry.get()
                new_content = content_text.get("1.0", tk.END)

                user_notes_list[current_note_index]["Date"] = new_date
                user_notes_list[current_note_index]["Subject"] = new_subject
                user_notes_list[current_note_index]["Notes"] = new_content

                note_edit_window.destroy()
                all_note_lists()
                messagebox.showinfo(
                    "Note Saved", "Your edited note has been saved successfully!"
                )
            else:
                showerror("Error", "Invalid note index.")

        save_button = tk.Button(
            note_edit_window,
            text="Save",
            padx=5,
            height=1,
            justify=LEFT,
            bg=theme_color5,
            fg=theme_color4,
            borderwidth=0,
            font=("Helvetica 11"),
            command=save_edited_note,
        )
        save_button.pack()


def display_full_note(note_index, note_date, note_subject, note_content):
    global current_user, current_note_index
    current_note_index = note_index

    note_view = Frame(window, width=368, height=300, bg=theme_color4)
    note_view.grid(row=1, column=0)

    note_view_text = Label(
        note_view,
        text="Single Note Page",
        width=21,
        padx=4,
        anchor=CENTER,
        font=("Helvetica 14 bold"),
        bg=theme_color4,
        fg=theme_color3,
    )
    note_view_text.place(x=40, y=30)

    date_label = tk.Label(
        note_view, text="Date: ", font=("Helvetica 12"), bg=theme_color4
    )
    date_label.place(x=10, y=80)

    date_value = tk.Label(
        note_view,
        text=note_date,
        wraplength=300,
        font=("Helvetica 12"),
        bg=theme_color4,
    )
    date_value.place(x=70, y=80)

    subject_label = tk.Label(
        note_view, text="Subject: ", font=("Helvetica 12"), bg=theme_color4
    )
    subject_label.place(x=10, y=105)

    subject_value = tk.Label(
        note_view,
        text=note_subject,
        wraplength=300,
        font=("Helvetica 12"),
        bg=theme_color4,
    )
    subject_value.place(x=70, y=105)

    note_label = tk.Label(
        note_view, text="Note: ", font=("Helvetica 12"), bg=theme_color4
    )
    note_label.place(x=10, y=130)

    note_value = tk.Label(
        note_view,
        text=note_content,
        wraplength=250,
        anchor="w",
        font=("Helvetica 12"),
        bg=theme_color4,
    )
    note_value.place(x=70, y=130)

    button_edit = tk.Button(
        note_view,
        text="Edit",
        width=10,
        padx=5,
        height=1,
        bg=theme_color2,
        fg=theme_color4,
        font=("Helvetica", 12, "bold"),
        justify=CENTER,
        command=edit_note,
    )
    button_edit.place(x=10, y=230)

    def delete_current_note():
        global current_note_index
        if 0 <= current_note_index < len(user_notes[current_user]):
            user_notes[current_user].pop(current_note_index)
            all_note_lists()
            messagebox.showinfo("Note Deleted", "Notes deleted successfully!")

    button_delete = tk.Button(
        note_view,
        text="Delete",
        width=10,
        padx=5,
        height=1,
        bg=theme_color2,
        fg=theme_color4,
        font=("Helvetica", 12, "bold"),
        justify=CENTER,
        command=delete_current_note,
    )
    button_delete.place(x=120, y=230)

    button_log_out = tk.Button(
        note_view,
        text="Cancel",
        width=10,
        padx=5,
        height=1,
        bg=theme_color2,
        fg=theme_color4,
        font=("Helvetica", 12, "bold"),
        justify=CENTER,
        command=dashboard,
    )
    button_log_out.place(x=230, y=230)

    copy_right = Label(
        note_view,
        text="© 2023 Ugyen. All rights reserved.",
        width=42,
        padx=4,
        anchor=CENTER,
        font=("Helvetica 9"),
        bg=theme_color4,
        fg=theme_color3,
    )
    copy_right.place(x=25, y=280)


def prev_note():
    global current_note_index
    if current_note_index > 0:
        current_note_index -= 1
        display_note_details(matching_notes)


def next_note():
    global current_note_index
    if current_note_index < len(matching_notes) - 1:
        current_note_index += 1
        display_note_details(matching_notes)


def log_out():
    global current_user
    current_user = None
    main.destroy()  # Destroy the 'main' frame
    login_page()  # Navigate back to the login page


login_page()
window.mainloop()
