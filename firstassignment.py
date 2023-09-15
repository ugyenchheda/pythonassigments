from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showerror
from PIL import Image, ImageTk
import os

script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, "images", "login.png")
# Open the image
image = Image.open(image_path)

# Define the new size (e.g., 200x200 pixels)
new_size = (200, 200)

# Resize the image
resized_image = image.resize(new_size)

theme_color1 = "blue"
theme_color2 = "#3b474d"
theme_color3 = "black"
theme_color4 = "white"
theme_color5 = "#3b474d"
transparent_theme = "FF0000AA"

window = Tk()
window.geometry('368x400')
window.title("Ugyen's Assignment")
window.configure(bg=theme_color4)
window.resizable(height=FALSE, width=FALSE)

# frames
top = Frame(window, width=368, height=80, bg=theme_color3)
top.grid(row=0, column=0)

main = Frame(window, width=368, height=300, bg=theme_color4)
main.grid(row=1, column=0)

image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)



# Top frame
app_name = Label(top, image=photo, compound=LEFT, text="Python Assignment 1", height=10, padx=13, pady=40, relief="solid", anchor=CENTER, font=('Arial 16 bold'), bg=theme_color2, fg=theme_color4)
app_name.photo = photo  
app_name.place(x=0, y=0)

#main frame
welcome = Label(main, text="Welcome", width=21, height=2, pady=10, anchor=CENTER, font=('Arial 16 bold'), bg=theme_color4, fg=theme_color3)
welcome.place(x=44, y=5)

login_text = Label(main, text="Login to Proceed", width=21, padx=4, anchor=CENTER, font=('Arial 12'), bg=theme_color4, fg=theme_color3)
login_text.place(x=80, y=55)

username_text = Label(main, text="Username:", width=21, padx=4, anchor=CENTER, font=('Arial 11'), bg=theme_color4, fg=theme_color3)
username_text.place(x=20, y=95)
username = ttk.Entry(main, width=21, justify=CENTER, font=("Arial 12"))
username.place(x=80, y=120)

Password_text = Label(main, text="Password:", width=21, padx=4, anchor=CENTER, font=('Arial 11'), bg=theme_color4, fg=theme_color3)
Password_text.place(x=20, y=150)
Password = ttk.Entry(main, width=21, justify=CENTER, font=("Arial 12"))
Password.place(x=80, y=175)

notes_list = []
def user_dashboard():
    user_name = "ugyen"
    password= "ugyen"
    username_entered = username.get()
    password_entered = Password.get()
    if not username_entered or not password_entered:
            showerror("Error", "Both Username and Password are required.")
            return
    
    if user_name != username_entered:
            showerror("Error", "User doesnot exist.")
            return
    if password_entered != password:
            showerror("Error", "Incorrect Password.")
            return
    notes_view()

def create_note():
    global notes_list
    create_view = Frame(window, width=368, height=300, bg=theme_color4)
    create_view.grid(row=1, column=0)

    note_view_text = Label(create_view, text="Create Notes", width=21, padx=4, anchor=CENTER, font=('Arial 12'), bg=theme_color4, fg=theme_color3)
    note_view_text.place(x=80, y=40)
    
    new_notes = tk.Text(create_view,  font=("Arial 12"), height=6, width=38, highlightbackground="grey", highlightthickness=1)
    new_notes.place(x=10, y=80)
    note_content = new_notes.get("1.0", "end-1c")
    notes_list.append(note_content)
    new_notes.delete("1.0", "end")
    button_create =tk.Button(create_view, text="Save", width=15, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Arial", 12, "bold"), justify=CENTER)
    button_create.place(x=10, y=230)
    
    button_cancel =tk.Button(create_view, text="Cancel", width=15, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Arial", 12, "bold"), justify=CENTER,command=user_dashboard)
    button_cancel.place(x=182, y=230)
    
    copy_right = Label(create_view, text="© 2023 Ugyen. All rights reserved.", width=42, padx=4, anchor=CENTER, font=('Arial 9'), bg=theme_color4, fg=theme_color3)
    copy_right.place(x=25, y=280)

def logout():
    option_view = Frame(window, width=368, height=300, bg=theme_color4)
    option_view.grid(row=1, column=0)

    note_view_text = Label(option_view, text="Log Out", width=21, padx=4, anchor=CENTER, font=('Arial 12'), bg=theme_color4, fg=theme_color3)
    note_view_text.place(x=80, y=40)
    
    new_notes = ttk.Entry(option_view,  font=("Arial 12"), width=30)
    new_notes.place(x=10, y=80)

def retrieve_note():
    option_view = Frame(window, width=368, height=300, bg=theme_color4)
    option_view.grid(row=1, column=0)

    note_view_text = Label(option_view, text="Retrieve a note", width=21, padx=4, anchor=CENTER, font=('Arial 12'), bg=theme_color4, fg=theme_color3)
    note_view_text.place(x=80, y=40)
    
        
    extract_window = tk.Toplevel(window)
    extract_window.title("Notes")

    notes_text = tk.Text(extract_window, font=("Arial", 12), height=10, width=40)
    notes_text.pack(padx=10, pady=10)

    # Populate the Text widget with the notes from the notes_list
    for note in notes_list:
        notes_text.insert("end", note + "\n")
        new_notes.place(x=10, y=80)

def notes_view():
    option_view = Frame(window, width=368, height=300, bg=theme_color4)
    option_view.grid(row=1, column=0)

    note_view_text = Label(option_view, text="Choose Option", width=21, padx=4, anchor=CENTER, font=('Arial 12'), bg=theme_color4, fg=theme_color3)
    note_view_text.place(x=80, y=40)

    button =Button(option_view, text="1. Create a note", padx=5, justify=LEFT, height=1, bg=theme_color4,borderwidth=0, font=("Arial 11"), command=create_note)
    button.place(x=50, y=90)

    button =Button(option_view, text="2. Retrieve a note", padx=5, justify=LEFT, height=1, bg=theme_color4,borderwidth=0, font=("Arial 11"), command=retrieve_note)
    button.place(x=50, y=130)

    button =Button(option_view, text="3. Logout", padx=5, height=1, justify=LEFT, bg=theme_color4,borderwidth=0, font=("Arial 11"), command=logout)
    button.place(x=50, y=170)

    copy_right = Label(option_view, text="© 2023 Ugyen. All rights reserved.", width=42, padx=4, anchor=CENTER, font=('Arial 9'), bg=theme_color4, fg=theme_color3)
    copy_right.place(x=25, y=280)

button =Button(main, text="Continue", width=25, padx=5, height=1, bg=theme_color2, fg=theme_color4, font=("Arial 12 bold"), justify=CENTER,command=user_dashboard)
button.place(x=50, y=230)
copy_right = Label(main, text="© 2023 Ugyen. All rights reserved.", width=42, padx=4, anchor=CENTER, font=('Arial 9'), bg=theme_color4, fg=theme_color3)
copy_right.place(x=25, y=280)



window.mainloop()

# Top frame
