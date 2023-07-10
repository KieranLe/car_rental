from asyncore import read
import math
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.ttk import *
from datetime import datetime
import re

import tkinter.messagebox
import mysql.connector

# Establish connection between the program and MySQL Workbench
conn = mysql.connector.connect(  user = 'root', 
                                password = 'Kevin2002',
                                host = 'localhost', database ='project_3330_part2')

print("Open succesfully")
# Create a cursor 
cur = conn.cursor()

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)


def deleteTex(text):
    text.delete('0', END)

# A simple login screen required to verify before other features can be used.
def loginW():

    def validateLogin():
        userName = usernameInput.get()
        password = passwordInput.get()
        if( userName=='' and password=='' ):
            output.set("Missing username and password ")
            tkinter.messagebox.showerror('Error','Name and Password cannot be blank')
        elif( userName=='' ):
            output.set("Missing username")
            tkinter.messagebox.showerror('Error','Name cannot be blank')
        elif( password=='' ):
            output.set("Missing password")
            tkinter.messagebox.showerror('Error','Password cannot be blank')
        else:
            if( userName == 'admin' and password== 'password'):
                loginSuccess()
                loginWindow.destroy()
                mainMenu()
                    
            else:
                loginFailure()

    def loginSuccess():
        tkinter.messagebox.showinfo("Welcome!", "Login success!")

    def loginFailure():
        tkinter.messagebox.showerror("Error!","Incorrect username or password.")
        output.set("Wrong username and password")

    def handleKeypress(event):
        validateLogin()

    loginWindow = tk.Tk()
    loginWindow.title("Sign In")
    loginWindow.geometry( '230x150')
    loginWindow.resizable(0, 0)
    loginWindow.eval('tk::PlaceWindow . center')

    loginWindow.iconbitmap('loginIcon.ico')

    loginLabel = Label( loginWindow, text="Please sign in")
    loginLabel.grid( row = 0, column = 0, columnspan= 2, padx=5, pady=5)

    userNameLabel = Label( loginWindow, text='Username:', width=10 )
    userNameLabel.grid( row = 1, column = 0, sticky = tk.W, padx=5, pady=5 )
    usernameInput = tk.StringVar()
    usernameEntry = Entry( loginWindow, textvariable=usernameInput)
    usernameEntry.grid( row = 1, column=1, sticky=tk.W, padx=5, pady=5)

    passwordLabel = Label( loginWindow, text="Password:", width=10 )
    passwordLabel.grid( row=2, column=0, sticky=tk.W, padx=5, pady=5)
    passwordInput = tk.StringVar()
    passwordEntry = Entry( loginWindow, textvariable=passwordInput, show='*')
    passwordEntry.grid( row=2, column=1, sticky=tk.W, padx=5, pady=5)

    SignInButton = Button( loginWindow, text="Login", command=validateLogin, width=10)
    SignInButton.grid( row=4, column=0, columnspan=2, padx=5, pady=5)
    

    output = tk.StringVar()
    f_result_label = tk.Label( loginWindow, textvariable=output, width= 30, fg='red' )
    f_result_label.grid( row=3, column=0, columnspan=2, sticky=tk.W )

    # Handle <Enter> key press
    loginWindow.bind("<Return>", handleKeypress)
    loginWindow.mainloop()

# Requirement 1: Add new Customer
# Either name or Phone can be empty
# Phone need to follow (xxx) xxx-xxxx format
# Error message will show up if fill incorrectly
def addNewCust():

    def openMainMenu():
        addCustWindow.destroy()
        mainMenu()

    def submit():
        custName  = f_name.get()
        custPhone = f_phone.get(); 
        query = "INSERT INTO CUSTOMER(Name, Phone) VALUES ( %s, %s)  "
        data = (custName,custPhone)
        if( custName == '' or custPhone == ''):
            my_str.set("Pleae try again!")
            tkinter.messagebox.showerror('Error', 'Name and Phone cannot be empty. Try again!')
        elif ( validatePhoneNumber(custPhone) == 0):
            tkinter.messagebox.showerror("Error","Phone not real")
        else:
            try:
                cur.execute(query,data)
                conn.commit() 
                deleteTex(f_name)
                deleteTex(f_phone)
                tkinter.messagebox.showinfo("OK", "Added successfully!")
            except:
                conn.rollback()

    def validatePhoneNumber(phoneNum):
        pattern = re.compile("^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$")
        result = pattern.match(phoneNum)
        if( result is None):
            return 0
        else:
            return 1

    def handleKeyPress(event):
        submit()

    addCustWindow = tk.Tk()
    addCustWindow.title( 'Add new customer' )
    addCustWindow.geometry( '250x150' )
    addCustWindow.resizable(0, 0)
    addCustWindow.eval('tk::PlaceWindow . center')

    addCustWindow.iconbitmap('customerIcon.ico')

    # Requirement 1 - Add a new customer ( Name and Phone ONLY )

    addCustWindow.columnconfigure(0, weight = 1)
    addCustWindow.columnconfigure(1, weight = 3)

    f_title = Label( addCustWindow, text = 'New Customer' )
    f_title.grid( row=0, column=0, columnspan=3, padx=5, pady=5)

    f_name_label = Label( addCustWindow, text = 'Customer\'s Name:' )
    f_name_label.grid( row=1, column=0, sticky=tk.W, padx=5, pady=5 )

    f_name = Entry( addCustWindow )
    f_name.grid( row=1, column=1, sticky=tk.E, padx=5, pady=5)

    f_phone_label = Label( addCustWindow, text = 'Customer\'s Phone:' )
    f_phone_label.grid( row=2, column=0, sticky=tk.W, padx=5, pady=5 )

    f_phone = Entry( addCustWindow )
    f_phone.grid( row=2, column=1, sticky=tk.E, padx=5, pady=5)

    submit_btn = Button( addCustWindow, text = 'Add', width = 10, command = submit )
    submit_btn.grid( row=4, column=1, sticky=tk.E, padx=5, pady=5)

    cancelButton = Button( addCustWindow, text = 'Cancel', width = 10, command = openMainMenu )
    cancelButton.grid(row=4, column=0, sticky=tk.E, padx=5, pady=5)

    my_str = tk.StringVar()
    f_result_label = tk.Label( addCustWindow, textvariable=my_str,  width= 20, fg='red')
    f_result_label.grid( row=3, column=1)


    addCustWindow.bind('<Return>', handleKeyPress)
    addCustWindow.mainloop()

