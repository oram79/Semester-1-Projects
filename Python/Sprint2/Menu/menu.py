import datetime
import time
import sys
import re
selection = []
 
 
def OptionOne():
# Description: 
# Author: Nicholas 
# Date(s): 


# Define program constants.
# Open the defaults file and read the values into variables
    f = open('Defaults.dat', 'r')
    NEXT_TRANSACTION_DATE = float(f.readline())
    NEXT_DRVIER_NUMBER = float(f.readline())
    MONTHLY_STAND_FEE = float(f.readline())
    DAILY_RENTAL_FEE = float(f.readline())
    WEEKLY_RENTAL_FEE = float(f.readline())
    HST_RATE = float(f.readline())
    f.close()




    # Define program functions.



    # Main program starts here.
    while True:
        
        # Gather user inputs.
        while True:
            DriveNum =                  input("Enter the employee's driver number (9999):                         ")
            if DriveNum == "":
                print("Data Entry Error - Employee's driver number cannot be blank.")
            elif len(DriveNum) != 4:
                print("Data Entry Error - Employee's driver number must be 4 digits only.")
            else:
                break
        
        while True:
            Name =                      input("Enter the employee's name:                                         ")
            if Name == "":
                print("Data Entry Error - Employee's name cannot be blank.")
            else:
                break

        while True:
            Address =                   input("Enter the employee's address:                                      ")
            if Address == "":
                print("Data Entry Error - Employee's address cannot be blank.")
            else:
                break
        
        while True:
            PhoneNum =                  input("Enter the employee's phone number ((999) 999-9999):                ")
            if PhoneNum == "":
                print("Data Entry Error - Employee's phone number cannot be blank.")
            elif len(PhoneNum) != 14:
                print("Data Entry Error - Employee's phone number must be 14 digits only.    ")
            else:
                break
        
        while True:
            DriveLicenseNum =           input("Enter the employee's drivers license number (99999999):            ")
            if DriveLicenseNum == "":
                print("Data Entry Error - Employee's drivers license number cannot be blank.")
            elif len(DriveLicenseNum) != 8:
                print("Data Entry Error - Employee's drivers license number must be 8 digits only.")
            else:
                break
        
        while True:
            try:
                DriveLicenseExpiryDate = input("Enter the employee's drivers license expiry date (YYYY-MM-DD):     ")
                DriveLicenseExpiryDate = datetime.datetime.strptime(DriveLicenseExpiryDate, "%Y-%m-%d")
            except:
                print("Data Entry Error - Employee's drivers license expiry date is not in a valid format.")
            else:
                break
        
        while True:
            InsurPolicyComp =            input("Enter the employee's insurance policy company:                     ")
            if InsurPolicyComp == "":
                print("Data Entry Error - Employee's insurance policy company cannot be blank.")
            else:
                break
        
        while True:
            PolicyNum =                  input("Enter the employee's policy number (999-9999-9999):                ")
            if PolicyNum == "":
                print("Data Entry Error - Employee's policy number cannot be blank.")
            elif len(PolicyNum) != 13:
                print("Data Entry Error - Employee's policy number must be 13 digits only.")
            else:
                break
        
        while True:
            EmpCarOption =               input("Enter if one of the company's cars (O(Own Car) or R(Rented Car)):  ").upper() 
            if EmpCarOption == "":
                print("Data Entry Error - Employee's car option cannot be blank.")
            elif EmpCarOption != "O" and EmpCarOption != "R":
                print("Data Entry Error - The employee's car option can only be entered as O or R only.")
            else:
                break

        # Perform required calculations.
        if EmpCarOption == "O":
            StandFee = MONTHLY_STAND_FEE
            Rentals = 0
        elif EmpCarOption == "R":
            StandFee = 0
            Rentals = DAILY_RENTAL_FEE + WEEKLY_RENTAL_FEE 
        
        BalDue = StandFee + Rentals
        
        # Display results
        print()
        print("Information for a New Employee at HAB Taxi Services")
        print("--------------------------------------------------------------------------------")
        print(f"Driver number:                       {DriveNum:>4s}")
        print(f"Name:                                {Name}")
        print(f"Address:                             {Address}")
        print(f"Phone number:                        {PhoneNum:>14s}")
        print(f"Drivers lincense number:             {DriveLicenseNum:>8s}")
        DriveLicenseExpiryDateDsp = datetime.datetime.strftime(DriveLicenseExpiryDate, "%Y-%m-%d")
        print(f"Drivers lincense expiry date:        {DriveLicenseExpiryDateDsp:>10s}")
        print(f"Employee's insurance policy company: {InsurPolicyComp}")
        print(f"Policy number:                       {PolicyNum:>13s}")
        if EmpCarOption == "O":
            print(f"Car option:                           {EmpCarOption:>1s}(Own Car)")
        elif EmpCarOption == "R":
            print(f"Car option:                           {EmpCarOption:>1s}(Rented Car)")
        StandFeeDsp = "${:.2f}".format(StandFee)
        print(f"Stand fee amount:                    {StandFeeDsp:>7s}")
        RentalsDsp = "${:.2f}".format(Rentals)
        print(f"Rentals amount:                    {RentalsDsp:>7s}")
        BalDueDsp = "${:.2f}".format(BalDue)
        print(f"Balance due amount:                  {BalDueDsp:>7s}")

        # Write the values to a data file called NewEmployee.dat.
        for _ in range(5):  # Change to control no. of 'blinks'
            print('Saving new employee information ...', end='\r')
            time.sleep(.3)  # To create the blinking effect
            sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
            time.sleep(.3)

        
        f = open("NewEmployee.dat", "a")
    
        # All values written to file must be a string.  If you have a numeric
        # value, use the str() function to convert.
        f.write("{}, ".format(DriveNum)) 
        f.write("{}, ".format(Name))
        f.write("{}, ".format(Address))
        f.write("{}, ".format(PhoneNum))
        f.write("{}, ".format(DriveLicenseNum))
        f.write("{}, ".format(DriveLicenseExpiryDateDsp))
        f.write("{}, ".format(InsurPolicyComp))
        f.write("{}, ".format(PolicyNum))
        f.write("{}, ".format(EmpCarOption))
        f.write("{}, ".format(StandFee))
        f.write("{}, ".format(Rentals))
        f.write("{}\n".format(BalDue))
        
        
        
        f.close()

        print()
        print("New employee's information successfully saved ...", end='\r')
        time.sleep(1)  # To create the blinking effect
        sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns

        print()
        Cont = input("Do you want to process another new employee's information?(Y/N): ").upper()
        print()
        if Cont == "N":
            break


 
 
