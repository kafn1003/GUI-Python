#importing the libraries
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql 
from tkinter import ttk

#This will create the window or the frame
master = tkinter.Tk()
#This will be the size of the window/frame
master.geometry("350x300")

#Labels
regform = Label (master, text = "REGISTRATION FORM", font = "Helvetica 15 bold")
regform.place(x = 30, y = 10)

#Requirements
#This will display the form in which the user will input his/her Student Number
content1 = StringVar()
studentnum = Label(master, text = "Student Number:")
studentnum.place(x = 30, y = 40)
box1 = Entry(master, textvariable = content1)
box1.place(x = 180, y = 40)

#This will display the form in which the user will input his/her Last Name
content2 = StringVar() 
lastname = Label(master, text = "Last Name:")
lastname.place(x = 30, y = 70)
box2 = Entry(master, textvariable = content2)
box2.place(x = 180, y = 70)

#This will display the form in which the user will input his/her First Name
content3 = StringVar()
firstname = Label(master, text = "First Name:")
firstname.place(x = 30, y = 100)
box3 = Entry(master, textvariable = content3)
box3.place(x = 180, y = 100)

#This will display the form in which the user will input his/her Middle Name
content4 = StringVar()
middlename = Label(master, text = "Middle Name:")
middlename.place(x = 30, y = 130)
box4 = Entry(master, textvariable = content4)
box4.place(x = 180, y = 130)

#This will display the form in which the user will input his/her Birthday
content5 = StringVar()
birthday = Label(master, text = "Birthday: (yyyy/mm/dd)")
birthday.place(x = 30, y = 160)
box5 = Entry(master, textvariable = content5)
box5.place(x = 180, y = 160)

#This will display the form in which the user will input his/her Age
content6 = StringVar()
age = Label(master, text = "Age:")
age.place(x = 30, y = 190)
box6 = Entry(master, textvariable = content6)
box6.place(x = 180, y = 190)

#This will display the form in which the user will input his/her Address
content7 = StringVar()
address = Label(master, text = "Address:")
address.place(x = 30, y = 220)
box7 = Entry(master, textvariable = content7)
box7.place(x = 180, y = 220)

