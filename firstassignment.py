from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkcalendar import Calendar
from tkinter.messagebox import showerror
from PIL import Image, ImageTk
import os
from tkinter import messagebox
from datetime import datetime
from tkinter import filedialog
import json
import sqlite3
import requests

# Connect to SQLite database
conn = sqlite3.connect('notes_database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users ( user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL ) ''')

# cursor.execute('''
#     ALTER TABLE user_notes
# ADD COLUMN url TEXT;''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_notes ( note_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, date TEXT, subject TEXT, notes TEXT, url TEXT,  FOREIGN KEY (user_id) REFERENCES users(user_id) )
''')

conn.commit()

theme_color2 = "#3b474d"
theme_color3 = "black"
theme_color4 = "white"
theme_color5 = "#3b474d"
theme_danger = "red"

window = Tk()
window.geometry('368x420')
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

def create_user():
    # Create a new window for user creation
    user_creation_window = tk.Toplevel(window)
    user_creation_window.title("Create User")

    # Username entry
    username_label = tk.Label(user_creation_window, text="Username:")
    username_label.pack()

    username_entry = ttk.Entry(user_creation_window)
    username_entry.pack()

    # Password entry
    password_label = tk.Label(user_creation_window, text="Password:")
    password_label.pack()

    password_entry = ttk.Entry(user_creation_window, show='*')
    password_entry.pack()

    def save_user():
        new_username = username_entry.get()
        new_password = password_entry.get()

        # Check if username or password is empty
        if not new_username or not new_password:
            messagebox.showerror("Error", "Both username and password are required.")
            return

        try:
            # Connect to the database (replace 'your_database.db' with the actual name of your database file)
            conn = sqlite3.connect('your_database.db')
            cursor = conn.cursor()

            # Insert the new user into the users table
            cursor.execute('''
                INSERT INTO users (username, password)
                VALUES (?, ?)
            ''', (new_username, new_password))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()

            messagebox.showinfo("User Created", "User successfully created.")
            user_creation_window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to create user: {str(e)}")

        user_creation_window.destroy()

    # Button to save user information
    save_button = tk.Button(user_creation_window, text="Save", command=save_user)
    save_button.pack()

    copy_right = tk.Label(user_creation_window, text="© 2023 Ugyen. All rights reserved.", width=42, padx=4, anchor=tk.CENTER, font=('Helvetica 9'), bg=theme_color4, fg=theme_color3)
    copy_right.pack()


    



def show_password():
    Password.config(show='')
    main.after(1000, hide_password)

def hide_password():
    Password.config(show='*')

def login_page():
    global username
    global Password
    global main  
    if main:
        main.destroy()  

    main = Frame(window, width=368, height=300, bg=theme_color4)
    main.grid(row=1, column=0)
    welcome = Label(main, text="Welcome", width=21, height=2, pady=10, anchor=CENTER, font=("Helvetica 16 bold"), bg=theme_color4, fg=theme_color3)
    welcome.place(x=44, y=5)

    login_text = Label( main, text="Login to Proceed", width=21, padx=4, anchor=CENTER, font=("Helvetica 11"), bg=theme_color4, fg=theme_color3, )
    login_text.place(x=80, y=55)

    username_text = Label( main, text="Username:", width=21, padx=4, anchor=CENTER, font=("Helvetica 11"), bg=theme_color4, fg=theme_color3 )
    username_text.place(x=20, y=95)
    username = ttk.Entry(main, width=21, justify=LEFT, font=("Helvetica 12"))
    username.place(x=80, y=120)

    Password_text = tk.Label(main, text="Password:", width=21, padx=4, anchor=tk.CENTER, font=("Helvetica 11"), bg=theme_color4, fg=theme_color3)
    Password_text.place(x=20, y=150)

    password_var = tk.StringVar()

    Password = ttk.Entry(main, width=21, justify=tk.LEFT, font=("Helvetica 12"), show='*') 
    Password.place(x=80, y=175)

    register_button = ttk.Button(main, text="Create User", command=create_user)
    register_button.place(x=80, y=203)

    show_button = ttk.Button(main, text="Show Password", command=show_password)
    show_button.place(x=182, y=203)

    button = Button( main,text="Continue", width=25, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica 12"), justify=CENTER, command=user_authentication)
    button.place(x=50, y=230)

    copy_right = Label( main, text="© 2023 Ugyen. All rights reserved.", width=42, padx=4, anchor=CENTER, font=("Helvetica 9"), bg=theme_color4, fg=theme_color3)
    copy_right.place(x=25, y=280)

global global_username
global_username = None

def user_authentication():
    global global_username
    global global_user_id
    global user_notes

    username_entered = username.get()
    password_entered = Password.get()

    if not username_entered or not password_entered:
        showerror("Error", "Both Username and Password are required.")
        return

    cursor.execute("SELECT user_id FROM users WHERE username = ? AND password = ?", (username_entered, password_entered))
    result = cursor.fetchone()

    if result is None:
        showerror("Error", "Invalid Username or Password.")
        return

    global_user_id = result[0]
    global_username = username_entered

    cursor.execute('''
        SELECT note_id, date, subject, notes
        FROM user_notes
        WHERE user_id = ?
    ''', (global_user_id,))

    user_notes_list = cursor.fetchall()

    user_notes[global_username] = [{
        "NoteId": note[0],
        "Date": note[1],
        "Subject": note[2],
        "Notes": note[3]
    } for note in user_notes_list]

    dashboard()

def dashboard():
    global main
    if main:
        main.destroy()
    option_view = Frame(window, width=368, height=300, bg=theme_color4)
    option_view.grid(row=1, column=0)

    note_view_text = Label(option_view, text="Choose Option", width=21, padx=4, anchor=CENTER, font=('Helvetica 14'), bg=theme_color4, fg=theme_color3)
    note_view_text.place(x=60, y=40)

    button =Button(option_view, text="1. Create a note", padx=5, justify=LEFT, height=1, bg=theme_color4,borderwidth=0, font=("Helvetica 12"), command=create_note)
    button.place(x=50, y=90)

    button =Button(option_view, text="2. Retrieve a note", padx=5, justify=LEFT, height=1, bg=theme_color4,borderwidth=0, font=("Helvetica 12"), command=all_note_lists)
    button.place(x=50, y=130)

    button =Button(option_view, text="3. Import Notes (Json files only)", padx=5, height=1, justify=LEFT, bg=theme_color4,borderwidth=0, font=("Helvetica 12"), command=add_json_files)
    button.place(x=50, y=170)

    button =Button(option_view, text="4. Logout", padx=5, height=1, justify=LEFT, bg=theme_color4,borderwidth=0, font=("Helvetica 12"), command=log_out)
    button.place(x=50, y=210)

    copy_right = Label(option_view, text="© 2023 Ugyen. All rights reserved.", width=42, padx=4, anchor=CENTER, font=('Helvetica 9'), bg=theme_color4, fg=theme_color3)
    copy_right.place(x=25, y=280)

note_date = None
note_subject = None
new_notes = None
user_notes = {}
keyword = None
current_note_index = None
user_notes_list = []
user_id = None

def get_selected_date(cal):
    global note_date 
    selected_date = cal.get_date()
    if note_date:
        note_date.delete("1.0", tk.END) 
        note_date.insert("1.0", selected_date) 
        cal.master.destroy()

def show_calendar(event):
    calendar_window = tk.Toplevel(window)
    calendar_window.title("Select Preferred Date")
    x_position = window.winfo_rootx() + event.x
    y_position = window.winfo_rooty() + event.y

    calendar_window.geometry(f'300x220+{x_position}+{y_position}')

    current_date = datetime.now()
    cal = Calendar(calendar_window, selectmode="day", year=current_date.year, month=current_date.month, day=current_date.day)
    cal.pack()

    get_date_button = tk.Button(calendar_window, text="Get Selected Date", command=lambda: get_selected_date(cal))
    get_date_button.pack()

def add_json_files():
    file_paths = filedialog.askopenfilenames(
        filetypes=[("JSON files", "*.json")],
        initialdir=os.getcwd(),
    )
    if not file_paths:
        dashboard()
        return

    option_view = tk.Frame(window, width=368, height=300, bg=theme_color4)
    option_view.grid(row=1, column=0)

    listbox = tk.Listbox(option_view, selectmode=tk.MULTIPLE, width=80, height=15)
    listbox.pack(pady=10)

    for file_path in file_paths:
        with open(file_path, 'r') as json_file:
            try:
                notes_data = json.load(json_file)
                notes_list = notes_data.get("notes", [])

                for note in notes_list:
                    date = note.get("date", "")
                    subject = note.get("subject", "")
                    notes_content = note.get("text", "")
                    url = note.get("url", "")  # Add this line to get the URL field

                    # Insert the note into the database, including the current user ID and URL
                    cursor.execute('''
                        INSERT INTO user_notes (user_id, date, subject, notes, url)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (global_user_id, date, subject, notes_content, url))

                    conn.commit()
                    listbox.insert(tk.END, f"Date: {date}, Subject: {subject}, Notes: {notes_content}, URL: {url}")

            except json.JSONDecodeError:
                print(f"Error decoding JSON file: {file_path}")

