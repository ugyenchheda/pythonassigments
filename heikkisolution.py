# notes.py - Simple notes application

# modules
import sys
import datetime
import getpass

# ---- HARDCODED DATA STARTS HERE ----
# Usually we would use database but here lists are used to store users
users = ["user1", "user2", "user3"]
passwords = ["pass1", "pass2", "pass3"]

# notes is a list of note dictionary
notes = []

# First test note for first user
note = {
    "userid" : 0,
    "subject" : "sub1",
    "date" : datetime.datetime.now(),
    "text" : "text1"
}

# Add note to the notes list
notes.append(note)

# Second test note for second user
note = {
    "userid" : 1,
    "subject" : "sub2",
    "date" : datetime.datetime.now(),
    "text" : "text2"
}

# Add note to the notes list
notes.append(note)

# Third test note for first user
note = {
    "userid" : 0,
    "subject" : "sub3",
    "date" : datetime.datetime.now(),
    "text" : "text3"
}

# Add note to the notes list
notes.append(note)

# ---- HARDCODED DATA ENDS HERE ----

# authentication function
# returns : userid as an integer
# return value -1 means that user was not found
def authenticate(username, password) -> int:
    # Userid is used after the login to identify user
    userid = 0

    # Loop to authenticate user
    for u in users:
        # TODO: test prints
        # print(u)
        if u == username:
            if password != passwords[userid]:
                return -1
            else:
                return userid
        userid += 1

    # User was not found.
    return -1

# create a new note for a specific user
# arguments : userid, subject, date, text
# returns : noteid or -1 if note creation fails
def createnote(userid, subject, date, text) -> int:
    # TODO: Error handling will be added later. 
    # Create a note item
    note = {
        "userid" : userid,
        "subject" : subject,
        "date" : date,
        "text" : text,
    }

    # Add note item to notes list
    notes.append(note)

    return(len(notes) - 1)

# list database ids of notes of a user
# arguments : userid
# returns : list of user's notes
def listusernotes(userid) -> []:
    # Create a new empty list that will contain ids and subject of a user notes
    usernotes = []
    # Database id of a single note
    dbid = 0
    # Go through all the notes and populate the new list that contains ids of one user
    for n in notes:
        if n["userid"] == userid:
            usernotes.append(dbid)
        # Next dbid to check
        dbid += 1
    
    # Return the populated list of notes of one user
    return usernotes

# list note details
# arguments : noteid
# returns : a note item as a dictionary
def notedetails(noteid) -> {}:
    # TODO: When database is used this function is used to fetch details from there
    # Now we simply return the information from notes list
    return notes[noteid]

# delete a note
# arguments : noteid
# returns : True is success or False in case of failure
def deletenote(noteid) -> bool:
    # Delete a list item
    notes.pop(noteid)
    # Return True for now
    return True

# main function
def main() -> int:
    # Main loop that will run "forever" - TODO: add exit later
    while (True):
        # userid is set initially to -1. In this app it means that user is not authenticated.
        userid = -1

        # Login loop
        while (userid == -1):
            print("Login please:")
            username = input("Username: ")
            password = getpass.getpass()
            userid = authenticate(username, password)

        # Empty line
        print()

        # Main menu
        onmainmenu = True
        while (onmainmenu):
            print("Main menu:")
            print("1. Create a note")
            print("2. Retrieve notes")
            print("3. Logout")

            choice = input("Choose and press enter: ")

            # Create a new note
            if int(choice) == 1:
                # Ask for details
                subject = input("Subject: ")
                text = input("Text: ")

                # Initially result is set to -1
                result = -1
                # Create a new note
                result = createnote(userid, subject, datetime.datetime.now(), text)
                # Print the result
                print("New note created: " + str(result))

            # List notes of current user and open a new menu to access them
            elif int(choice) == 2:
                # Request list of notes
                usernotes = listusernotes(userid)

                # List number
                number = 0

                # Fetch details of each note and show them in menu
                for n in usernotes:
                    print(str(number) + ". " + notedetails(n)["subject"])
                    number += 1
                
                # Show details of one note and show note specific menu
                selectednote =  input("Enter a number of a note of any other number to exit")
                if ((int(selectednote) < len(usernotes)) and (int(selectednote) >= 0)):
                    note = notedetails(usernotes[int(selectednote)])
                    print("--- --- ---")
                    print("Subject: " + note["subject"])
                    print("Date: " + str(note["date"]))
                    print("Text: " + note["text"])
                    print("--- --- ---")
                    # One new menu loop that is used to delete menu item
                    choice = input("Type \"Delete\" to delete this note or press enter to go back: ")

                    if (choice == "Delete"):
                        deletenote(usernotes[int(selectednote)])
                        # Reset choice variable as it is used in other menus
                        choice = 0
                    else:
                        # Reset choice variable as it is used in other menus
                        choice = 0

                else:
                    # Reset choice variable as it is used in other menus
                    choice = 0

            # Rest of the answers will log user out
            else:
                onmainmenu = False
            
    # Exit successfully
    return(0)

# main function entry point
if __name__ == '__main__':
    sys.exit(main())