#This function will insert the certain records into the database
def inserttodb():
    #Open another window
    master1 = tkinter.Tk()
    #The new window's size
    master1.geometry("280x250")
    #Title of the new window
    master1.title("Information")

    #A listbox will be shown
    showlist = Listbox(master1, height = 9, width = 30)
    #Position of the listbox
    showlist.place(x = 30, y = 40)
    #Listbox Label
    listlabel = Label(master1, text="Student")
    #Position of the Listbox Label
    listlabel.place(x = 30 ,y = 10) 
    
    #The information that will be collected from the form
    showlist.insert(END, content1.get())
    showlist.insert(END, content2.get())
    showlist.insert(END, content3.get())
    showlist.insert(END, content4.get())
    showlist.insert(END, content5.get())
    showlist.insert(END, content6.get())
    showlist.insert(END, content7.get())
    
    #This will collect the data that was inputted by the user in the form
    studentno = content1.get()
    lastname = content2.get()
    firstname = content3.get()
    middlename = content4.get()
    birthday = content5.get()
    age = content6.get()
    address = content7.get()
    
    #Open database connection
    db = pymysql.connect("localhost", "root", "", "studentdb")
    #The cursor objects will interact with the server.
    cursor = db.cursor()
    #The SQL query that prepares to INSERT the data into the database
    insert = ("""INSERT INTO tblstudent (StudentNumber, LastName, FirstName, MiddleName, Birthday, Age, Address )
    VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (studentno, lastname, firstname, middlename, birthday, age, address))
    #Execute the SQL command
    cursor.execute(insert)
    #Accept the changes
    db.commit()
    
    #Delete the fields
    box1.delete(0, 'end')
    box2.delete(0, 'end')
    box3.delete(0, 'end')
    box4.delete(0, 'end')
    box5.delete(0, 'end')
    box6.delete(0, 'end')
    box7.delete(0, 'end')
    
    #Close the database connection
    db.close()
    
    #This is a function that makes the user confirm the information that he/she will submit.
    def confirmation():
        
        #Opening another window
        master2 = tkinter.Tk()
        #Size
        master2.geometry("800x600")
        #Name of the window
        master2.title("Masterlist")
        #The message that will appear after clicking confirm
        messagebox.showinfo("STATUS", "Registration successful!")
        #Name of the listbox
        tablename = Label (master2, text = "STUDENTS:", font = "Helvetica 12")
        #Position of the Listbox Label
        tablename.place(x = 30, y = 10)        
        #The Listbox
        showlist2 = Listbox(master2, width = 100, height = 20)
        #POosition of the listbox
        showlist2.place(x = 30, y = 40)
        
        #Open database connection
        db = pymysql.connect("localhost", "root", "", "studentdb")
        #The cursor objects will interact with the server.
        cursor = db.cursor()
        #The SQL query that prepares to show the data of the database
        show = "SELECT *FROM tblstudent"
        #Eexcute the SQL command
        cursor.execute(show)
        
        #Fetch query result
        results = cursor.fetchall()
        #These lines will make the table for the list of students
        showlist2.delete(0, showlist2.size())
        for row in results:
            addstud = str(row[0])+"     " + str(row[1]) + "    /    " + row[2] + "    /    " + row[3] + "    /    " + row[4] + "    /    " + str(row[5]) + "    /    " + str(row[6]) + "    /    " + row[7]
            showlist2.insert(showlist2.size()+1, addstud)
        #Close the database connection
        db.close()
       
        #Function for deleting 
        def deletetodb():
            #Open database connection
            db = pymysql.connect("localhost", "root", "", "studentdb")
            #The cursor objects will interact with the server.
            cursor = db.cursor()
            #The SQL query that prepares to DELETE certain data from the database
            delete = ("DELETE FROM tblstudent WHERE StudentNumber = '" + content1.get() + "'")
            #Execute the SQL command
            cursor.execute(delete)
            #Accept the changes
            db.commit()
            
            #Delete the fields
            box1.delete(0, 'end')
            box2.delete(0, 'end')
            box3.delete(0, 'end')
            box4.delete(0, 'end')
            box5.delete(0, 'end')
            box6.delete(0, 'end')
            box7.delete(0, 'end')
            #This will refresh the listbox 
            confirmation()
            #Close the database connection
            db.close()
            
        #Function for updating
        def updatetodb():
            #This will collect the data that was inputted by the user in the form
            studentno = content1.get()
            lastname = content2.get()
            firstname = content3.get()
            middlename = content4.get()
            birthday = content5.get()
            age = content6.get()
            address = content7.get()        
            
            #Open the database connection
            db = pymysql.connect("localhost", "root", "", "studentdb")
            #The cursor objects will interact with the server.
            cursor = db.cursor()
            #The SQL query that prepares to DELETE certain data from the database
            update = ("UPDATE tblstudent SET LastName = '" + content2.get() + "', FirstName = '" + content3.get() + "', MiddleName = '" + content4.get() + "', Birthday = '" + content5.get() + "', Age = '" + content6.get() +"', Address = '" + content7.get()+ "' WHERE StudentNumber = '"+ content1.get()+ "'")
            #Execute the SQL command
            cursor.execute(update)
            #Accept the changes
            db.commit()
            
            #Delete the fields
            box1.delete(0, 'end')
            box2.delete(0, 'end')
            box3.delete(0, 'end')
            box4.delete(0, 'end')
            box5.delete(0, 'end')
            box6.delete(0, 'end')
            box7.delete(0, 'end')
            #Refresh the listbox
            confirmation()
            #Close the database connection
            db.close()
        
        #The DELETE button
        delete = Button(master2, text="DELETE", command = deletetodb)
        #The position of the DELETE button
        delete.place(x = 90, y = 380)   
        #The UPDATE button
        update = Button(master2, text="UPDATE", command = updatetodb)
        #The position of the UPDATE button
        update.place(x = 30, y = 380)
    
    #The CONFIRM button
    confirm = Button(master1, text = "CONFIRM", command = confirmation)
    #The position of the CONFIRM button
    confirm.place(x = 30, y = 200)
    
#The function that will help the user if he wants to delete or update certain records    
def get():
    #This will collect the data that was inputted by the user in the form   
    studentno = content1.get()
    lastname = content2.get()
    firstname = content3.get()
    middlename = content4.get()
    birthday = content5.get()
    age = content6.get()
    address = content7.get()
    
    #Open the database connection
    db = pymysql.connect("localhost", "root", "", "studentdb")
    #The cursor objects will interact with the server.
    cursor = db.cursor()
    #The SQL query that prepares to show certain data from the database or the listbox
    get = ("SELECT *FROM tblstudent WHERE StudentNumber = '" + box1.get() +"'")
    #Execute the SQL command
    cursor.execute(get)
    #Fetch query result
    results = cursor.fetchall()
    
    #When the StudentNumber was gotten, the following will also be gathered for editing or deleting
    for row in results:
        box2.insert(0, row[2])
        box3.insert(0, row[3])
        box4.insert(0, row[4])
        box5.insert(0, row[5])
        box6.insert(0, row[6])
        box7.insert(0, row[7])
    #Close the database connection    
    db.close()

#GET Button
get = Button(master, text = "GET INFO", command = get)
#Position of the GET button
get.place(x = 180, y = 250)        

#SUBMIT button
submit = Button(master, text = "SUBMIT", command = inserttodb)
#The position of the SUBMIT button
submit.place(x = 115, y = 250)

#This is needed so the code will run
master.mainloop()