def create_note():
    global note_date
    global note_subject
    global new_notes
    global note_url
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
    
    note_url_label = Label(create_view, text="Url", width=21, padx=4, anchor='w', font=('Helvetica 10'), bg=theme_color4, fg=theme_color3)
    note_url_label.place(x=5, y=110)

    note_url = tk.Text(create_view,  font=("Helvetica 12"), height=1, width=31, highlightbackground="grey", highlightthickness=1)
    note_url.place(x=75, y=110)
    
    new_notes_label = Label(create_view, text="Add Notes:", width=21, padx=4, anchor='w', font=('Helvetica 10'), bg=theme_color4, fg=theme_color3)
    new_notes_label.place(x=5, y=140)
    
    new_notes = tk.Text(create_view,  font=("Helvetica 12"), height=4, width=31, highlightbackground="grey", highlightthickness=1)
    new_notes.place(x=75, y=140)
    
    button_create =tk.Button(create_view, text="Save", width=15, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12), justify=CENTER, command=save_note)
    button_create.place(x=10, y=230)
    
    button_cancel =tk.Button(create_view, text="Cancel", width=15, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12), justify=CENTER,command=dashboard)
    button_cancel.place(x=182, y=230)
    
    copy_right = Label(create_view, text="© 2023 Ugyen. All rights reserved.", width=42, padx=4, anchor=CENTER, font=('Helvetica 9'), bg=theme_color4, fg=theme_color3)
    copy_right.place(x=25, y=280)

