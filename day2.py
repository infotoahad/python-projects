# Tip calculator!!!
print("Welcome to the tip calculator!!!")
bill = float(input("What is the total bill? "))
tip = int(input("How much do you want to tip? "))
people = int(input("How many people to split? "))
tipped_bill = tip / 100 * bill + bill
print(tipped_bill)
total_bill = bill + tipped_bill
bill_per_person = total_bill / people
final_amount = round(bill_per_person)
print(f"Each person should pay rs.{final_amount}")
