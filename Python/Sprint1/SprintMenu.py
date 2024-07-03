def NLchocoCom():
    
    # Program for NL Chocolate Company
    # Author Logan Oram
    # Date Feb 19th, 2024

    # Imports

    import datetime

    DAILY_RATE = 85.00
    PER_KILOMETER = .17
    RENTAL_CAR = 65.00
    HST = .15
    
    # gather user information

    while True:

        while True:
            EmployeeNum = input("Enter The Employee Number: ")
            if EmployeeNum == "":
                print("Error - Employee Number Cannot Be Invaild: ")
            elif len(EmployeeNum) != 5:
                print("Error - Employee Number Must Be 5 Characters Only: ")
            else:
                break
            
        
        while True:
            EmpFName = input("Enter The Employee First Name: ").title()
            if EmpFName == "":
                print("Error - Employee First Name Cannot Be Invaild: ")
            else:
                break

        while True:
            EmpLName = input("Enter The Emploee Last Name: ").title()
            if EmpLName == "":
                print("Error - Employee Last Name Cannot Be Invaild: ")
            else:
                break
        
        while True:
            TripLocation = input("Enter The Location Employee Visted: ").title()
            if TripLocation == "":
                print("Error - Trip Location Cannot Be Invaild: ")
            else: 
                break

        while True:
            try:
                TripStart = input("Enter The Employee Trip Start Date: (MM-DD-YYYY) ")
                TripStart = datetime.datetime.strptime(TripStart,"%m-%d-%Y")
            except:
                print("Error - Start Date Is Invaild")
            else:
                if TripStart == "":
                    print("Error - Trip Start Date Cannot Be Invaild: ")
                else:
                    break

        while True:
            try:
                TripEnd = input("Enter The Employee Trip End Date: (MM-DD-YYYY) ")
                TripEnd = datetime.datetime.strptime(TripEnd,"%m-%d-%Y")
            except:
                print("Error - End Date Is Invaild")
            else:
                if TripEnd == "":
                    print("Error - Trip End Date Cannot Be Invaild: ")
                else:
                    break

        while True:
            TransportType = input("Enter The Transportation Type (O or R) : ").upper()
            if TransportType == "":
                print("Error - Transportation Type Cannot Be Invaild: ")
            elif TransportType == "O" or TransportType == "R":
                break
            else:
                print("Error - Transport Type Must Be O or R ")
                

        while True:
            ClaimType = input("Enter The Claim Amount (S or E) : ").upper()
            if ClaimType == "":
                print("Error - Claim Type Cannot Be Invaild: ")
            elif ClaimType == "S" or ClaimType == "E":
                break
            else:
                print("Error - Transport Type Must Be S or E ")
                

        while True:
            TotKilometers = int(input("Enter The Total Kilometers Traveled: "))
            if TotKilometers == "":
                print("Error - Kilometers Travled Cannot Be Invaild: ")
            elif int(TotKilometers) > 2000:
                print("Error - Total Kilometers Cannot Exceed 2000km: ")
            else:
                break

   # Generate program results through calculations.
            
        NumDays = (TripEnd - TripStart).days
            
        PerDiem = NumDays * DAILY_RATE

        MilageAmount = TotKilometers * PER_KILOMETER
        if TransportType == "O":
            MilageAmount = RENTAL_CAR * NumDays


        Amtbonus = 0 
        if NumDays > 3:
            Amtbonus += 100.00

        if TotKilometers > 1000 and TransportType == 'O':
            Amtbonus += 0.04 * TotKilometers

        if ClaimType == "E": 
            Amtbonus += 45.00 * NumDays

        ClaimAmount = PerDiem + MilageAmount + Amtbonus

        SalesTax = ClaimAmount * HST

        ClaimTotal = ClaimAmount + SalesTax

        TripStart1 = TripStart = datetime.datetime.strftime(TripStart,"%m-%d-%Y")
        TripEnd1 = TripEnd = datetime.datetime.strftime(TripEnd,"%m-%d-%Y")

   # Display User Results
        
        print()
        print(f"          NL Chocolate Company")
        print(f"------------------------------------------")
        print(f"Employee #:           {EmployeeNum:<5s}")
        print(f"First Name:           {EmpFName:<10s}")
        print(f"Last Name:            {EmpLName:<10s}")
        print(f"------------------------------------------")
        print(f"Trip Details")
        print(f"------------------------------------------")
        print(f"Trip Location:        {TripLocation:<8s}")
        print(f"Trip Start-Date:      {TripStart:<10s}")
        print(f"Trip End-Date:        {TripEnd:<10s}")
        print(f"Number Of Days:       {NumDays:<2}")
        print(f"Transportation Type:  {TransportType:<6s}")
        print(f"Claim Type:           {ClaimType:<10s}")
        print(f"Total Kilometers:     {TotKilometers:<4}")
        print(f"------------------------------------------")
        print(f"Invoice Summary")
        print(f"------------------------------------------")
        MilageAmountDsp = "${:,.2f}".format(MilageAmount)
        print(f"Mile Amount:          {MilageAmountDsp:<10}")
        AmtbonusDsp = "${:,.2f}".format(Amtbonus)
        print(f"Bonus:                {AmtbonusDsp:<4}")
        ClaimAmountDsp = "${:,.2f}".format(ClaimAmount)
        print(f"Claim Amount:         {ClaimAmountDsp:<8}")
        SalesTaxDsp = "${:,.2f}".format(SalesTax)
        print(f"HST Amount:           {SalesTaxDsp:<8}")
        ClaimTotalDsp = "${:,.2f}".format(ClaimTotal)
        print(f"Total Claim Amount:   {ClaimTotalDsp:<8}")

        Continue = input(" Any Further Data Entry's ?? (END to quit): ").upper()         
        if Continue == "END":
            break
    pass