def save_note():
    global note_date
    global note_subject
    global note_url
    global new_notes
    global user_notes
    global global_username

    date_value = note_date.get("1.0", tk.END).strip()
    subject_value = note_subject.get("1.0", tk.END).strip()
    url_value = note_url.get("1.0", tk.END).strip()
    notes_value = new_notes.get("1.0", tk.END).strip()

    if not date_value:
        showerror("Error", "Please select a date.")
        return

    if not subject_value:
        showerror("Error", "Please enter a subject.")
        return

    if not notes_value:
        showerror("Error", "Please enter notes content.")
        return

    cursor.execute("SELECT user_id FROM users WHERE username = ?", (global_username,))
    result = cursor.fetchone()
    if result:
        user_id = result[0]
    else:
        showerror("Sorry", "User doesnot exit with that name.")
        return

    cursor.execute('''INSERT INTO user_notes (user_id, date, subject, notes, url) VALUES (?, ?, ?,?, ?)''', (user_id, date_value, subject_value, notes_value, url_value))
    conn.commit()

    if global_username not in user_notes:
        user_notes[global_username] = []

    user_notes[global_username].append({
        "Date": date_value,
        "Subject": subject_value,
        "Url": url_value,
        "Notes": notes_value
    })

    note_date.delete("1.0", tk.END)
    note_subject.delete("1.0", tk.END)
    note_url.delete("1.0", tk.END)
    new_notes.delete("1.0", tk.END)

    create_view = Frame(window, width=368, height=300, bg=theme_color4)
    create_view.grid(row=1, column=0)

    new_notes_label = tk.Label(create_view, text="Notes Saved", font=("Helvetica 12"), height=6, width=38, highlightbackground="grey", highlightthickness=1)
    new_notes_label.place(x=10, y=80)

    button_create = tk.Button(create_view, text="Add Another", width=15, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12, "bold"), justify=CENTER, command=create_note)
    button_create.place(x=10, y=230)

    button_cancel = tk.Button(create_view, text="Dashboard", width=15, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12, "bold"), justify=CENTER, command=dashboard)
    button_cancel.place(x=182, y=230)

    copy_right = tk.Label(create_view, text="© 2023 Ugyen. All rights reserved.", width=42, padx=4, anchor=CENTER, font=('Helvetica 9'), bg=theme_color4, fg=theme_color3)
    copy_right.place(x=25, y=280)