# Requirement 2: Add new Vehicle
# All info need to be filled or else error message will show up 

def addNewVehicle():

    def openMainMenu():
        addVehicleWindow.destroy()
        mainMenu()

    def submit():
        vehicle_ID = vehicleIdEntry.get()
        vehicle_Description = vehicleDesEntry.get()
        vehicle_Year = vehicleYearEntry.get()
        vehicle_Type = typeChoice.get()
        vehicle_TypeInt = 0
        match vehicle_Type:
            case 'Compact':
                vehicle_TypeInt = 1
            case 'Medium':
                vehicle_TypeInt = 2
            case 'Large':
                vehicle_TypeInt = 3
            case 'SUV':
                vehicle_TypeInt = 4
            case 'Truck':
                vehicle_TypeInt = 5
            case 'Van':
                vehicle_TypeInt = 6

        vehicle_Category =  categoryChoice.get()

        query = "INSERT INTO VEHICLE VALUES(%s, %s, %s, %s, %s)"
        data = (vehicle_ID,vehicle_Description,vehicle_Year,vehicle_TypeInt,vehicle_Category)
        
        if( vehicle_ID=='' or vehicle_Description=='' or vehicle_Type=='' or
            vehicle_TypeInt==None or vehicle_Year==None or vehicle_Category==''):
            tkinter.messagebox.showerror('Error','Please fill in all the blank')
        else:
            try:
                cur.execute(query, data)
                conn.commit()
                deleteTex(vehicleIdEntry)
                deleteTex(vehicleDesEntry)
                deleteTex(vehicleYearEntry)
                tkinter.messagebox.showinfo("OK", "Added successfully!")
            except:
                conn.rollback()

    def handleKeyPress(event):
        submit()

    addVehicleWindow = tk.Tk()
    addVehicleWindow.title( 'New Vehicle' )
    addVehicleWindow.geometry( '250x220' )
    addVehicleWindow.resizable( 0,0 )
    addVehicleWindow.eval('tk::PlaceWindow . center')

    addVehicleWindow.iconbitmap('caricon.ico')

    frameTop = tk.Frame(addVehicleWindow)
    frameTop.grid()

    vehicleLabel = tk.Label( frameTop, text= 'Add new vehicle')
    vehicleLabel.config(bg="orange", width=35, fg="white")
    vehicleLabel.grid( row=0, column=0, columnspan=3)

    vehicleIdLabel = Label( frameTop, text='Vehicle ID')
    vehicleIdLabel.grid( row=1, column=0, padx=5, pady=5, sticky=tk.W)

    vehicleIdEntry = Entry( frameTop )
    vehicleIdEntry.grid( row=1, column=1, padx=5, pady=5, sticky=tk.E, ipadx= 20 )

    vehicleDesLabel = Label( frameTop, text='Description')
    vehicleDesLabel.grid( row=2, column=0, padx=5, pady=5, sticky=tk.W)

    vehicleDesEntry = Entry( frameTop )
    vehicleDesEntry.grid( row=2, column=1, padx=5, pady=5, sticky=tk.E, ipadx= 20 )

    vehicleYearLabel = Label( frameTop, text='Year')
    vehicleYearLabel.grid( row=3, column=0, padx=5, pady=5, sticky=tk.W)

    vehicleYearEntry = Entry( frameTop, width=5 )
    vehicleYearEntry.grid( row=3, column=1, padx=5, pady=5, sticky=tk.W )

    typeOption = [ "Compact", "Medium", "Large", "SUV", "Truck", "Van"]
    vehicleTypeLabel = Label( frameTop, text='Type')
    vehicleTypeLabel.grid( row=4, column=0, padx=5, pady=5, sticky=tk.W)

    typeChoice = tk.StringVar()
    vehicleTypeOption = ttk.Combobox( frameTop, textvariable=typeChoice, values = typeOption, width=13, state="readonly" )
    vehicleTypeOption.grid( row=4, column=1, padx=5, pady=5, sticky=tk.W)

    frameCaterogy = tk.Frame( addVehicleWindow, relief='sunken' )
    frameCaterogy.grid()

    vehicleCategoryLabel = Label( frameCaterogy, text='Category')
    vehicleCategoryLabel.grid( row=5, column=0, padx=5, pady=5, ipadx=11, sticky=tk.W)

    categoryChoice = tk.StringVar()
    categoryList = ( ('Basic', 0), ('Luxury',1) )
    posCategory = 1
    for list in categoryList:
        r = ttk.Radiobutton( frameCaterogy, text=list[0], value=list[1], variable=categoryChoice)
        r.grid(row=5, column=posCategory, padx=5, pady=5, sticky=tk.W)
        posCategory += 1

    vehicleConfirmButton = Button (frameCaterogy, text='OK', width=15, command=submit)
    vehicleConfirmButton.grid( row=6, column=2, padx=5, pady=5, sticky=tk.E)

    cancelButton = Button( frameCaterogy, text = 'Cancel', width = 10, command = openMainMenu )
    cancelButton.grid(row=6, column=0, sticky=tk.E, padx=5, pady=5)

    addVehicleWindow.bind('<Return>', handleKeyPress)
    addVehicleWindow.mainloop()

