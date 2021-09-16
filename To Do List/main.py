import time

def printtodo(todo):
    check = " "
    if todo["completed"]:
        check = "x"
    print("["+check+"]", todo["title"])
    print("   ",todo["body"])
    print("   ",todo["due_date"])

def main():

    to_dos = []

    while True:
        print("1. Add to do")
        print("2. Remove to do")
        print("3. Edit to do")
        print("4. View to do")
        print("5. Checkmark to do")
        print("6. Exit")
        choice = input("Choose an option: ")

        print()

        if choice == "1":
            title = input("Title of your to do: ")
            body = input("Add a description: ")
            due_date = input("Add a due date: ")

            id = time.time()

            to_do = {
                "id":id,
                "title":title,
                "body":body,
                "due_date":due_date,
                "completed":False
            }

            to_dos.append(to_do)

        if choice == "2":
            i = 0
            for to_do in to_dos:
                print(str(i) + ")")
                printtodo(to_do)
                i += 1
            option = int(input("Which todo do you want to get rid of? "))
            del to_dos[option]


        if choice == "3":
            i = 0
            for to_do in to_dos:
                print(str(i) + ")")
                printtodo(to_do)
                i += 1
            index = int(input("Which todo do you want to edit?"))

            titlechange = input("Do you want to change the name of the todo (yes/no)?")
            if titlechange == "yes":
                to_dos[index]["title"] = input("What is the new title?")

            else:
                pass

            bodychange = input("Do you want to change the description of the todo (yes/no)?")
            if bodychange == "yes":
                to_dos[index]["body"] = input("What is the new description?")
            else:
                pass

            due_datechange = input("Do you want to change the due date of the todo.(yes/no)")
            if due_datechange == "yes":
                to_dos[index]["due_date"] = input("What is the new due date?")
            else:
                pass

        if choice == "4":
            for to_do in to_dos:
                printtodo(to_do)

        if choice == "5":
            i = 0
            for to_do in to_dos:
                printtodo(to_do)
            i += 1
            checkmark = int(input("Which todo do you want to checkmark?"))
            for to_do in to_dos:
                if checkmark == index(to_do):
                    to_do.completed = True

        if choice == "6":
            quit = input("Are you sure you want to quit? yes/no: ")
            if quit == "yes":
                break

        print()

main()