selection.append(OptionOne)
 
def OptionTwo():
 
   print("Under Construction")
 
selection.append(OptionTwo)
 
def OptionThree():
 
    print("Under Construction")
 
selection.append(OptionThree)
 
def OptionFour():
 
    print("Under Construction")
 
selection.append(OptionFour)
 
def OptionFive():
 
    print("Under Construction")
 
selection.append(OptionFive)
 
def OptionSix():
 
    print("Under Construction")
 
selection.append(OptionSix)
 
def OptionSeven():
 #description:
#author: Zac D
#date: 4/12/2024




    def read_drivers(NewEmployee):
        drivers = []
        with open(NewEmployee, 'r') as file:
            next(file)  #skip header line
            for line in file:
                parts = line.strip().split(',')
                driver_id = int(parts[0])
                drivers[driver_id] = {
                    "name": parts[1],
                    "balance_due": float(parts[10])
                }
        return drivers

    def read_financials(CompanyRevenues):
        financials = []
        with open(CompanyRevenues, 'r') as file:
            next(file)  #skip header line
            for line in file:
                parts = line.strip().split(',')
                financials.append((int(parts[0]), parts[1], parts[2], float(parts[3])))
        return financials

    #read from dat files
    drivers = read_drivers("NewEmployee.dat")
    financials = read_financials("CompanyRevenues.dat")


    def print_driver_financial_listing(drivers, financials):
        print("Driver Financial Listing")
        print("-" * 30)
        for driver_id, driver_info in drivers.items():
            total_earnings = 0
            total_deductions = 0
            for record in financials:
                if record[0] == driver_id:
                    if record[3] < 0:
                        total_deductions += abs(record[3])
                    else:
                        total_earnings += record[3]
            
            net_pay = total_earnings - total_deductions
            driver_info["balance_due"] += net_pay  #update the balance due
            print(f"Driver: {driver_info['name']}")
            print(f"Total Earnings: ${total_earnings:.2f}")
            print(f"Total Deductions: ${total_deductions:.2f}")
            print(f"Net Pay: ${net_pay:.2f}")
            print("-" * 30)

    #execute
    print_driver_financial_listing(drivers, financials)
    
 
selection.append(OptionSeven)
 
def OptionEight():
#   Purpose     -   Project 2 Option 8 for the SD11 WInter Semester Final Sprint            
#   Author(s)   -   Zac Davidge, Ardent Pardy  
#   Date(s)     -   04/11/2024





    current_datetime = datetime.datetime.now()
    DateToday = current_datetime.strftime("%Y-%m-%d")

    while True:
        DriveNum = input("Enter Driver Number: ")
        if not DriveNum.isdigit():
            print("Invalid Characters. Numbers ONLY, please.")
        else:
            break

    while True:
        StartDate = input("Enter Start Date (YYYY-MM-DD): ")
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', StartDate):
            print("Invalid format. Enter date in YYYY-MM-DD format, please.")
        else:
            break

    while True:
        EndDate = input("Enter End Date (YYYY-MM-DD): ")
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', EndDate):
            print("Invalid format. Enter date in YYYY-MM-DD format, please.")
        else:
            break

    Desc= input("Enter a _Brief_ Description:  ")

    def driver_listing():
        print("\nHAB Taxi Services")
        print("Driver Financial Listing for HAB Taxi Services From {StartDate} to")
        print(EndDate)
        print()
        print()
        print(" Trans      Trans        Trans          Trans")
        print(" ID         Start Date   End Date       Brief Desc")
        print("===================================================================")
        print("\n",DriveNum,"      ", StartDate,"-", EndDate,"   ",Desc)
    driver_listing()


 
selection.append(OptionEight)
 
def OptionNine():
    print("Goodbye!")
    exit()   
# Option 9
# Author: Daniel Bowers
 
 

selection.append(OptionNine)
# Main menu
# Author: Daniel Bowers
while True:
    print("HAB Taxi Services")
    print("Company Services System")
    print()
    print("1. Enter a New Employee (driver).")
    print("2. Enter Company Revenues.")
    print("3. Enter Company Expenses.")
    print("4. Track Car Rentals.")
    print("5. Record Employee Payment.")
    print("6. Print Company Profit Listing.")
    print("7. Print Driver Financial Listing.")
    print("8. Print Driver Financial Listing for a specific period.")
    print("9. Quit Program.")
    print()
 
    while True:
        choice = input("Enter choice (1-9): ")
        if choice.isdigit() == False:
            print("Not a valid response, please re-enter.")
        else:
            choice = int(choice)
            if choice > 9 or choice < 1:
                print("Not a valid response, please re-enter.")
            else:
                break
 
    print()
    choice = selection[choice-1]
    choice()

    # Comments - Unable to debug Script 7 - Very sorry.