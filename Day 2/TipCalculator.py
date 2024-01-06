#Tip Calculator

print("Welcome to tip calculator!")
bill= float(input("What was your total bill?\n$"))

percent_tip = int(input("How much tips would you like to pay?\n%"))

num_people = int(input("How many people to split the bill with?\n"))


bill_t = bill * (percent_tip/100)
total_bill= bill + bill_t
each_person = round(total_bill/num_people,2)

print(f"Each person should pay : ${each_person}")