# Requirement 3: Add New Rental
# How to use:
# 1) Pick a Type and Category then press [Search] button -> List of available vehicle will be displayed on treeview
# 2) Assuming customer is already existed, type in customer's name then press [Find] button
#    Customer's phone and ID will be displayed -> ID will automatically fill in the [CustID] textbox under [New Rental Info]
# 3) Double click on a vehicle -> automatically fill in the [VehicleID] textbox under [New Rental Info]
# 4) Fill out the rest 
# 5) Press [Calculate Total] to calculate the total amount based on quantity and rental type
# 6) Press submit to add into database 
def addRental():

    def openMainMenu():
        addRentalWindow.destroy()
        mainMenu()

    def clearTreeView():
        for element in tree.get_children():
            tree.delete(element)

    def search():
        clearTreeView()
        query = "SELECT VehicleID, Description, Year FROM VEHICLE WHERE Type = %s AND Category = %s AND VehicleID NOT IN ( SELECT DISTINCT VehicleID FROM Rental WHERE (%s <= ReturnDate) AND (%s >= StartDate) AND Returned = 0)"
        intType = typeChoice.get()
        match intType:
            case 'Compact':
                intType = 1
            case 'Medium':
                intType = 2
            case 'Large':
                intType = 3
            case 'SUV':
                intType = 4
            case 'Truck':
                intType = 5
            case 'Van':
                intType = 6
        cur.execute( query, ( intType, categoryChoice.get(), startDateEntry.get(), endDateEntry.get()  ) )
        filledStartDate.set(startDateEntry.get())
        filledReturnDate.set(endDateEntry.get())
        carsAvailable = cur.fetchall()

        for car in carsAvailable:
            tree.insert( '', tk.END, values=(car[0], car[1], car[2]) )

    def findCust():
        query = "SELECT CustID, Phone FROM CUSTOMER WHERE Name like %s"
        searchName =  custNameEntry.get()
        cur.execute( query, (searchName,))
        foundCust = cur.fetchall()
        for element in foundCust:
            filledPhone.set( element[1] )
            filledID.set( element[0] )
            filledCustID.set( element[0])


    # Create add rental window, set its title and size
    addRentalWindow = Tk()
    addRentalWindow.title( 'Add new rental' )
    addRentalWindow.geometry( '1050x640' ) # width x Height
    addRentalWindow.iconbitmap('carRental.ico')
    addRentalWindow.resizable(0, 0)
    
    treeFrame = tk.Frame(addRentalWindow)
    treeFrame.pack(pady=10)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", rowheight= 25, background= "#EDEBDF", 
                                fieldbackground= "#EDEBDF", foreground='black')
    style.configure("Treeview.Heading", font=('Calibri', 13, 'bold')) # Modify font for headings
    style.map("Treeview", background=[('selected', '#347083')])

    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side=RIGHT, fill=BOTH)

    tree = ttk.Treeview(treeFrame, yscrollcommand=treeScroll.set, selectmode="extended", show='headings')
    tree.pack()

    treeScroll.config(command=tree.yview)
    
    tree['column'] = ('vehicleID','description','year')

    # Configure columns
    tree.column( "vehicleID",    width=200, anchor=W )
    tree.column( "description",  width=200, anchor=W )
    tree.column( "year",         width=100, anchor=W )
    

    # Specify the headings for each column
    tree.heading( 'vehicleID',   text='Vehicle ID' ) 
    tree.heading( 'description', text='Description' )
    tree.heading( 'year',        text='Year' )


    # Frame: Type + Choice provided by Customer 
    custChoiceFrame = LabelFrame(addRentalWindow, text="Choice")
    custChoiceFrame.pack(expand=FALSE, padx=20, fill=BOTH)
    

    typeOption = [ "Compact", "Medium", "Large", "SUV", "Truck", "Van"]
    rentalChoiceLabel = Label( custChoiceFrame, text='Type')
    rentalChoiceLabel.grid( row=0, column=0, padx=5, pady=5, sticky=tk.E)

    typeChoice = tk.StringVar()
    rentalType = ttk.Combobox( custChoiceFrame, textvariable=typeChoice, values = typeOption, width=13, state="readonly" )
    rentalType.grid( row=0, column=1, padx=5, pady=5, sticky=tk.E)

    categoryOption = [ "0", "1"]
    rentalCategoryLabel = Label( custChoiceFrame, text='Category')
    rentalCategoryLabel.grid( row=-0, column=2, padx=5, pady=5, sticky=tk.E)

    categoryChoice = tk.StringVar()
    rentalCategory = ttk.Combobox( custChoiceFrame, textvariable=categoryChoice, values = categoryOption, width=5, state="readonly" )
    rentalCategory.grid( row=0, column=4, padx=3, pady=5, sticky=tk.E)

    searchButton = Button(custChoiceFrame, text='Search', width=20, command=search)
    searchButton.grid( row=0, column=30, padx=5, pady=5, sticky=tk.E)

    startDateLabel = Label( custChoiceFrame, text='Start Date')
    startDateLabel.grid(row=0, column=10, padx=5, pady=5, sticky=tk.E)
    startDateEntry = Entry( custChoiceFrame )
    startDateEntry.grid( row=0, column=15, padx=5, pady=5, sticky=tk.E )

    endDateLabel = Label( custChoiceFrame, text='Return Date')
    endDateLabel.grid(row=0, column=20, padx=5, pady=5, sticky=tk.E)
    endDateEntry = Entry( custChoiceFrame )
    endDateEntry.grid( row=0, column=25, padx=5, pady=5, sticky=tk.E )

    # Frame: look for existing customer
    findCustFrame = LabelFrame(addRentalWindow, text="Finding Customer's Info")
    findCustFrame.pack(expand=FALSE, padx=20, fill=BOTH)

    custNameLabel = Label( findCustFrame, text='Name')
    custNameLabel.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
    
    custNameEntry = Entry( findCustFrame )
    custNameEntry.grid( row=0, column=1, padx=5, pady=5, sticky=tk.E )

    custButton = Button( findCustFrame, text='Find', width= 20, command=findCust)
    custButton.grid( row=0, column=3, padx=5, pady=5, sticky=tk.E )

    custPhoneLabel = Label( findCustFrame, text='Phone')
    custPhoneLabel.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
    
    filledPhone = StringVar()
    custPhoneEntry = Entry( findCustFrame, state='readonly', textvariable= filledPhone )
    custPhoneEntry.grid( row=1, column=1, padx=5, pady=5, sticky=tk.E )

    custIDLabel = Label( findCustFrame, text='Customer ID')
    custIDLabel.grid(row=1, column=2, padx=5, pady=5, sticky=tk.E)
    
    filledID = StringVar()
    custIDEntry = Entry( findCustFrame, state='readonly', textvariable= filledID )
    custIDEntry.grid( row=1, column=3, padx=5, pady=5, sticky=tk.E )


    # Frame: adding new rental 
    newRentalFrame = LabelFrame(addRentalWindow, text="New Rental Information")
    newRentalFrame.pack(expand=FALSE, padx=20, fill=BOTH)
    # custid, vehicleid, startdate, orderdate, rental type, qty, return date, total amount, paymentdate, returned
    # info that will automatically fill in when picking from treeview = vehicle id, description, year
    filledCustID = StringVar()
    rentalCustIDLabel = Label( newRentalFrame, text='CustID')
    rentalCustIDLabel.grid( row =0, column=0, padx=5, pady=5, sticky=tk.W)
    rentalCustIDEntry = Entry( newRentalFrame, state='readonly', textvariable= filledCustID)
    rentalCustIDEntry.grid( row =0, column=1, padx=5, pady=5, sticky=tk.W)
  
    filledVehID = StringVar()
    rentalVehcIDLabel = Label( newRentalFrame, text='VehicleID')
    rentalVehcIDLabel.grid( row =1, column=0, padx=5, pady=5, sticky=tk.W)
    rentalVehcIDEntry = Entry( newRentalFrame, state='readonly', textvariable= filledVehID)
    rentalVehcIDEntry.grid( row =1, column=1, padx=5, pady=5, sticky=tk.W)

    filledStartDate = StringVar()
    rentalStartDateLabel = Label( newRentalFrame, text='Start Date')
    rentalStartDateLabel.grid( row =0, column=2, padx=5, pady=5, sticky=tk.W)
    rentalStartDateEntry = Entry( newRentalFrame, state='readonly', textvariable=filledStartDate)
    rentalStartDateEntry.grid( row =0, column=3, padx=5, pady=5, sticky=tk.W)

    filledReturnDate = StringVar()
    rentalReturnDateLabel = Label( newRentalFrame, text='Return Date')
    rentalReturnDateLabel.grid( row =0, column=4, padx=5, pady=5, sticky=tk.W)
    rentalReturnDateEntry = Entry( newRentalFrame, state='readonly', textvariable=filledReturnDate)
    rentalReturnDateEntry.grid( row =0, column=5, padx=5, pady=5, sticky=tk.W)

    rentalOrderDateLabel = Label( newRentalFrame, text='Order Date')
    rentalOrderDateLabel.grid( row =0, column=6, padx=5, pady=5, sticky=tk.W)
    rentalOrderDateEntry = Entry( newRentalFrame)
    rentalOrderDateEntry.grid( row =0, column=7, padx=5, pady=5, sticky=tk.W)

    rentalTypeLabel = Label( newRentalFrame, text='Rental Type')
    rentalTypeLabel.grid( row =1, column=2, padx=5, pady=5, sticky=tk.W)

    comboOption= ["Daily", "Weekly"]
    comboChoice = tk.StringVar()
    rentalTypeCombo = ttk.Combobox( newRentalFrame, textvariable=comboChoice, values=comboOption, width=5, state="readonly" )
    rentalTypeCombo.config(width=18)
    rentalTypeCombo.grid( row=1, column=3, padx=5, pady=5, sticky=tk.W)

    
    calculatedQty = StringVar()
    rentalQtyLabel = Label( newRentalFrame, text='Quantity')
    rentalQtyLabel.grid( row =1, column=4, padx=5, pady=5, sticky=tk.W)
    rentalQtyEntry = Entry( newRentalFrame, state='readonly', textvariable= calculatedQty)
    rentalQtyEntry.grid( row =1, column=5, padx=5, pady=5, sticky=tk.W)

 
    rentalPaymentDateLabel = Label( newRentalFrame, text='Payment Date')
    rentalPaymentDateLabel.grid( row =1, column=6, padx=5, pady=5, sticky=tk.W)
    rentalPaymentDateEntry = Entry( newRentalFrame )
    rentalPaymentDateEntry.grid( row =1, column=7, padx=5, pady=5, sticky=tk.W)


    calculatedAmount = StringVar()
    rentalTotalAmount = Label( newRentalFrame, text='Total Amount')
    rentalTotalAmount.grid( row =2, column=0, padx=5, pady=5, sticky=tk.W)
    rentalTotalAmount = Entry( newRentalFrame, state='readonly', textvariable= calculatedAmount)
    rentalTotalAmount.grid( row =2, column=1, padx=5, pady=5, sticky=tk.W)

    # Get data when double click on item in treeview
    def selectItem(a):
        selected = tree.focus()
        values = tree.item(selected, 'values')
        for value in values:
            filledVehID.set( value )
            break

    tree.bind('<Button-1>', selectItem)

    # Add new rental into database 
    def submit():
        query = "INSERT INTO RENTAL(CustID, VehicleID, StartDate, OrderDate, RentalType, Qty, ReturnDate, TotalAmount, PaymentDate, Returned) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)  "
        intType = rentalTypeCombo.get()
        match intType:
            case 'Daily':
                intType = 1
            case 'Weekly':
                intType = 7
        if( rentalPaymentDateEntry.get() == '' ):
            payDate = None
            returned = 0
        else:
            payDate = rentalPaymentDateEntry.get()
            returned = 1
        data = ( rentalCustIDEntry.get(), rentalVehcIDEntry.get(), rentalStartDateEntry.get(), rentalOrderDateEntry.get(), 
                 intType, rentalQtyEntry.get(), rentalReturnDateEntry.get(), rentalTotalAmount.get(), payDate, returned)
        cur.execute( query, data)
        conn.commit()
        tkinter.messagebox.showinfo("OK", "Added successfully!")


    submitButton = Button(newRentalFrame, text="Submit", width=15, command=submit)
    submitButton.grid( row=1, column=8, padx=5, pady=5, sticky=tk.E)

    def calculateAmount():
        calculateQty()
        inputType = rentalTypeCombo.get()
        intType = typeChoice.get()
        match intType:
            case 'Compact':
                intType = 1
            case 'Medium':
                intType = 2
            case 'Large':
                intType = 3
            case 'SUV':
                intType = 4
            case 'Truck':
                intType = 5
            case 'Van':
                intType = 6

        weeklyQuery = "SELECT WEEKLY FROM RATE WHERE Type = %s AND Category = %s"
        dailyQuery  = "SELECT DAILY FROM RATE WHERE Type = %s AND Category = %s"
        total = 0
        if( inputType == "Weekly"):
            cur.execute( weeklyQuery, (intType, categoryChoice.get()) )
            rates = cur.fetchall()
            for rate in rates:
                total = rate[0] * int(rentalQtyEntry.get())
                calculatedAmount.set( total )
        else:
            cur.execute( dailyQuery, (intType, categoryChoice.get()) )
            rates = cur.fetchall()
            for rate in rates:
                total = rate[0] * int(rentalQtyEntry.get())
                calculatedAmount.set( total )
    
    def calculateQty():
        rentalType = rentalTypeCombo.get()
        quantity = days_between(rentalStartDateEntry.get(), rentalReturnDateEntry.get())
        if quantity == 0:
                quantity = 1
        if rentalType == "Weekly":
            quantity = math.ceil(quantity / 7)
        calculatedQty.set( quantity )
        

    calculatedAmountButton = Button(newRentalFrame, text="Calculate Total", width=15, command=calculateAmount)
    calculatedAmountButton.grid( row=2, column=2, padx=5, pady=5, sticky=tk.W)

    returnFrame = LabelFrame(addRentalWindow)
    returnFrame.pack(expand=FALSE, padx=20, fill=BOTH)

    returnButton = Button(returnFrame, text="Return to Main Menu", width=20, command=openMainMenu)
    returnButton.grid( row=1, column=1, padx=5, pady=5, sticky=tk.W)

    addRentalWindow.mainloop()
    