def all_note_lists():
    global keyword
    global global_username
    global user_notes_list  

    cursor.execute('''
    SELECT user_notes.note_id, user_notes.date, user_notes.subject, user_notes.notes,user_notes.url FROM user_notes
    JOIN users ON user_notes.user_id = users.user_id WHERE users.username = ? ''', (global_username,))

    user_notes_list = cursor.fetchall()

    option_view = Frame(window, width=368, height=300, bg=theme_color4)
    option_view.grid(row=1, column=0)

    note_view_text = Label(option_view, text=f"Notes of {global_username}", width=21, padx=4, anchor=CENTER, font=('Helvetica 16 bold'), bg=theme_color4, fg=theme_color3)
    note_view_text.place(x=40, y=10)

    if not user_notes_list or len(user_notes_list) == 0:
        no_notes_label = Label(option_view, text="No notes have been added yet.", font=("Helvetica", 12, "bold"), bg=theme_color4, fg=theme_danger)
        no_notes_label.place(x=80, y=110)

        button_create = tk.Button(option_view, text="Add", width=15, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12), justify=CENTER, command=create_note)
        button_create.place(x=10, y=230)

        button_cancel = tk.Button(option_view, text="Dashboard", width=15, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12), justify=CENTER, command=dashboard)
        button_cancel.place(x=182, y=230)
    else:
        note_position = 50
        note_number = 1

        # Create a Listbox widget to display the notes
        notes_listbox = tk.Listbox(option_view, font=("Helvetica", 12), bg=theme_color4, fg=theme_color3, selectmode=tk.SINGLE)
        notes_listbox.place(x=10, y=note_position, width=350, height=140)

        # Create a vertical scrollbar and link it to the Listbox
        scrollbar = tk.Scrollbar(option_view, command=notes_listbox.yview)
        scrollbar.place(x=355, y=note_position, height=140)
        notes_listbox.config(yscrollcommand=scrollbar.set)

        def on_click(event):
            selected_index = notes_listbox.curselection()
            if selected_index:
                index = selected_index[0]
                note = user_notes_list[index]
                display_full_note(index, note[1], note[2], note[3], note[4])

        for note_index, note in enumerate(user_notes_list):
            subject = note[2][:25]
            url = note[4]
            notes_listbox.insert(tk.END, f"{note_number}) {subject}")

            note_number += 1

        # Bind the Listbox selection event to the on_click function
        notes_listbox.bind("<ButtonRelease-1>", on_click)

        keyword = tk.Text(option_view, height=1, wrap=tk.WORD, width=30, font=("Helvetica", 12), padx=5, pady=6, bd=1, relief="solid")
        keyword.place(x=10, y=200)

        search_button = tk.Button(option_view, text="Search", width=5, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12), justify=CENTER, command=search_notes)
        search_button.place(x=280, y=200)

        button_cancel = tk.Button(option_view, text="Go to Dashboard", width=15, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12), justify=CENTER, command=dashboard)
        button_cancel.place(x=110, y=240)

    copy_right = Label(option_view, text="© 2023 Ugyen. All rights reserved.", width=42, padx=4, anchor=CENTER, font=('Helvetica 9'), bg=theme_color4, fg=theme_color3)
    copy_right.place(x=25, y=280)

def search_notes():
    global keyword, matching_notes
    global global_username

    keyword_text = keyword.get("1.0", tk.END).strip().lower()
    if not keyword_text:
        showerror("Error", "Please enter a keyword to search.")
        return

    if global_username not in user_notes or not user_notes[global_username]:
        messagebox.showinfo("Info", "No notes found for this user.")
        return

    matching_notes = []
    for index, note in enumerate(user_notes[global_username]):
        if 'Subject' in note and keyword_text in note['Subject'].lower():
            matching_notes.append((index, note))

    if not matching_notes:
        messagebox.showinfo("Info", "No matching notes found.")
        return

    global current_note_index
    current_note_index = 0
    display_search_results(matching_notes)

