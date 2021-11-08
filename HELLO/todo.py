import sys #system config
import os  # operating system module


def list_task(): #list task function
    if (os.path.isfile('text.txt')): # to create filepath in your directory
        count = 1  # initializing count as one
        with open('text.txt') as listingTodo:  # fecting text file as text listing to do
            filesize = os.path.getsize("text.txt")  # textfile path
            if filesize == 0:  # null file
                print("No todos for today! :)")  # when file is null it shows up the text "no todos"
            else:
                for lines in listingTodo:
                    if "[X] " in lines:
                        print(str(count) + " - " + lines)
                        count += 1
                    else:
                        print(str(count) + " - [ ] " + lines)
                        count += 1
    else:
        with open('text.txt','a') as listingTodo:
            print("No todos for today! :)")



def add_task():
    if len(sys.argv) < 3:
        print("Unable to add: no task provided")
    else:
        with open("text.txt", "a") as addition:
            addition.write(sys.argv[2] + "\n")
            print(sys.argv[2] +" Item has been added to the list")


def remove_task():
    if len(sys.argv) < 3:
        print("Unable to remove: no index provided")
    elif len(sys.argv) == 3:
        if sys.argv[2].isnumeric():
            index = int(sys.argv[2]) - 1
            with open("text.txt", "r+") as substraction:
                if index < len(substraction.readlines()):
                    substraction.seek(0)
                    lines = substraction.readlines()
                    del lines[index]
                    substraction.seek(0)
                    substraction.truncate()
                    substraction.writelines(lines)
                    print(" Item has been removed from the list")
                else:
                    print("Unable to remove: index out of bound")
        else:
            print("Unable to remove: index is not a number")


def check_task():
    if len(sys.argv) < 3:
        print("Unable to check: no index provided")
    elif len(sys.argv) == 3:
        if sys.argv[2].isnumeric():
            with open("text.txt", "r+") as finding:
                index = int(sys.argv[2]) - 1
                if index < len(finding.readlines()):
                    finding.seek(0)
                    elements = finding.readlines(index)
                    elements.insert(index, "[X] ")
                    finding.seek(0)
                    finding.writelines(elements)
                    print(elements)

                else:
                    print("Unable to check: index out of bound")
        else:
            print("Unable to check: index is not a number")


if len(sys.argv) == 1:
    print("\nCommand Line Todo application"
          "\n\n========================= \n\nCommand line arguments: \n"
          " -l   Lists all the tasks \n -a   Adds a new task \n"
          " -r   Removes a task \n -c   Completes a task")

elif len(sys.argv) > 1:

    if sys.argv[1] == "-l":
        list_task()


    elif sys.argv[1] == "-a":
        add_task()

    elif sys.argv[1] == "-r":
        remove_task()

    elif sys.argv[1] == "-c":
        check_task()

else:
    print("Unsupported argument \n\nCommand line arguments: \n"
          " -l   Lists all the tasks \n -a   Adds a new task \n"
          " -r   Removes a task \n -c   Completes a task")