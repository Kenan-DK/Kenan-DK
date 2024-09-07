from tkinter import *  
import tkinter as tk   #Imports Tkinter, the message box, fractions, random
from tkinter import messagebox
from fractions import Fraction
import random

#----------Database stuff------------------------
global staff_usernames
global staff_password
staff_usernames = ["Walter", "H.Okumura", "Dr.Ivo"] #primitive storage of the usernames and passwords
staff_password = ["cryst4L", "Phant0m", "3ggMan"]

global student_usernames
global student_password
student_usernames = ["JokerRen", "Mario86", "M0n1ca"] #primitive storage of the usernames and passwords
student_password = ["P5Royal", "Itsam3", "Adr3st1a"]

global AccountTypeInitial

global Classes
global ClassCodes
Classes = ["Test Class A", "Test Class B"] #Storage of the classes and their codes
ClassCodes = ["60675791", "omYBfKfz"]

global members
global scores
members = ["Sample Member A", "Sample Member B", "Sample Member C", "Sample Member D"]
scores = ["16", "23", "7", "39"]  #Storage of class members and scores


global current_user
current_user = ""

global logged_in
logged_in = False




#----------GAMEPLAY------------------------------
def Gameplay():
    life = 4
    QuestionNumber = 0 #Life and Question Number initialised

    while life != 0:
        QuestionNumber = QuestionNumber + 1
        print("\n""Question", QuestionNumber)
        print("Life:", life)

        numA = random.randint(1, 12)
        numB = random.randint(6, 12)  #Values used within the questions are randomly picked
        numC = random.randint(1, 12)  #These will be altered to better suit the target audience of year 5 and 6 students
        numD = random.randint(3, 12)
        name = ["Olivia", "Andrew", "Jeremy", "Ashley", "Greg", "Harry", "Ramone", "Lorenzo", "Daisy", "Amelia", "Elena", "Peter"]
        item = ["Oranges", "Bananas", "Pizzas", "Chicken", "Chocolate Cakes", "Steak", "Carrots", "Corn Flakes", "Ice Creams", "Pencils", "books", "Video Games"]
        randomX = random.randint(0,11)  #The names, items and randomX/Y are values to be used within the word problems
        randomY = random.randint(0,11)

        QuestionType = random.randint(1, 5)

        if QuestionType == 1:
            fractionA = Fraction(numA, numB)
            fractionB = Fraction(numC, numD)
            actualAnswer = fractionA + fractionB
            print("Question:", fractionA, "+", fractionB)
            
        elif QuestionType == 2:
            fractionA = Fraction(numA, numB)
            fractionB = Fraction(numC, numD)
            actualAnswer = fractionA - fractionB
            print("Question: ", fractionA, "-", fractionB)  #Generates the types of questions to be used
                                                            #as well as the answer to the questions
                                                            #The questions are now fraction based
        
        elif QuestionType == 3:
            fractionA = Fraction(numA, numB)
            fractionB = Fraction(numC, numD)
            actualAnswer = fractionA * fractionB
            print("Question: ", fractionA, "x", fractionB)

        elif QuestionType == 4:
            fractionA = Fraction(numA, numB)
            fractionB = Fraction(numC, numD)
            actualAnswer = fractionA / fractionB
            print("Question: ", fractionA, "/", fractionB)


        elif QuestionType == 5:
            fractionA = Fraction(numA, numB)
            fractionB = Fraction(numC, numD)
            print(name[randomX], "Buys", fractionA, "of a shop's", item[randomY], ".")
            print(name[randomX], "also buys", fractionB, "of the shop's", item[randomX], ".")
            print("How much did", name[randomX], "buy altogether?")
            actualAnswer = fractionA + fractionB


        numerator = int(input("Answer's Numerator: "))
        denominator = int(input("Answer's Denominator: ")) #The numerator and denominator are entered seperately
        userAnswer = Fraction(numerator, denominator)  #then they are entered into the imported fraction module's function
        if userAnswer == actualAnswer:                 #to create the user's full answer.
            print("Correct!")

        else:
            print("Incorrect!")
            print("The Answer is", actualAnswer)  #Deducts a life is the user's answer is incorrect
            life = life - 1



        if life == 0:
            print("\n""<--> Game Over <-->")
            print("Score: ", QuestionNumber)

            if logged_in == True:
                scores.append(QuestionNumber)
                
            else:
                print("your score cannot be saved")
                
            retry = str(input("Would you like to retry? (yes or no): ")) #Retry if user runs out of lives
            if retry == "yes":
                Gameplay() #Calls the sub program so that the user retries.

            else:
                print("Try again sometime!") #Used as a placeholder until main menu developped


            
