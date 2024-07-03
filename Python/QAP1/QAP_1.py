# Program for The Edsel Car Rental Company
# Author: Logan Oram
# Dates: Jan 19, 2024

# Define program constants.

CAR_RENT_CHARGE = 55.00
KILO_TRAVEL = .24
INSURE_COST = 14.00
DIS_RENTAL = .10
DIS_MILAGE = .25
HST = .15


# Gather user information.

CustName = input("Please enter the customer name: ")
CustPhoNum = input("Please enter your phone number: ")
RentDays = int(input("Please enter the amount of days rented with us: "))
OdoReadBefore = int(input("Please enter the vehicle odometer reading before rented (Ex: 99999): "))
OdoReadAfter = int(input("Please enter the vehicle odometer reading after rented (Ex: 99999): "))


# Generate program results through calculations.

TotKilometers = OdoReadAfter - OdoReadBefore

RentalCost = CAR_RENT_CHARGE * RentDays

MilageCost = TotKilometers * KILO_TRAVEL

InsuranceCost = RentDays * INSURE_COST

DiscountRental = RentalCost * DIS_RENTAL

DiscountMilage = MilageCost * DIS_MILAGE

TotalDis = DiscountRental + DiscountMilage 

TotalRentCost = RentalCost + MilageCost + InsuranceCost - TotalDis

calcHST = TotalRentCost * HST

FinalInvoice = TotalRentCost + calcHST

# Display user results to the screen.

print(f"----------------------------------------------------") 
print(f"          The Edsel Car Rental Company")
print(f"            Customer Rental Summary")
print(f"----------------------------------------------------") 
print(f"Customer Name:                      {CustName:>5s}") 
print(f"Customer Phone Number:              {CustPhoNum:>10s}")
print(f"Rental day's:                       {RentDays:>2}")
print(f"Odometer Before Rental:             {OdoReadBefore:>5}") 
print(f"Odometer After Rental:              {OdoReadAfter:>5}") 
print(f"----------------------------------------------------") 
print(f"Total Kilometers Traveled           {TotKilometers:>5}") 
print(f"Rental Cost                         {RentalCost:>5}")
print(f"Milage Cost                         {MilageCost:>5}") 
print(f"insurance Cost                      {InsuranceCost:>5}") 
print(f"Total Discount                      {TotalDis:>5}") 
print(f"Total Rental Cost                   {TotalRentCost:>5}") 
print(f"HST                                 {calcHST:>5}")
print(f"----------------------------------------------------")
print(f"Final Invoice Total                 {FinalInvoice:>5}")
print(f"----------------------------------------------------")
print(f"Thank You For Choosing The Edsel Car Rental Company")
print(f"                See You Soon :)")
print(f"----------------------------------------------------")
print()
print()