# Program For Sleep Tite Motel
# Author Logan Oram
# Date March 22nd 2024

import datetime
import formatValues as FV

# Default values

NEXT_POLICY_NUM = 1944
BASIC_PREM = 869.00
ADDIT_CAR_DIS = .25
LIABILITY_COST = 130.00
GLASS_COST = 86.00
LOANER_COST = 58.00
HST = .15
PROCESS_FEE = 39.99

# Function to calculate monthly payment and total cost

def CalHST(Tot_Insur_Prem):
    Hst = Tot_Insur_Prem + HST
    return Hst

def CalTotCost(Tot_Insur_Prem, Hst):
    Tot_Cost = Tot_Insur_Prem + Hst
    return Tot_Cost


    

# User Inputs

while True:
    
    
    while True:
        Cust_Fname = input("Enter first name: ")
        if Cust_Fname =="":
            print("Error - Name Cannot Be Invaild:")
        else:
            break
    
    while True:
        CustLname  = input("Enter last name: ")
        if CustLname == "":
            print("Error - Name Cannot Be Blank:")
        else:
            break
    
    
    while True:
        address = input("Enter address: ")
        if address == "":
            print("Error - Address Cannot Be Invaild:")
        else:
            break
    
    while True:
        city = input("Enter city: ").title()
        if city == "":
            print("Error - City Cannot Be Invaild:")
        else:
            break

    ProvList = ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"]
    while True:
        province = input("Enter Current Province (XX): ").upper()
        if province == "":
            print("Error - Province Must Not Be invaild: ")
        elif province not in ProvList:
            print("Error - Province Must Be From List: ")
        else:
            break
    
    while True:
        postal_code = input("Enter postal code: ")
        if postal_code == "":
            print("Error - Postal Code Cannot Be Invaild:")
        else:
            break
    
    while True:
        phone_number = input("Enter phone number: ")
        if phone_number == "":
            print("Error - Phone Number Cannot Be Invaild:")
        else:
            break
    
    while True:
        num_cars = int(input("Enter number of cars being insured: "))
        if num_cars == "":
            print("Error - The Number Of Cars Cannot Be Invaild:")
        else:
            break
    
    while True:
        extra_liability = input("Extra liability coverage? (Y/N): ").upper()
        if extra_liability == "":
            print("Error - Cannot Be Invaild: ")
        else:
            break
    
    while True:
        glass_coverage = input("Glass coverage? (Y/N): ").upper()
        if glass_coverage == "":
            print("Error - Glass Coverage Cannot Be Invaild:")
        else:
            break
    
    while True:
        loaner_car = input("Loaner car coverage? (Y/N): ").upper()
        if loaner_car == "":
            print("Error - Loaner Car Cannot Be Invaild:")
        else:
            break
    
    while True:
        payment_method = input("Is The Customer Paying In Full, Monthly or Down Payment (F/M/D): ").title()
        if payment_method == "":
            print("Error - Payment Method Cannot Be Invaild:")
        elif payment_method == "D":
            down_payment = float(input("Enter down payment amount: "))
        else:
            down_payment = 0
            break

        # List for dates and costs
        Datelist = []
        Costlist = []

        while True:
            while True:
                date = input("Enter the date of the claim 'MM-DD-YYYY:" )
                if not date:
                    break

                if date == "":
                    print("Error - The date cannot be blank:")
                else:
                    break

                if date == "":
                    break
            
            while True:
                cost = float(input("Enter the cost of the claim:" ))
                if cost == "":
                    print("Error - cost cannot be blank: ")
                else:
                    break

            Datelist.append(date)
            Costlist.append(cost)


            # Calculations For The Program

            Insur_Prem = BASIC_PREM * num_cars
            if num_cars >1:
                Insur_Prem = (BASIC_PREM * num_cars) * ADDIT_CAR_DIS

            Ext_Liab = 0
            if extra_liability == "Y":
                Ext_Liab = LIABILITY_COST * num_cars

            Glass_Cover = 0
            if glass_coverage == "Y":
                Glass_Cover = GLASS_COST * num_cars

            Car_Loan = 0
            if loaner_car == "Y":
                Car_Loan = LOANER_COST * num_cars

            Tot_Extra_Cost = Ext_Liab + Glass_Cover + Car_Loan

            Tot_Insur_Prem = Insur_Prem + Tot_Extra_Cost

            Hst = CalHST(Tot_Insur_Prem)

            Tot_cost = CalTotCost(Tot_Insur_Prem, Hst)
            
            MonthlyPay = PROCESS_FEE + Tot_cost / 8

            FtotCost = (Tot_cost - down_payment) + PROCESS_FEE
            MonthlyPay = FtotCost / 8

            InvoiceDate = datetime.datetime.now().strftime("%m-%d-%Y")
            
            FirstPayDay = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%m-%d-%Y")

            
            # Display Results
            
            print()
            print("-----------------------------------------------")
            print("One Stop Insurance Company: ")
            print("-----------------------------------------------")
            print(f"Customer:")
            print(f"{Cust_Fname:<15}{CustLname:<10}")
            print(f"Address:")
            print(f"    {address:<14} ")
            print(f"{city:<15},{province:<2}{postal_code:<6}")
            print(f"{phone_number:<10}")
            print("-----------------------------------------------")
            print(f"Cars Insured:                       {num_cars:<2}")
            print(f"Extra Liability:                    {extra_liability:<3s}")
            print(f"Glass Coverage:                     {glass_coverage:<3s}")
            print(f"Loaner Car:                         {loaner_car:<3}")
            print(f"Payment Type:                       {payment_method:<7s}")
            print(f"Down Payment:                       {FV.FDollar2(down_payment):<6}")
            print(f"----------------------------------------------")
            print(f"Insurance Premiums:                 {FV.FDollar2(Insur_Prem):<6}")
            print(f"Extra Liability:                    {FV.FDollar2(Ext_Liab):<6}")
            print(f"Glass Coverage:                     {FV.FDollar2(Glass_Cover):<6}")
            print(f"Loaner Car:                         {FV.FDollar2(Car_Loan):<6s}")
            print(f"----------------------------------------------")
            print(f"Total Extra Costs:                  {FV.FDollar2(Tot_Extra_Cost):<6s}")
            print(f"Total Insurance Premium:            {FV.FDollar2(Tot_Insur_Prem):<6s}")
            print(f"HST:                                {FV.FDollar2(Hst):<6s}")
            print(f"Total Cost:                         {FV.FDollar2(Tot_cost):<6s}")
            print(f"Final Total Cost:                   {FV.FDollar2(FtotCost):<6s}")
            print(f"Monthly Payments:                   {FV.FDollar2(MonthlyPay):<6s}")
            print(f"Invoice Date:                       {InvoiceDate:<7s}")
            print(f"First Payment Date:                 {FirstPayDay:<7s}")
            print(f"----------------------------------------------")
            print(f"Customers Claims:")
            print()
            print(f"    Claim #        Claim Date        Amount     ")
            print(f"----------------------------------------------")
            ClaimNum = 1
            for i in range(0, len(Datelist)):
                print(f"     {ClaimNum:2d}             {Datelist[i]:>10s}        {FV.FDollar2(Costlist[i]):>7}")
            
            Next_Cust = input("Do you want to enter another customer? (Y/N): ").upper()
            if Next_Cust != "Y":
                break
