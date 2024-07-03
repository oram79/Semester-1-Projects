# Program for the St.John's Marina & Yacht Club
# Author Logan Oram
# Date Feb 1st, 2024

#import libraries

# define program constants

EVEN_NUM_SITE = 80.00
ODD_NUM_SITE = 120.00
EXTRA_MEM = 5.00
WEEK_SITE_CLEAN = 50.00
VIDEO_SURV = 35.00
MONTH_CHAR_S = 75.00
MONTH_CHAR_E = 150.00
PROCESS_FEE = 59.99
CANCEL_FEE = 0.60
MONTH_DUE_S = 75.00
MONTH_DUE_E = 150.00
PROCESS_FEE = 59.99
HST = .15

# Gather user information

Current_Date = input("Please Enter The Current Date: (YYYY-MM-DD) ")
Site_Num = int(input("Enter The Site Number: "))               
Member_Name = input("Enter The Client Name: ")
Street_Address = input("Enter The Customers Address: ")
City = input("Enter The Clients City: ")
Province = input("Enter The Clients Province: (XX) ").upper()
Postal_Code = input("Enter The Clients Postal Code: (A1A 1A1) ").upper()
Phone_Num_H = input("Enter The Clients Phone Number: (H) ")
Phone_Num_C = input("Enter The Clients Phone Number: (C) ")

Member_Type = (input("Enter The Member Type They Chosen: (S) Or (E) ")).upper()
if Member_Type == "S":
    Mem_Type = "Standard"
else:
    Mem_Type = "Executive"

Extra_Mem = int(input("Was There Any Extra Members? (0-5) "))

Week_Site_Clean = input("Weekly Site Cleaning? (Y) Or (N) ").upper()
if Week_Site_Clean == "Y":
    Site_Clean = "Yes"
else:
    Site_Clean = "No"

Video_Surv = input("Video Surveillance? (Y) Or (N) ").upper()
if Video_Surv == "Y":
    Vid_Sur = "Yes"
else:
    Vid_Sur = "No"

# Generate program results through calculations.

if Site_Num % 2:
    Site_Charge = EVEN_NUM_SITE
else:
    Site_Charge = ODD_NUM_SITE

Tot_Site_Charge =  Site_Charge + (EXTRA_MEM * Extra_Mem)

if Video_Surv == "Y":
    Vid_Charge = VIDEO_SURV
else:
    Vid_Charge = 0

if Week_Site_Clean == "Y":
    Site_Charge = WEEK_SITE_CLEAN
else:
    Site_Charge = 0 

Extra_Charge = Site_Charge + Vid_Charge
Sub_Total = Tot_Site_Charge + Extra_Charge
CalcHST = Sub_Total * HST
Total_month_Charge = Sub_Total + CalcHST

if Mem_Type == "S":
    Month_dues = MONTH_CHAR_S
else:
    Month_dues = MONTH_CHAR_E

Total_monthly_fee = Total_month_Charge + Month_dues
Total_Year_Fees = Total_monthly_fee * 12
Monthly_payment = (Total_Year_Fees + PROCESS_FEE) / 12
Cancel_fee = Total_Year_Fees * CANCEL_FEE



# Display user results to the screen.
print(f"----------------------------------------")
print(f"      St.John's Marina & Yacht Club")
print(f"         Yearly Member Receipt ")
print(f"----------------------------------------")
print(f"Client Name And Address:")
print()
print(f"{Member_Name:<10s}")
print(f"{Street_Address:<10s}")
print(f"{City:<10s},{Province:<2s} {Postal_Code:<6s}")
print()
print(f"Phone: {Phone_Num_H:<10s}"  "(H)") 
print(f"       {Phone_Num_C:<10s}"  "(C)")
print()
print(f"Site #: {Site_Num:<2d} Member Type: {Mem_Type:<9}")
print()
print(f"Alternate Members:               {Extra_Mem:<2}")
print(f"Weekly Site Cleainig:            {Site_Clean:<3s}")
print(f"Video Surveillance:              {Vid_Sur:<3s}")
print()
Tot_Site_ChargeDsp = "${:,.2f}".format(Tot_Site_Charge)
print(f"Site Charges:                    {Tot_Site_ChargeDsp:<4s}")
Extra_ChargeDsp = "${:,.2f}".format(Extra_Charge)
print(f"Extra Charges:                   {Extra_ChargeDsp:<4s}")
print("                                 -------")
Sub_TotalDsp = "${:,.2f}".format(Sub_Total)
print(f"Subtotal:                        {Sub_TotalDsp:<5}")
CalcHSTDsp = "${:,.2f}".format(CalcHST)
print(f"Sales Tax (HST):                 {CalcHSTDsp:<5}")
print("                                 -------")
Total_month_ChargeDsp = "${:,.2f}".format(Total_month_Charge)
print(f"Total Monthly Charges:           {Total_month_ChargeDsp:<5}")
Month_duesDsp = "${:,.2f}".format(Month_dues)
print(f"Monthly Dues:                    {Month_duesDsp:<5}")
print("                                 -------")
Total_monthly_feeDsp = "${:,.2f}".format(Total_monthly_fee)
print(f"Total Monthly fees:              {Total_monthly_feeDsp:<5s}")
Total_Year_FeesDsp = "${:,.2f}".format(Total_Year_Fees)
print(f"Total Yearly Fees:             {Total_Year_FeesDsp:>5s}")
print()
Monthly_paymentDsp = "${:,.2f}".format(Monthly_payment)
print(f"Monthly Payment:                 {Monthly_paymentDsp:>5s}")
print(f"----------------------------------------")
print()
print(f"Issued: 2024-02-04")
print(f"HST Reg No: 549-33-5849-4720-9885")
print()
Cancel_feeDsp = "${:,.2f}".format(Cancel_fee)
print(f"Cancellation Fee:              {Cancel_feeDsp:>5s}")
print(f"----------------------------------------")