# Requirement #4: Handle the return of a rented car
def handleReturn():

    def openMainMenu():
        handleReturnWindow.destroy()
        mainMenu()

    def clearTreeView():
        for element in tree.get_children():
            tree.delete(element)
    
    def search():
        clearTreeView()
        query = "SELECT * FROM vRentalInfo WHERE Type = %s AND Category = %s AND (ReturnDate LIKE %s) AND (CustomerName LIKE %s);"
        intType = typeChoice.get()
        match intType:
            case 'Compact':
                intType = 1
            case 'Medium':
                intType = 2
            case 'Large':
                intType = 3
            case 'SUV':
                intType = 4
            case 'Truck':
                intType = 5
            case 'Van':
                intType = 6
        cur.execute( query, ( typeChoice.get(), categoryChoice.get(), '%'+returnDateEntry.get()+'%', '%'+custNameEntry.get()+'%'  ) )
        carsAvailable = cur.fetchall()

        for car in carsAvailable:
            tree.insert( '', tk.END, values=(car[0], car[1], car[2],car[3], car[4], car[5], car[6], car[7], car[8], car[9], car[10], car[11]) )

    def update():
        query = "UPDATE RENTAL SET Returned = 1, PaymentDate = %s WHERE CustID = %s AND VehicleID = %s AND StartDate = %s;"
        data = ( paymentDateEntry.get(), rentalCustIdEntry.get(), rentalVehicleIdEntry.get(), rentalStartDateEntry.get() )
        cur.execute( query, data )
        conn.commit()
        tkinter.messagebox.showinfo("OK", "Added successfully!")
    


    # Create handle rental window, set its title and size
    handleReturnWindow = Tk()
    handleReturnWindow.title( 'Handle Return' )
    handleReturnWindow.geometry( '1600x580' ) # width x Height
    handleReturnWindow.iconbitmap('carRental.ico')
    handleReturnWindow.resizable(0, 0)
    
    treeFrame = tk.Frame(handleReturnWindow)
    treeFrame.pack(pady=10)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", rowheight= 20, background= "#EDEBDF", 
                                fieldbackground= "#EDEBDF", foreground='black')
    style.configure("Treeview.Heading", font=('Calibri', 10, 'bold')) # Modify font for headings
    style.map("Treeview", background=[('selected', '#347083')])

    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side=RIGHT, fill=BOTH)

    tree = ttk.Treeview(treeFrame, yscrollcommand=treeScroll.set, selectmode="extended", show='headings')
    tree.pack()

    treeScroll.config(command=tree.yview)
    
    tree['column'] = ('OrderDate','StartDate','ReturnDate','TotalDays','VIN','Vehicle','Type','Category','CustomerID','CustomerName','OrderAmount','RentalBalance');
    
    # Configure columns
    tree.column( "OrderDate",    width=150, anchor=W )
    tree.column( "StartDate",  width=150, anchor=W )
    tree.column( "ReturnDate",         width=150, anchor=W )
    tree.column( "TotalDays",         width=100, anchor=W )
    tree.column( "VIN",         width=150, anchor=W )
    tree.column( "Vehicle",         width=150, anchor=W )
    tree.column( "Type",         width=100, anchor=W )
    tree.column( "Category",         width=100, anchor=W )
    tree.column( "CustomerID",         width=100, anchor=W )
    tree.column( "CustomerName",         width=150, anchor=W )
    tree.column( "OrderAmount",         width=100, anchor=W )
    tree.column( "RentalBalance",         width=150, anchor=W )

    # Specify the headings for each column
    tree.heading( 'OrderDate',   text='OrderDate' ) 
    tree.heading( 'StartDate', text='StartDate' )
    tree.heading( 'ReturnDate',        text='ReturnDate' )
    tree.heading( 'TotalDays',        text='TotalDays' )
    tree.heading( 'VIN',        text='VIN' )
    tree.heading( 'Vehicle',        text='Vehicle' )
    tree.heading( 'Type',        text='Type' )
    tree.heading( 'Category',        text='Category' )
    tree.heading( 'CustomerID',        text='CustomerID' )
    tree.heading( 'CustomerName',        text='CustomerName' )
    tree.heading( 'OrderAmount',        text='OrderAmount' )
    tree.heading( 'RentalBalance',        text='RentalBalance' )
    
    # Retrieve a rental by the return date, customer name (the table needs the id), and vehicle info
    retrieveRentalFrame = LabelFrame(handleReturnWindow, text="Enter return date, customer name, and vehicle info")
    retrieveRentalFrame.pack(expand=FALSE, padx=20, fill=BOTH)
    
    typeOption = [ "Compact", "Medium", "Large", "SUV", "Truck", "Van"]
    rentalChoiceLabel = Label( retrieveRentalFrame, text='Type')
    rentalChoiceLabel.grid( row=0, column=0, padx=5, pady=5, sticky=tk.E)

    typeChoice = tk.StringVar()
    rentalType = ttk.Combobox( retrieveRentalFrame, textvariable=typeChoice, values = typeOption, width=13, state="readonly" )
    rentalType.grid( row=0, column=1, padx=5, pady=5, sticky=tk.E)

    categoryOption = [ "Basic", "Luxury"]
    rentalCategoryLabel = Label( retrieveRentalFrame, text='Category')
    rentalCategoryLabel.grid( row=-0, column=2, padx=5, pady=5, sticky=tk.E)

    categoryChoice = tk.StringVar()
    rentalCategory = ttk.Combobox( retrieveRentalFrame, textvariable=categoryChoice, values = categoryOption, width=7, state="readonly" )
    rentalCategory.grid( row=0, column=4, padx=3, pady=5, sticky=tk.E)
    
    returnDateLabel = Label(retrieveRentalFrame, text="Return Date" )
    returnDateLabel.grid( row=0, column=20, padx=5, pady=5, sticky=tk.E)

    returnDateEntry = Entry( retrieveRentalFrame )
    returnDateEntry.grid( row=0, column=25, padx=5, pady=5, sticky=tk.E )

    custNameLabel = Label( retrieveRentalFrame, text='Name')
    custNameLabel.grid(row=0, column=30, padx=5, pady=5, sticky=tk.E)
    
    custNameEntry = Entry( retrieveRentalFrame )
    custNameEntry.grid( row=0, column=35, padx=5, pady=5, sticky=tk.E )

    searchButton = Button( retrieveRentalFrame, text='Search', width=20, command=search)
    searchButton.grid( row=0, column=40, padx=5, pady=5, sticky=tk.E)

    updateRentalFrame = LabelFrame(handleReturnWindow, text="Pay For Vehicle")
    updateRentalFrame.pack(expand=FALSE, padx=20, fill=BOTH)
    
    rentalVehicleIdLabel = Label( updateRentalFrame, text='Vehicle ID')
    rentalVehicleIdLabel.grid( row =1, column=1, padx=5, pady=5, sticky=tk.W)
    filledVehicleId = StringVar()
    rentalVehicleIdEntry = Entry ( updateRentalFrame, state='readonly', textvariable= filledVehicleId )
    rentalVehicleIdEntry.grid( row=1, column=2, padx=5, pady=5, sticky=tk.E )

    rentalCustIdLabel = Label( updateRentalFrame, text='Customer ID')
    rentalCustIdLabel.grid( row =1, column=3, padx=5, pady=5, sticky=tk.W)
    filledCustId = StringVar()
    rentalCustIdEntry = Entry ( updateRentalFrame, state='readonly', textvariable= filledCustId )
    rentalCustIdEntry.grid( row=1, column=4, padx=5, pady=5, sticky=tk.E )

    rentalStartDateLabel = Label( updateRentalFrame, text='Start Date')
    rentalStartDateLabel.grid( row =1, column=5, padx=5, pady=5, sticky=tk.W)
    filledRentalStartDate = StringVar()
    rentalStartDateEntry = Entry ( updateRentalFrame, state='readonly', textvariable= filledRentalStartDate )
    rentalStartDateEntry.grid( row=1, column=6, padx=5, pady=5, sticky=tk.E )

    rentalBalanceLabel = Label( updateRentalFrame, text='Rental Balance Due')
    rentalBalanceLabel.grid( row =1, column=7, padx=5, pady=5, sticky=tk.W)
    filledRentalBalance = StringVar()
    rentalBalanceEntry = Entry ( updateRentalFrame, state='readonly', textvariable= filledRentalBalance )
    rentalBalanceEntry.grid( row=1, column=8, padx=5, pady=5, sticky=tk.E )

    paymentDateLabel = Label( updateRentalFrame, text='Payment Date')
    paymentDateLabel.grid( row =1, column=9, padx=5, pady=5, sticky=tk.W)
    paymentDateEntry = Entry ( updateRentalFrame )
    paymentDateEntry.grid( row=1, column=10, padx=5, pady=5, sticky=tk.E )

    searchButton = Button( updateRentalFrame, text='Make Payment', width=20, command=update)
    searchButton.grid( row=1, column=11, padx=5, pady=5, sticky=tk.E)

    # Get data when double click on item in treeview
    def selectItem(a):
        selected = tree.focus()
        values = tree.item(selected, 'values')
        # print(values)
        try:
            filledVehicleId.set( values[4] )
            filledCustId.set( values[8] )
            filledRentalStartDate.set( values[1] )
            filledRentalBalance.set( values[11] )
        except:
            pass

    tree.bind('<Button-1>', selectItem)
    
    returnFrame = LabelFrame(handleReturnWindow)
    returnFrame.pack(expand=FALSE, padx=20, fill=BOTH)

    returnButton = Button(returnFrame, text="Return to Main Menu", width=20, command=openMainMenu)
    returnButton.grid( row=1, column=1, padx=5, pady=5, sticky=tk.W)

    handleReturnWindow.mainloop()