def display_search_results(matching_notes):
    global current_note_index
    global keyword
    keyword_text = keyword.get("1.0", tk.END).strip()

    retrieve_view = Frame(window, width=368, height=300, bg=theme_color4)
    retrieve_view.grid(row=1, column=0)

    note_view_text = Label(retrieve_view, text=f"Search Result of '{keyword_text}'", width=21, padx=4, anchor=CENTER, font=("Helvetica 12"), bg=theme_color4, fg=theme_color3)
    note_view_text.place(x=80, y=10)

    y_position = 50
    note_number = 1
    
    for note_index, note_dict in matching_notes:
        try:
            note_date = note_dict['Date']
            url = note_dict.get("URL", "URL not found")
        except KeyError:
            note_date = "Date not found"

        subject = note_dict.get("Subject", "")
        note_content = note_dict.get("Notes", "")

        def on_click_closure(event, index=note_index, date=note_date, subject=subject, notes=note_content, url=url):
                    display_full_note(index, date, subject, notes, url)

        matched_subject = Label(retrieve_view, text=f"{note_number}) {subject}", font=("Helvetica 12"), bg=theme_color4, fg=theme_color3, justify=LEFT, anchor=NW)
        matched_subject.place(x=5, y=y_position)
        matched_subject.bind("<Button-1>", on_click_closure)
        y_position += 30
        note_number += 1
    button_cancel = tk.Button(retrieve_view, text="Back", width=15, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12), justify=CENTER, command=all_note_lists)
    button_cancel.place(x=20, y=240)
    button_cancel = tk.Button(retrieve_view, text="Dashboard", width=15, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12), justify=CENTER, command=dashboard)
    button_cancel.place(x=180, y=240)

    copy_right = Label(retrieve_view, text="© 2023 Ugyen. All rights reserved.", width=42, padx=4, anchor=CENTER, font=('Helvetica 9'), bg=theme_color4, fg=theme_color3)
    copy_right.place(x=25, y=280)

def fetch_title(url: str) -> str:
    title = ""
    try:
        res = requests.get(url)
        res.raise_for_status()  
        
        page = res.text.lower()
        title_start = page.find("<title>")
        title_end = page.find("</title>")

        if title_start != -1 and title_end != -1:
            title = page[title_start + 7: title_end].strip()
        else:
            raise ValueError("Title tags not found on the page.")

    except ValueError as ve:
        # Handle the case when title tags are not found
        title = str(ve)
    except requests.RequestException as e:
        # Handle request exceptions
        title = f"Request failed: {e}"
    except Exception as ex:
        # Handle other unexpected exceptions
        title = f"An error occurred: {ex}"

    return title

