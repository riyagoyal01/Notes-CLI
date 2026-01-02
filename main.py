import os
from datetime import datetime


NOTES_dir="Notes"

if not os.path.exists(NOTES_dir):
    os.makedirs(NOTES_dir)

def reading_notes():
    print('Notes:\n')
    c=os.listdir(NOTES_dir)
    for i in range(len(c)):
        print(i+1,c[i])

    a= input("Enter note title: ")
    a=a.lower()
    filename = f"{a}.txt"
    filepath = os.path.join(NOTES_dir, filename)

    if not os.path.exists(filepath):
        print("INVALID INPUT")
        reading_notes()

    with open(filepath, "r") as file:
        content = file.read()

    print("\n--- Note Content ---")
    print(content)
    print("--------------------")

def creating_notes():
    a= input("Enter note title: ")
    a=a.lower()
    filename = f"{a}.txt"
    filepath = os.path.join(NOTES_dir, filename)

    if os.path.exists(filepath):
        print("A note with this title already exists!")
        creating_notes()
    
    print("Enter the content of the note (type END on a new line to finish):")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
        lines.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

    with open(filepath,"w") as file:
        content="".join(lines)
        file.write(content)

def removing_notes():
    print('Notes:\n')
    c=os.listdir(NOTES_dir)
    for i in range(len(c)):
        print(i+1,c[i])

    a= input("Enter note title: ")
    a=a.lower()
    filename = f"{a}.txt"
    filepath = os.path.join(NOTES_dir, filename)

    if not os.path.exists(filepath):
        print("INVALID INPUT")
        removing_notes()

    os.remove(filepath)

def adding_notes():
    print('Notes:\n')
    c=os.listdir(NOTES_dir)
    for i in range(len(c)):
        print(i+1,c[i])

    a= input("Enter note title: ")
    a=a.lower()
    filename = f"{a}.txt"
    filepath = os.path.join(NOTES_dir, filename)

    if not os.path.exists(filepath):
        print("INVALID INPUT")
        creating_notes()

    print("Enter the content of the note (type END on a new line to finish):")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    with open(filepath,"a") as file:
        content="\n".join(lines)
        file.write(content)

def searching_notes():
    k=input('enter the keyword to search in notes: ').lower()
    found=0
    c=os.listdir(NOTES_dir)
    for i in range(len(c)):
        filename=c[i]
        filepath=os.path.join(NOTES_dir, filename)
        with open(filepath, "r") as file:
            content = file.read()
            content=content.lower()
            if k in content:
                print(f'Keyword is in {c[i]}')
                found=1
    if found==0:
        print("keyword is there in none of the notes")
    else:
        print("keyword is in the above notes")

while True:
    print(" \n"+"NOTE MANAGER ".center(50,'-'))
    print("1. Create Note")
    print("2. Read Note")
    print("3. Search Notes")
    print("4. Remove Note")
    print("5. Add more details")
    print("6. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        creating_notes()
    
    elif choice == "2":
        reading_notes()

    elif choice == "3":
        searching_notes()

    elif choice == "4":
        removing_notes()

    elif choice=="5":
        adding_notes()

    elif choice == "6":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")