def mainMenu():
    # Create handle rental window, set its title and size
    
    def openAddNewCust():
        mainMenuWindow.destroy()
        addNewCust()
    
    def openAddNewVehicle():
        mainMenuWindow.destroy()
        addNewVehicle()
    
    def openAddRental():
        mainMenuWindow.destroy()
        addRental()

    def openHandleReturn():
        mainMenuWindow.destroy()
        handleReturn()
    
    def openReturnCustView():
        mainMenuWindow.destroy()
        returnCustView()
    
    def openReturnVehicleView():
        mainMenuWindow.destroy()
        returnVehicleView()

    mainMenuWindow = Tk()
    mainMenuWindow.title( 'Main Menu' )
    mainMenuWindow.geometry( '250x250' ) # width x Height
    mainMenuWindow.iconbitmap('carRental.ico')
    mainMenuWindow.resizable(0, 0)
    mainMenuWindow.eval('tk::PlaceWindow . center')

    mainMenuFrame = tk.Frame(mainMenuWindow)
    mainMenuFrame.pack(anchor="c")

    titleLabel = Label( mainMenuFrame, text='Main Menu', font=("Calibri", 25))
    titleLabel.grid( row =1, column=0, padx=5, pady=5, sticky=tk.W)
    
    addCustomerButton = Button( mainMenuFrame, text='Add Customer', width=25, command=openAddNewCust)
    addCustomerButton.grid( row=2, column=0, padx=5, pady=1, sticky=tk.E)

    addVehicleButton = Button( mainMenuFrame, text='Add Vehicle', width=25, command=openAddNewVehicle)
    addVehicleButton.grid( row=3, column=0, padx=5, pady=1, sticky=tk.E)

    addRentalButton = Button( mainMenuFrame, text='Rent Vehicle', width=25, command=openAddRental)
    addRentalButton.grid( row=4, column=0, padx=5, pady=1, sticky=tk.E)

    handleReturnButton = Button( mainMenuFrame, text='Return Vehicle', width=25, command=openHandleReturn)
    handleReturnButton.grid( row=5, column=0, padx=5, pady=1, sticky=tk.E)

    returnCustViewButton = Button( mainMenuFrame, text='Show Customer Balances', width=25, command=openReturnCustView)
    returnCustViewButton.grid( row=6, column=0, padx=5, pady=1, sticky=tk.E)

    returnCustViewButton = Button( mainMenuFrame, text='Show Vehicle Average Prices', width=25, command=openReturnVehicleView)
    returnCustViewButton.grid( row=7, column=0, padx=5, pady=1, sticky=tk.E)

    mainMenuWindow.mainloop()


