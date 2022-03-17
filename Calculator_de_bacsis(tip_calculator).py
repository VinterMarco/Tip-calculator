print("Welcome to the tip calculator!")
bill = float(input("How much was the bill?: $"))
tip = int(input("You want to tip 10,12 or 15? "))
people = int(input("How many people share the bill?: "))

bill_with_tip = tip / 100 * bill + bill
shared_bill_with_tip = bill_with_tip / people
print(f"THe total bill with the tip of {tip} % is : {bill_with_tip} $ ")
print(f"The shared bill with {people} people is {shared_bill_with_tip}")
print(f"And the bill without the tip is {bill} $")