def TutorialA():
    messagebox.showinfo("Questions", "Questions types are randomly picked and the numbers are randomly generated")
    messagebox.showinfo("Questions", "This makes sure that each question is different, so don't let your guard down!")


def TutorialB():
    messagebox.showinfo("Answering Questions","Answering a question is a bit complicated, The numerator is entered first")
    messagebox.showinfo("Answering questions","and the denominator is entered second")


def TutorialC():
    messagebox.showinfo("Scoring", "Your score is determined by how many questions you are able to answer.")
    messagebox.showinfo("Scoring", "The higher the score the better, so give it your all!")


def TutorialD():
    messagebox.showinfo("Methods", "You will need to be able to add, subtract, multiply and divide fractions")



def howToPlayWindow():
    w = tk.Tk()
    w.title("Tutorial")
    w.config(bg="green")
    w.geometry("350x300")

    title = tk.Label(w, text = "How To Play") 
    title.config(font = ("Arial", 30), bg="green")
    title.pack()

    if logged_in == True:
        savedataLabel = tk.Label(w, text = "Your data will be saved", bg="green")
        savedataLabel.pack()

    else:
        savedataLabel = tk.Label(w, text = "Your data will not be saved", bg="green")
        savedataLabel.pack()


    tutorialA = Button(w, text = "Questions", command = TutorialA)
    tutorialA.pack()


    tutorialB = Button(w, text = "Answering Questions", command = TutorialB)
    tutorialB.pack()


    tutorialC = Button(w, text = "Scoring", command = TutorialC)
    tutorialC.pack()


    tutorialD = Button(w, text = "What you'll need to know", command = TutorialD)
    tutorialD.pack()

    PlayButton = Button(w, text = "Play", command = Gameplay)
    PlayButton.pack()
    


#----------Account Creation----------------------
def createAccountWindow():
    w = tk.Tk()
    w.title("Create an Account")
    w.config(bg="orange")
    w.geometry("350x300")

    title = tk.Label(w, text = "Create an Account") 
    title.config(font = ("Arial", 30), bg="orange")
    title.pack()

    username_label = tk.Label(w, text = "Username", bg="orange") #Label for username entry
    username_label.pack()

    global username
    username = tk.Entry(w, width = "28")    #Username Entry
    username.pack()


    password_label = tk.Label(w, text = "Password", bg="orange") #Label for password entry
    password_label.pack()

    global password
    password = tk.Entry(w, width = "28") #Password Entry
    password.pack()


    confirm_password_label = tk.Label(w, text = "Confirm Password", bg="orange") #Label for confirm password entry
    confirm_password_label.pack()

    global confirm_password
    confirm_password = tk.Entry(w, width = "28") #Confirm Password Entry
    confirm_password.pack()


    AccountTypeChoices = [
                          "Staff",   #Drop-down menu displaying the possible account types
                          "Student", #that are able to be created by the users.
                         ]

    global AccountTypeInitial
    AccountTypeInitial = StringVar(w)
    AccountTypeInitial.set("Staff")
    Account = AccountTypeInitial


    AccountType = OptionMenu(w, AccountTypeInitial, *AccountTypeChoices) #* allows for all items to
    AccountType.pack()                                                   #to be displayed.


    createAccountButton = tk.Button(w, text = "Create  Account", command = createAccount)
    createAccountButton.pack() #submits entered data into create account subprogram for validation.


def createAccount():
    AccountType = AccountTypeInitial.get()
    submit_username = username.get()
    submit_password = password.get()                #Get method gets username/passwords
    submit_confirm_password = confirm_password.get()
    


    if len(submit_username) <= 3:
        messagebox.showinfo("Error", "Can't accept, Username is too short") #validation for security reasons


    elif len(submit_password) <= 5:
        messagebox.showinfo("Error","Can't accept, Password is too short")


    elif submit_password != submit_confirm_password:
        messagebox.showinfo("Error","Password and Confirm Password are not the same")


    elif submit_username in (student_usernames or staff_usernames):
        messagebox.showerror("Username already exists")

    elif submit_username in (student_password or staff_password):
        messagebox.showerror("Username already exists")


    elif len(submit_username) >= 3 and submit_password == submit_confirm_password:
        messagebox.showinfo("Success","Username and Password accepted, Your account has been created!")

        if AccountType == "Staff":
           staff_usernames.append(submit_username) #Adds to the storage once accepted.
           staff_password.append(submit_password)


        elif AccountType == "Student":
           student_usernames.append(submit_username) #Adds to the storage once accepted.
           student_password.append(submit_password)






