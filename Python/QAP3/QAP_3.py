# Program for the Honest Harry Car Sales
# Author Logan Oram
# Date Feb 7th, 2024

# Imports

import datetime 

# Define Program Constants

LICENSE_FEE1_RATE = 75.00
LICENSE_FEE2_RATE = 165.00
TRANSFER_FEE1_ESP = 0.01
TRANSFER_FEE2_ESP = 0.016
FINANCE_FEE_RATE = 39.99
HST_ESP = 0.15

# Gather User Information

InvDate1 = datetime.datetime.now().strftime("%B %d, %Y")
InvDate2 = datetime.datetime.now().strftime("%d %b, %y")
FtimePay = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%d %b, %y")

while True:
    
    while True: 
        CustFName = input("Enter The Customer's First Name: ").title()
        if CustFName == "":
            print("Error - Customer Name Cannot Be Invaild: ")
        else:
            break

    while True:
        Cus_Last_Name = input("Enter The Customers Last Name: ").title()
        if Cus_Last_Name == "":
            print("Error - Customer Name Cannot Be Invaild: ")
        else:
            break
    while True:
        Cust_Phone_Num = input("Enter the phone number (9999999999): ")
        if Cust_Phone_Num == "":
            print("Error - Phone number cannot be blank.")
        elif len(Cust_Phone_Num) != 10:
            print("Error - Phone number must be 10 digits only.")
        else:
            break

    while True:
        CustAdd = input("Enter The Customers Address: ")
        if CustAdd == "":
            print("Error - Customer Address Must Be Entered: ")
        else:
            break

    while True:
        CustCity = input("Enter The Customers City: ")
        if CustCity == "":
            print("Error - Customer City Must Be Entered: ")
        else:
            break

    while True:
        CustProv = input("Enter The Customers Province: ").upper()
        if CustProv == "":
            print("Error - Customer Province Must Be Entered")
        else:
            break

    while True:
        CustPostal = input("Enter The Customers Postal Code: (A1A1A1) ").upper()
        if CustPostal == "":
            print("Error - Customer Postal Code Must Be Entered: ")
        elif len(CustPostal) != 6:
            print("Error - Customer Postal Code Must Be 6 Characters Long")
        else:
            break
        
    
    while True:
        Plate_Num = input("Enter The Vehicle's License Plate Number (XXX999): ").upper()
        if Plate_Num == "":
            print("Error - Plate Number Cannot Be Invaild:")
        elif len(Plate_Num) != 6:
            print("Error - License Plate Must Be 6 Characters Long")
        else:
            break
        
    while True:
        Car_Sale_Price = float(input("Enter The Vehicle's Sale Price: "))
        if Car_Sale_Price >= 50000.00:
            print("Error - Vehicle Sale Price Cannot Exceed $50,000")
        else:
            break
        
    while True:
        Car_Trade_In = float(input("Enter The Vehicle Trade In Price: "))
        if Car_Trade_In >= Car_Sale_Price:
            print(" Error - Vehicle Trade In Cannot Exceed Vehicle Sale Price")
        else:
            break

    while True:
        Car_Make = input("Enter The Car's Make: ")
        if Car_Make == "":
            print("Error - Car Make Must Be Entered")
        else:
            break

    while True:
        Car_Model = input("Enter The Car's Model: ")
        if Car_Model == "":
            print("Error - Vehicle's Model Must Be Entered: ")
        else:
            break

    while True:
        Car_Year = input("Enter The Vehicle's Year: ")
        if Car_Year == "":
            print("Error - Vehicle's Year Must Be Entered: ")
        else:
            break

    while True:
        Sale_Person = input("Enter The Sales Person Name: ")
        if Sale_Person == "":
            print("Error - Sale Person Name Must Be Entered: ")
        else:
            break
    
    # Gen

    ReceiptNum = CustFName[0] + Cus_Last_Name[0] + "-" + Plate_Num[3:7] + "-" + Cust_Phone_Num[6:10]

    # Generate program results through calculations.

    PriceAfterTrade = Car_Sale_Price - Car_Trade_In 

    license_fee = LICENSE_FEE1_RATE
    if Car_Sale_Price >= 5000:
        license_fee = LICENSE_FEE2_RATE

    Transfer_fee = TRANSFER_FEE1_ESP * Car_Sale_Price
    if Car_Sale_Price > 20000:
        Transfer_fee = (Car_Sale_Price * TRANSFER_FEE2_ESP) + Transfer_fee

    Sub_Total = PriceAfterTrade + license_fee + Transfer_fee

    Sales_tax = Sub_Total * HST_ESP

    Tot_Sales_price = Sub_Total + Sales_tax

    # display Results
    
    print(f"         1         2         3         4         5         6         7")
    print(f"123456789012345678901234567890123456789012345678901234567890123456789012345678")
    print()
    print(f"Honest Harry Car Sales:                          Invoice Date: {InvDate1:<14s}")                           
    print(f"Used Car Sale And Receipt:                       Receipt No: {ReceiptNum:<11s}")
    print()  
    Car_Sale_PriceDsp = "${:,.2f}".format(Car_Sale_Price)
    Car_Trade_InDsp = "${:,.2f}".format(Car_Trade_In)
    print(f"                                         Sale Price:               {Car_Sale_PriceDsp:<10}")
    print(f"Sold To:                                 Trade Alowance:           {Car_Trade_InDsp:<10}")
    print(f"                                         ------------------------------------")
    PriceAfterTradeDsp = "${:,.2f}".format(PriceAfterTrade)
    license_feeDsp = "${:,.2f}".format(license_fee)
    Transfer_feeDsp = "${:,.2f}".format(Transfer_fee)
    print(f"     {CustFName[0]}. {Cus_Last_Name:<15s}                  Price After Trade:         {PriceAfterTradeDsp:<10}")
    print(f"     {CustAdd:<15s}                    License Fee:                 {license_feeDsp:<10}")
    print(f"     {CustCity:<10s} {CustProv:<2s} {CustPostal:<6s}               Transfer Fee:                {Transfer_feeDsp:<10}")
    print(f"                                         ------------------------------------  ")
    Sub_TotalDsp = "${:,.2f}".format(Sub_Total)
    Sales_taxDsp = "${:,.2f}".format(Sales_tax)
    print(f"Car Details:                             Subtotal:                  {Sub_TotalDsp:<10}")
    print(f"                                         HST:                        {Sales_taxDsp:<10}")
    print(f"     {Car_Year:<4s} {Car_Make:<8s}{Car_Model:<8s}               ------------------------------------") 
    Tot_Sales_priceDsp = "${:,.2f}".format(Tot_Sales_price)
    print(f"                                         Total Sales Price:         {Tot_Sales_priceDsp:<10}")
    print()
    print(f"------------------------------------------------------------------------------------------------")
    print()
    print(f"                                   Financing      Total         Monthly ")    
    print(f"          # Years     # Payments      Fee         Price         Payment")
    print(f"         -------------------------------------------------------------------")
    for years in range(1, 5):
        NumPayments = years * 12
        FinFeeTot = FINANCE_FEE_RATE * years
        TotPriceFin = float(Tot_Sales_price) + FinFeeTot
        MonthPay = TotPriceFin / NumPayments

        FinFeeTotDsp = "${:,.2f}".format(FinFeeTot)
        TotPriceFin = "${:,.2f}".format(TotPriceFin)
        MonthPay = "${:,.2f}".format(MonthPay)
        print(f"              {years:<4}         {NumPayments:<2}        {FinFeeTotDsp:<10}  {TotPriceFin:<10}     {MonthPay}")
    print("         --------------------------------------------------------------------")
    print(f"           Invoice Date: {InvDate2:<7s}              First Payment Date: {FtimePay:<7s}")
    print()
    print()
    print("-------------------------------------------------------------------------------------------------")
    print(f"                                Best Used Cars At The Best Prices!")
    print()
    print()
    
    Continue = input(" Enter The Customers First Name (END to quit): ").upper()         
    if Continue == "END":
        break