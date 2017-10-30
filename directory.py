import csv

def menu():
    print "A) Add to Directory"
    print "B) Diplay Directory"
    print "X) Exit Directory Program"
    selection = raw_input()
    if selection == "A":
        addToDirectory()
    elif selection == "B":
        displayDirectory()
    elif selection == "X":
        quit()
    else:
        print "Invalid Selection"
        menu()

def addToDirectory():
    print "Add to Directory"
    firstName = raw_input("First Name: ")
    lastName = raw_input("Last Name: ")
    email = raw_input("Email: ")
    phone = raw_input("Phone: ")
    directory = open("directory.csv", "a")
    outstring = firstName + "," + lastName + "," + email + "," + phone + "\n"
    directory.write(outstring)
    directory.close()
    print (firstName + " " + lastName + " " + "added to directory.")
    menu()

def displayDirectory():
    print "Display Directory"
    directory = open("directory.csv", "r")
    try:
        rowtext = ""
        reader = csv.reader(directory)
        for row in reader:
            for item in row:
                rowtext = rowtext + " " + item
            print rowtext
            rowtext = ""
    finally:
        directory.close()
    menu()

menu()