#----------Login----------------------------------
def loginWindow():
    w = tk.Tk()
    w.title("Login page")
    w.config(bg="green")
    w.geometry("350x300")

    title = tk.Label(w, text = "Login") 
    title.config(font = ("Arial", 30), bg="green")
    title.pack()

    username_label = tk.Label(w, text = "Username", bg="green") #Label for username entry
    username_label.pack()

    global username
    username = tk.Entry(w, width = "28")    #Username Entry
    username.pack()


    password_label = tk.Label(w, text = "Password", bg="green") #Label for password entry
    password_label.pack()

    global password
    password = tk.Entry(w, width = "28") #Password Entry
    password.pack()



    AccountTypeChoices = [
                            "Staff",   #Drop-down menu displaying the possible account types
                            "Student", #that are able to be created by the users.
                            ]

    global AccountTypeInitial
    AccountTypeInitial = StringVar(w)
    AccountTypeInitial.set("Staff")
    Account = AccountTypeInitial


    AccountType = OptionMenu(w, AccountTypeInitial, *AccountTypeChoices) #* allows for all items to
    AccountType.pack()                                                   #to be displayed.


    loginAccountButton = tk.Button(w, text = "login", command = login)
    loginAccountButton.pack() #submits entered data into create account subprogram for validation.



def login():
    AccountType = AccountTypeInitial.get()
    login_username = username.get()
    login_password = password.get()                #Get method gets username/passwords
    
    
    if AccountType == "Staff":
        if login_username == "":
            messagebox.showerror("login failed", "Username is Missing")

        elif login_password == "":
            messagebox.showerror("login failed", "Password is Missing")

        elif login_username not in staff_usernames or login_password not in staff_password:
            messagebox.showerror("login failed", "Username or Password not found")

        elif login_username in staff_usernames and login_password in staff_password:
            messagebox.showerror("login successful", "Username and password found, welcome back!")
            logged_in = True
            current_user = login_username


           

    elif AccountType == "Student":
        if login_username == "":
            messagebox.showerror("login failed", "Username is Missing")

        elif login_password == "":
            messagebox.showerror("login failed", "Password is Missing")

        elif login_username not in student_usernames or login_password not in student_password:
            messagebox.showerror("login failed", "Username or Password not found")

        elif login_username in student_usernames and login_password in student_password:
            messagebox.showerror("login successful", "Username and password found, welcome back!")
            logged_in = True
            current_user = login_username
           





#----------Classes--------------------------------
def joinClassWindow():
    w = tk.Tk()
    w.title("Join a Class")
    w.config(bg="orange")     #Sets up Join class window
    w.geometry("350x300")

    title = tk.Label(w, text = "Join a Class") 
    title.config(font = ("Arial", 30), bg="orange")
    title.pack()


    joinclassName_label = tk.Label(w, text = "Class Name", bg="orange") #Label for Class Name entry
    joinclassName_label.pack()

    global joinclassNameEntry
    joinclassNameEntry = tk.Entry(w, width = "28")    #Class Name Entry
    joinclassNameEntry.pack()


    joinclassCode_label = tk.Label(w, text = "Class Code", bg="orange") #Label for Class Code entry
    joinclassCode_label.pack()

    global joinclassCodeEntry
    joinclassCodeEntry = tk.Entry(w, width = "28")    #Class Code Entry
    joinclassCodeEntry.pack()

    joinclassButton = tk.Button(w, text = "Join Class", command = joinClass)
    joinclassButton.pack()