def display_full_note(note_index, note_date, note_subject, note_content, note_url):
    global current_note_index
    current_note_index = note_index

    note_view = Frame(window, width=368, height=300, bg=theme_color4)
    note_view.grid(row=1, column=0)

    note_view_text = Label(note_view, text="Single Note Page", width=21, padx=4, anchor=CENTER, font=('Helvetica 14 bold'), bg=theme_color4, fg=theme_color3)
    note_view_text.place(x=40, y=30)     

    subject_label = tk.Label(note_view, text="Subject: ", font=('Helvetica 12'), bg=theme_color4)
    subject_label.place(x=10, y=80)  

    subject_value = tk.Label(note_view, text=note_subject, wraplength=300, font=('Helvetica 12'), bg=theme_color4)
    subject_value.place(x=70, y=80)

    date_label = tk.Label(note_view, text="Date: ", font=('Helvetica 12'), bg=theme_color4)
    date_label.place(x=10, y=105)   

    date_value = tk.Label(note_view, text=note_date, wraplength=300, font=('Helvetica 12'), bg=theme_color4)
    date_value.place(x=70, y=105)

    url_label = tk.Label(note_view, text="URL: ", font=('Helvetica 12'), bg=theme_color4)
    url_label.place(x=10, y=130)

    title = fetch_title(note_url)
    url_value = tk.Label(note_view, text=title, wraplength=300, font=('Helvetica 12'), bg=theme_color4)
    url_value.place(x=70, y=130)
    window.update_idletasks()

    note_label = tk.Label(note_view, text="Note: ", font=('Helvetica 12'), bg=theme_color4)
    note_label.place(x=10, y=155)  

    note_value = tk.Label(note_view, text=note_content, anchor=W, wraplength=250, font=('Helvetica 12'), bg=theme_color4)
    note_value.place(x=70, y=155)
    
    button_edit =tk.Button(note_view, text="Edit", width=10, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12), justify=CENTER, command=edit_current_note)
    button_edit.place(x=10, y=230)

    def delete_current_note():
        global current_note_index
        global global_username

        if 0 <= current_note_index < len(user_notes_list):
            note_id = user_notes_list[current_note_index][0]

            cursor.execute('''DELETE FROM user_notes WHERE note_id = ?''', (note_id,))
            conn.commit()

            all_note_lists()
            messagebox.showinfo("Note Deleted", "Note deleted successfully!")
        else:
            messagebox.showinfo("Error", "Invalid note index.")

    button_delete =tk.Button(note_view, text="Delete", width=10, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12), justify=CENTER, command=delete_current_note)
    button_delete.place(x=120, y=230)
    
    button_done =tk.Button(note_view, text="Back", width=10, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Helvetica", 12), justify=CENTER,command=all_note_lists)
    button_done.place(x=230, y=230)
    
    copy_right = Label(note_view, text="© 2023 Ugyen. All rights reserved.", width=42, padx=4, anchor=CENTER, font=('Helvetica 9'), bg=theme_color4, fg=theme_color3)
    copy_right.place(x=25, y=280)

import tkinter.messagebox as messagebox
from tkinter import LabelFrame

def edit_current_note():
    global current_note_index
    global global_username

    if global_username in user_notes:
        user_notes_list = user_notes[global_username]

        if 0 <= current_note_index < len(user_notes_list):
            current_note = user_notes_list[current_note_index]
            note_id = current_note["NoteId"]
            current_date = current_note.get("Date", "")
            current_subject = current_note.get("Subject", "")
            current_url = current_note.get("Url", "")
            current_content = current_note.get("Notes", "")

            note_edit_window = tk.Toplevel(window)
            note_edit_window.title("Edit Note")
            note_edit_window.configure(bg=theme_color4)

            # Use LabelFrame to group related widgets
            entry_frame = LabelFrame(note_edit_window, text="Edit Note")
            entry_frame.pack(padx=10, pady=10)

            date_label = tk.Label(entry_frame, text="Date:")
            date_label.grid(row=0, column=0, sticky=tk.W)
            date_entry = tk.Entry(entry_frame)
            date_entry.insert(0, current_date)
            date_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

            subject_label = tk.Label(entry_frame, text="Subject:")
            subject_label.grid(row=1, column=0, sticky=tk.W)
            subject_entry = tk.Entry(entry_frame)
            subject_entry.insert(0, current_subject)
            subject_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

            url_label = tk.Label(entry_frame, text="URL:")
            url_label.grid(row=2, column=0, sticky=tk.W)
            url_entry = tk.Entry(entry_frame)
            url_entry.insert(0, current_url)
            url_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

            content_label = tk.Label(entry_frame, text="Content:")
            content_label.grid(row=3, column=0, sticky=tk.W)
            content_text = tk.Text(entry_frame, wrap=tk.WORD, height=10, width=40)
            content_text.insert(tk.END, current_content)
            content_text.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

            def save_edited_note():
                global global_username

                new_date = date_entry.get()
                new_subject = subject_entry.get()
                new_url = url_entry.get()
                new_content = content_text.get("1.0", tk.END).strip()

                # Additional input validation could be added here

                # Update the current_note dictionary
                current_note["Date"] = new_date
                current_note["Subject"] = new_subject
                current_note["Url"] = new_url
                current_note["Notes"] = new_content

                # Update the database
                try:
                    cursor.execute('''
                        UPDATE user_notes
                        SET date = ?, subject = ?, url = ?, notes = ?
                        WHERE note_id = ?
                    ''', (new_date, new_subject, new_url, new_content, note_id))
                    conn.commit()

                    note_edit_window.destroy()
                    all_note_lists()
                    messagebox.showinfo("Note Saved", "Your edited note has been saved successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")

            save_button = tk.Button(entry_frame, text="Save", padx=5, height=1, justify=LEFT, bg=theme_color5,
                                    fg=theme_color4, borderwidth=0, font=("Helvetica 11"), command=save_edited_note)
            save_button.grid(row=4, column=1, pady=10, sticky=tk.W)
        else:
            showerror("Error", "Invalid note index.")
    else:
        showerror("Error", "User not found in user notes.")


def log_out():
    global global_username
    global_username = None
    global main
    if main:
        main.destroy()
    login_page() 

login_page()
window.mainloop()