# Program For Fun Interview Questions
# Author Zac Davidge
# Date Feb 25th, 2024

def InterQue():
    def fizz_buzz(n):
        result = []

        for i in range(1, n + 1):

            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")

            elif i % 3 == 0:
                result.append("Fizz")

            elif i % 5 == 0:
                result.append("Buzz")
            else: 
                result.append(str(i))
        
        return result

    n = 100

    result = fizz_buzz(n)

    print(''.join(result))
    pass





def StringAndDates():
    # cool Stuff With Strings and Dates
    # Author Logan Oram
    # Date Feb 24th, 2024

    #imports

    import datetime 
    import random
    CurDate = datetime.datetime.now()

    # User Inputs

    print()
    EmployFName = input(f"Enter Your First Name: ").title()
    EmployLName = input(f"Enter Your Last Name: ").title()
    PhonNum = input(f"Enter Your Phone Number: (999)999-9999 ")
    StartWork = input(f"When Did You Start Working With Us?: (MM-DD-YYYY) ")
    Bday = input(f"Enter Your Birthday: (MM-DD-YYYY) ")

    # Username And Password Generator

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()."

    string = lower + upper + numbers + symbols
    length = 16
    password = "".join(random.sample(string,length))

    # Employee ID

    reciptID = EmployFName[0] + EmployLName[0] + "-" + PhonNum[8:12] + "-" + StartWork[6:10] + "-" + Bday[0:2]

    # Length Of Employement

    StartWork = datetime.datetime.now().strptime(StartWork, "%m-%d-%Y")
    Bday = datetime.datetime.now().strptime(Bday, "%m-%d-%Y")

    CurYear = CurDate.year
    CurMonth = CurDate.month
    CurDay = CurDate.day

    BirthYear = Bday.year
    BirthMonth = Bday.month
    Birthday = Bday.day

    RetireDay = datetime.datetime(BirthYear +65, BirthMonth, Birthday)

    EmpDuration = (CurDate - StartWork).days

    # Time Untill Retirement

    DaysTillRetire = (RetireDay - CurDate).days
    YearsTillRetire = DaysTillRetire / 365

    # Time Until Birthday

    TillBday = (CurDate - Bday).days / 12

    # Display Results

    print()
    print(f"First Name: {EmployFName:<10s}")
    print(f"Last Name: {EmployLName:<10s} ")
    print(f"Phone Number: {PhonNum:<10} ")
    print(f"Started Working: {StartWork} ")
    print(f"Birthday: {Bday} ")
    print("Password:")
    print(password)
    print("CHANGE AFTER FIRST LOGIN!")
    print(f"Employee ID: {reciptID}")
    print(f"Length Of Employment: {EmpDuration}")
    print(f"Time Till Retirement: {RetireDay}")
    print(F"Time Till Birthday: {TillBday}")

    pass