def joinClass():
    joinClassName = joinclassNameEntry.get() #Gest values from entry boxes
    joinClassCode = joinclassCodeEntry.get()

    if len(joinClassName) == 0 or len(joinClassCode) == 0:
        messagebox.showerror("Join Class", "Required fields empty") #Validation

    elif joinClassName in Classes and joinClassCode in ClassCodes: #Checks if entered data exists
        Classes.append(joinClassName)
        ClassCodes.append(joinClassCode) #appends are for use later
        messagebox.showinfo("Join Class", "Class Joined Successully")
        members.append(current_user)
        scores.append("0")

    else:
        messagebox.showinfo("Join Class", "Class Details Not found") #if data entered not found



def RemoveStudents():
   
    removeWindow = Toplevel(w)
    removeWindow.title("Remove Students") #New window initialised
    removeWindow.config(bg="violet")
    removeWindow.geometry("450x200")


    remove_label = tk.Label(removeWindow, text = "Who would you like to Remove") #Label for username entry
    remove_label.config(font = ("Arial, 20"), bg="violet")
    remove_label.pack()

    remove_subLabel = tk.Label(removeWindow, text = "Enter the Student Number of the Student You Wish To Remove") 
    remove_subLabel.config(font = ("Arial, 15"), bg="violet") #Label for Student Number entry
    remove_subLabel.pack()

    global remove
    remove = tk.Entry(removeWindow, width = "28")    #choose a student to remove
    remove.pack()

    submit_remove = tk.Button(removeWindow, text = "Remove", command = confirmRemove)
    submit_remove.pack()  #submits chosen student

    quitRemove = tk.Button(removeWindow, text = "Quit Removal", command = removeWindow.destroy)
    quitRemove.pack() #Ends the process removal if selected, closes this window only
     

def confirmRemove():
    
    confirmWindow = Toplevel(w)
    confirmWindow.title("Confirm Removal") #Initialises new window
    confirmWindow.config(bg="violet")
    confirmWindow.geometry("450x200")

    title = tk.Label(confirmWindow, text = "Are you Sure you want to Remove this student") 
    title.config(font = ("Arial", 20), bg="violet")
    title.pack()

    ConfirmButton = tk.Button(confirmWindow, text = "Yes", command = Remove) #asks user for confirmation
    ConfirmButton.pack()

    DenyButton = tk.Button(confirmWindow, text = "No", command = confirmWindow.destroy)
    DenyButton.pack() #Closes this window, ends the process


def Remove():
    removed = int(remove.get()) #gets the chosen student to remove and makes the value an integer

    if members[removed] in members: #Checks if the chosen student is within the database
        members.remove(members[removed]) #Removes chosen student based on the confirmation and the data entered.
        scores.remove(scores[removed])

    return(members, scores)


def ViewStudents():

    iterator = 0 #Iterates Through the temporary database

    print("Student No.","||", "Members", "||", "Score")
    print("==" * 20)

    for iterator in range(len(members)):
        print("No",iterator, "||", members[iterator], "||", scores[iterator]) #outputs members and their scores
        if iterator < len(members):
             iterator = iterator + 1

        else:
            iterator = len(members)


def removeHelp():
    removeHelpWindow = Toplevel(w)
    removeHelpWindow.config(bg="violet")
    removeHelpWindow.geometry("300x250")
    removeHelpWindow.title("Help Menu")

    HelpWindowLabel = Label(removeHelpWindow, text = "Choose an Area to Recieve Assistance")
    HelpWindowLabel.config(font = ("Arial", 17), bg="violet")
    HelpWindowLabel.pack()

    
    viewClassHelp = tk.Button(removeHelpWindow, text = "View Class", command = ViewClassInstructions)
    viewClassHelp.pack()
    
    removalHelp = tk.Button(removeHelpWindow, text = "Remove Student", command = RemovalInstructions)
    removalHelp.pack()

    closeHelp = tk.Button(removeHelpWindow, text = "Close Help Window", command = removeHelpWindow.destroy)
    closeHelp.pack()

    
def ViewClassInstructions():
    VCInstructions = messagebox.showinfo(title = "View Class", message = "View Class allows for You to view all students in your class.")
    VCInstructions2 = messagebox.showinfo(title = "View Class", message = "Students will be displayed with their scores and student number.")
    #Instructions on how the View class section works


def RemovalInstructions():
    RemovalInstructions = messagebox.showinfo(title = "Remove Students", message = "To remove a student, enter a student number in the entry box.")
    RemovalInstructions2 = messagebox.showinfo(title = "Remove Students 2", message = "Removing a Student also removes their score.") 
    #Instructions on how to remove a student


