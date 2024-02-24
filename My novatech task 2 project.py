# Import necessary libraries
import os

# Define note class
class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

# Define storage location (text file)
storage_file = "notes.txt"

# Function to read notes from file
def read_notes():
    notes = []
    if os.path.exists(storage_file):
        with open(storage_file, "r") as f:
            for line in f:
                title, *content = line.strip().split("|")
                notes.append(Note(title, "\n".join(content)))
    return notes

# Function to write notes to file
def write_notes(notes):
    with open(storage_file, "w") as f:
        for note in notes:
            f.write(f"{note.title}|{note.content}\n")

# Function to list all notes
def list_notes():
    notes = read_notes()
    if notes:
        for note in notes:
            print(f"- {note.title}")
    else:
        print("No notes found.")

# Function to create a new note
def create_note():
    title = input("Enter note title: ")
    content = input("Enter note content (multiple lines): ")
    notes = read_notes()
    notes.append(Note(title, content))
    write_notes(notes)
    print(f"Note '{title}' created successfully!")

# Function to view a specific note
def view_note():
    title = input("Enter note title to view: ")
    notes = read_notes()
    for note in notes:
        if note.title == title:
            print(f"\nTitle: {note.title}")
            print(f"Content:\n{note.content}\n")
            return
    print(f"Note '{title}' not found.")

# Function to delete a note
def delete_note():
    title = input("Enter note title to delete: ")
    notes = read_notes()
    new_notes = [note for note in notes if note.title != title]
    if len(new_notes) != len(notes):
        write_notes(new_notes)
        print(f"Note '{title}' deleted successfully!")
    else:
        print(f"Note '{title}' not found.")

# Main menu
def main():
    print("\nWelcome to the Note-Taking App!")
    print("Available commands:")
    print("- list: List all notes")
    print("- create: Create a new note")
    print("- view: View the content of a note")
    print("- delete: Delete a note")
    print("- exit: Exit the application")

    while True:
        command = input("\nEnter a command: ").lower()
        if command == "list":
            list_notes()
        elif command == "create":
            create_note()
        elif command == "view":
            view_note()
        elif command == "delete":
            delete_note()
        elif command == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