# Program For Fun Interview Questions
# Author Zac Davidge
# Date Feb 25th, 2024

# Program For Little Buit of Everything

def BitEvery():
    from datetime import datetime, timedelta

    # Function to calculate maintenance dates
    def calculate_maintenance_dates(purchase_date):
        basic_cleaning_date = purchase_date + timedelta(days=10)
        tube_fluid_check_date = purchase_date + timedelta(weeks=3)
        major_inspection_date = purchase_date + timedelta(weeks=26)
        
        return basic_cleaning_date, tube_fluid_check_date, major_inspection_date

    # Function to calculate monthly amortization
    def calculate_monthly_amortization(cost):
        useful_life_months = 180
        salvage_value = 0.1 * cost
        monthly_amortization = (cost - salvage_value) / useful_life_months
        return monthly_amortization

    # Main function
    def main():
        # User input
        cost = float(input("Enter the cost of the equipment: "))
        purchase_date_str = input("Enter the purchase date (YYYY-MM-DD): ")
        purchase_date = datetime.strptime(purchase_date_str, "%Y-%m-%d")

        # Calculate maintenance dates
        basic_cleaning_date, tube_fluid_check_date, major_inspection_date = calculate_maintenance_dates(purchase_date)

        # Calculate monthly amortization
        monthly_amortization = calculate_monthly_amortization(cost)

        # Output maintenance schedule
        print("\nMaintenance Schedule:")
        print(f"Basic Cleaning: {basic_cleaning_date.strftime('%Y-%m-%d')}")
        print(f"Tube and Fluid Checks: {tube_fluid_check_date.strftime('%Y-%m-%d')}")
        print(f"Major Inspection: {major_inspection_date.strftime('%Y-%m-%d')}")

        # Output monthly amortization
        print("\nMonthly Amortization:")
        print(f"${monthly_amortization:.2f}")

    if __name__ == "__main__":
        main()
    pass





def oldnew():
    
    # Program For a Game of Rock, Paper, Scissors
    
    import random

    options = ("Rock", "Paper", "Scissors")
    running = True

    while running:

        player = None
        computer = random.choice(options)
        print()
        while player not in options:   
            player = input("Enter A Choice (Rock, Paper or Scissors): ").title()

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It's A Tie!")
        elif player == "Rock" and computer == "Scissors":
            print("You Win! ")
        elif player == "Paper" and computer == "Rock":
            print("You Win")
        elif player == "Scissors" and computer == "Paper":
            print("You Win! ")
        else:
            print("You Lose!")

        if not input("Play Again? (y/n): ").lower() == "y":
            running = False

    print("Thanks For Playing!")





while True:
    print()
    print("Logan And Zac's Python Programs - Main Menu")
    print()
    print("1. NL Chocolate Company: ")
    print("2. Fun Interview Questions: ")
    print("3. Cool Stuff With Strings And Dates: ")
    print("4. A Little Bit Of Everything: ")
    print("5. Something old, Something New: ")
    print("6. Quit: ")
    print()
   
    while True:
        try:
            Choice = input("Enter choice (1 - 6): ")
            Choice = int(Choice)
        except:
            print("Data Entry Error - must be a valid number between 1 and 6.")
        else:
            if Choice < 1 or Choice > 6:
                print("Data Entry Error - must be a valid number between 1 and 6.")
            else:
                break
       
    if Choice == 1:
        NLchocoCom()
    elif Choice == 2:
        InterQue()
    elif Choice == 3:
        StringAndDates()
    elif Choice == 4:
        BitEvery()
    elif Choice == 5:
        oldnew()
    else:
        break
print()
print("Thank You For Reviewing Our Python Programs!")