def StaffClassManagementPage():
    w = tk.Tk()
    w.config(bg="violet")
    w.geometry("300x250") #sets up the window
    w.title("Manage Class")

    title = tk.Label(w, text = "Manage Your Class") 
    title.config(font = ("Arial", 30), bg="violet")
    title.pack()


    viewStudentsButton = tk.Button(w, text = "View Students", command = ViewStudents)
    viewStudentsButton.pack()                               #Options for teachers to pick from in this section

    removeStudentsButton = tk.Button(w, text = "Remove Students", command = RemoveStudents)
    removeStudentsButton.pack()

    helpManageButton = tk.Button(w, text = "Help", command = removeHelp)
    helpManageButton.pack()

    goBackButton = tk.Button(w, text = "Return to Main Menu", command = w.destroy) #Closes window for now
    goBackButton.pack()



def generateCode():
    classCode = ""
    codeLength = 8
    letters = string.ascii_letters  #Makes use of both letters and numbers
    numbers = string.digits         #to generate codes for classes

    className = classNameEntry.get() #Gets the name of the class


    for x in range(3):
        characterChoice = random.randint(1,2)
        if characterChoice == 1:
            classCode = "".join(random.choice(letters) for x in range(8)) #generates code

        elif characterChoice == 2:
            classCode = "".join(random.choice(numbers) for x in range(8))


    print("\n""Your class name is:", className)
    print("Your Class Code is:", classCode)

    Classes.append(className)
    ClassCodes.append(classCode) #Adds class data to database




def ClassValidate():
    className = classNameEntry.get()

    if len(className) < 12:
        messagebox.showinfo("Can't accept", "Class Name is too short.")
              #Validates the Class name to be a certain length

    elif len(className) > 15:
        messagebox.showinfo("Can't accept", "Class Name is too long.")


    else:
        generateCode() #Calls the generateCode subprogram

def StaffClassCreationPage():
    w = tk.Tk()
    w.title("Create a Class")
    w.config(bg="orange")      #Sets up the class creation window
    w.geometry("350x300")

    title = tk.Label(w, text = "Create a Class") 
    title.config(font = ("Arial", 30), bg="orange")
    title.pack()


    className_label = tk.Label(w, text = "Class Name", bg="orange") #Label for username entry
    className_label.pack()

    classNameEntry = tk.Entry(w, width = "28")    #Username Entry
    classNameEntry.pack()


    classCode_label = tk.Label(w, text = "Class Code", bg="orange") #Label for password entry
    classCode_label.pack()

    creationButton = tk.Button(w, text = "Create Class", command = ClassValidate)
    creationButton.pack()






def classMenu():
    accessPermits = AccountTypeInitial.get()
    AccountType = accessPermits
    w = tk.Tk()
    w.title("Class Main Menu")
    w.config(bg="orange")     #Sets up Join class window
    w.geometry("350x300")

    title = tk.Label(w, text = "Classes") 
    title.config(font = ("Arial", 30), bg="orange")
    title.pack()


    joinClassPage = Button(w, text = "Join Class", command =  joinClassWindow)
    joinClassPage.pack()

    viewClassPage = Button(w, text = "View Class", command =  ViewStudents)
    viewClassPage.pack()

    if AccountType == "Staff":

        manageClassPage = Button(w, text = "Manage Class", command = StaffClassManagementPage)
        manageClassPage.pack()

        CreateClassPage = Button(w, text = "Create a Class", command = StaffClassCreationPage)
        CreateClassPage.pack()


    goBackButton = tk.Button(w, text = "Return to Main Menu", command = w.destroy) #Closes window for now
    goBackButton.pack()

        




#-----------Window Setup---------------------------
w = tk.Tk()
w.config(bg="light blue")
w.geometry("300x250")
title = Label(w, text = "Main Menu") #creates the main menu page
title.config(font = ("Arial", 35), bg="light blue")
title.pack()

startGamepage = Button(w, text = "Start Game", command = howToPlayWindow)
startGamepage.pack()

CreateAccount = Button(w, text = "Create Account", command = createAccountWindow)
CreateAccount.pack()

loginPage = Button(w, text = "Login", command = loginWindow)
loginPage.pack()

ClassMenuPage = Button(w, text = "Class", command = classMenu)
ClassMenuPage.pack()