# Requirement #5: return the view's result
# def returnView():
#Requirement #5a: return customers
def returnCustView():

    def openMainMenu():
        returnCustViewWindow.destroy()
        mainMenu()

    def clearTreeView():
        for element in tree.get_children():
            tree.delete(element)

    def search():
        clearTreeView()
        query = "SELECT CustID as CustomerID, Name as CustomerName, CONCAT('$', FORMAT(coalesce(SUM(RentalBalance), 0), 2)) as RentalBalance FROM CUSTOMER LEFT JOIN vRentalInfo ON CustomerID = CustID WHERE ( CustID like %s) AND (Name like %s) GROUP BY CustID ORDER BY SUM(RentalBalance);"
        cur.execute( query, ( '%'+custIDEntry.get()+'%', '%'+custNameEntry.get()+'%' ) )
        carsAvailable = cur.fetchall()

        for car in carsAvailable:
            tree.insert( '', tk.END, values=(car[0], car[1], car[2]) )

    # Create add rental window, set its title and size
    returnCustViewWindow = Tk()
    returnCustViewWindow.title( 'Return Customer View' )
    returnCustViewWindow.geometry( '640x580' ) # width x Height
    returnCustViewWindow.iconbitmap('carRental.ico')
    returnCustViewWindow.resizable(0, 0)
    
    treeFrame = tk.Frame(returnCustViewWindow)
    treeFrame.pack(pady=10)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", rowheight= 20, background= "#EDEBDF", 
                                fieldbackground= "#EDEBDF", foreground='black')
    style.configure("Treeview.Heading", font=('Calibri', 13, 'bold')) # Modify font for headings
    style.map("Treeview", background=[('selected', '#347083')])

    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side=RIGHT, fill=BOTH)

    tree = ttk.Treeview(treeFrame, yscrollcommand=treeScroll.set, selectmode="extended", show='headings')
    tree.pack()

    treeScroll.config(command=tree.yview)
    
    tree['column'] = ('CustomerID','CustomerName','RentalBalance')

    # Configure columns
    tree.column( "CustomerID",    width=150, anchor=W )
    tree.column( "CustomerName",  width=150, anchor=W )
    tree.column( "RentalBalance",         width=150, anchor=W )

    # Specify the headings for each column
    tree.heading( 'CustomerID',   text='CustomerID' ) 
    tree.heading( 'CustomerName', text='CustomerName' )
    tree.heading( 'RentalBalance',        text='RentalBalance' )

    # Retrieve a rental by the return date, customer name (the table needs the id), and vehicle info
    retrieveCustFrame = LabelFrame(returnCustViewWindow, text="Enter Customer ID, Customer Name, or part of Customer Name")
    retrieveCustFrame.pack(expand=FALSE, padx=20, fill=BOTH)
    
    custIDLabel = Label(retrieveCustFrame, text="Customer ID" )
    custIDLabel.grid( row=0, column=0, padx=5, pady=5, sticky=tk.E)
    custIDEntry = Entry( retrieveCustFrame )
    custIDEntry.grid( row=0, column=5, padx=5, pady=5, sticky=tk.E )

    custNameLabel = Label(retrieveCustFrame, text="Customer Name" )
    custNameLabel.grid( row=0, column=10, padx=5, pady=5, sticky=tk.E)
    custNameEntry = Entry( retrieveCustFrame )
    custNameEntry.grid( row=0, column=15, padx=5, pady=5, sticky=tk.E )

    searchButton = Button(retrieveCustFrame, text='Search', width=20, command=search)
    searchButton.grid( row=0, column=30, padx=5, pady=5, sticky=tk.E)

    returnFrame = LabelFrame(returnCustViewWindow)
    returnFrame.pack(expand=FALSE, padx=20, fill=BOTH)

    returnButton = Button(returnFrame, text="Return to Main Menu", width=20, command=openMainMenu)
    returnButton.grid( row=1, column=1, padx=5, pady=5, sticky=tk.W)

    returnCustViewWindow.mainloop()
    
