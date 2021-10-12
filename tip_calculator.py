# A print statement that introduces the app
print('Welcome to Tylers tip calculator!')
# A variable that represents the total bill before tip / tax by prompting user input and turns the input into a float
bill_total = float(input('What is the total for the bill?: '))
# A variable that represents what percentage the user wants to tip by prompting user input and turns the input into a float
tip_percentage = float(input('What percentage would you like to add for the tip?: '))
# A variable that represents the total amount of people splitting the bill by prompting user input and turns the user input into an integer
total_people = int(input('How many people will be splitting the bill?: '))

# Line 12 calculates what the bill is including the tip provided by user input
bill_before_tax = bill_total * (tip_percentage/100 + 1)
# line 14 impliments tax by multiplying the bill total w/ out tip by .1, which represents 10 percent sales tax
tax = bill_total * .1
# line 16 calculates the total bill with tax and tip included by adding the taxes on the bill total to the bill with the tip
final_w_tax = round(bill_before_tax + tax,3)
# line 18 calculates what each person owes towards the total bill with tip included by divided the total by the amount of people
split = round(final_w_tax / total_people,2)
#line 20 + 21 prints the total bill and what each person owes for the bill with tip 
print(f'Total Bill: ${final_w_tax}')
print(f'Each person owes ${split} towards the bill, including tip and tax!')