#Requirement #5a: return vehicles
def returnVehicleView():
    
    def openMainMenu():
        returnVehicleViewWindow.destroy()
        mainMenu()

    def clearTreeView():
        for element in tree.get_children():
            tree.delete(element)

    def search():
        clearTreeView()
        query = "SELECT VehicleID, Description, CONCAT('$',FORMAT(coalesce(AVG( OrderAmount / TotalDays ), 0), 2)) AvgDailyPrice FROM Vehicle LEFT JOIN vRentalInfo ON VehicleID = VIN WHERE ( VehicleID LIKE %s) AND (Description LIKE %s) GROUP BY VehicleID ORDER BY AVG( OrderAmount / TotalDays );"
        cur.execute( query, ( '%'+VINEntry.get()+'%', '%'+descriptionEntry.get()+'%' ) )
        carsAvailable = cur.fetchall()

        for car in carsAvailable:
            tree.insert( '', tk.END, values=(car[0], car[1], car[2]) )

    # Create add rental window, set its title and size
    returnVehicleViewWindow = Tk()
    returnVehicleViewWindow.title( 'Return Vehicles View' )
    returnVehicleViewWindow.geometry( '640x580' ) # width x Height
    returnVehicleViewWindow.iconbitmap('carRental.ico')
    returnVehicleViewWindow.resizable(0, 0)
    
    treeFrame = tk.Frame(returnVehicleViewWindow)
    treeFrame.pack(pady=10)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", rowheight= 20, background= "#EDEBDF", 
                                fieldbackground= "#EDEBDF", foreground='black')
    style.configure("Treeview.Heading", font=('Calibri', 13, 'bold')) # Modify font for headings
    style.map("Treeview", background=[('selected', '#347083')])

    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side=RIGHT, fill=BOTH)

    tree = ttk.Treeview(treeFrame, yscrollcommand=treeScroll.set, selectmode="extended", show='headings')
    tree.pack()

    treeScroll.config(command=tree.yview)
    
    tree['column'] = ('VIN','Description','Average Daily Price')

    # Configure columns
    tree.column( "VIN",    width=150, anchor=W )
    tree.column( "Description",  width=150, anchor=W )
    tree.column( "Average Daily Price",         width=150, anchor=W )

    # Specify the headings for each column
    tree.heading( 'VIN',   text='VIN' ) 
    tree.heading( 'Description', text='Description' )
    tree.heading( 'Average Daily Price',        text='Average Daily Price' )

    # Retrieve a rental by the return date, customer name (the table needs the id), and vehicle info
    retrieveVehicleFrame = LabelFrame(returnVehicleViewWindow, text="Enter VIN, Vehicle's Description, or part of Vehicle's Description")
    retrieveVehicleFrame.pack(expand=FALSE, padx=20, fill=BOTH)
    
    VINLabel = Label(retrieveVehicleFrame, text="VIN" )
    VINLabel.grid( row=0, column=0, padx=5, pady=5, sticky=tk.E)
    VINEntry = Entry( retrieveVehicleFrame )
    VINEntry.grid( row=0, column=5, padx=5, pady=5, sticky=tk.E )

    descriptionLabel = Label(retrieveVehicleFrame, text="Vehicle's Description" )
    descriptionLabel.grid( row=0, column=10, padx=5, pady=5, sticky=tk.E)
    descriptionEntry = Entry( retrieveVehicleFrame )
    descriptionEntry.grid( row=0, column=15, padx=5, pady=5, sticky=tk.E )

    searchButton = Button(retrieveVehicleFrame, text='Search', width=20, command=search)
    searchButton.grid( row=0, column=30, padx=5, pady=5, sticky=tk.E)

    returnFrame = LabelFrame(returnVehicleViewWindow)
    returnFrame.pack(expand=FALSE, padx=20, fill=BOTH)

    returnButton = Button(returnFrame, text="Return to Main Menu", width=20, command=openMainMenu)
    returnButton.grid( row=1, column=1, padx=5, pady=5, sticky=tk.W)

    returnVehicleViewWindow.mainloop()
    

loginW()

cur.close()
conn.close()