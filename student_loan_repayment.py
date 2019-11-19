#Loan repayment plan
# The arrray below has loans in the format [[LOAN,APR],[LOAN,APR]...] where APR stands for annual percentage rate
loan_table = [[3376.0,4.290],[6601.0,4.290],[1685.0,3.760],[3203.0,3.760],[1755.0,4.450],[3292.0,4.450],[4500.0,5.050],[5752.0,5.050],[2250,4.530],[3021.0,4.530]]
list_payments = []
MAX = len(loan_table) #MAX is the number of loans taken and what are their respective percentage rate
total_paid = 0
MULTIPLIER = 1 # here I just want to see what happens if I had taken that same amount twice, thrice or N-TIMES
monthly_payment = 367.0 * MULTIPLIER
number_payments = []
total_interest = 0.0
interest = []
owed = 0.0
total_payments = 0.0
total_owed = 0.0
#First get the total number of payments
for i in range(0,MAX):
    total_owed += loan_table[i][0] * MULTIPLIER
    
#Now we need to know what percentage of the total each loan is
percentage = []
for i in range(0,MAX):
    loan = loan_table[i][0] * MULTIPLIER
    percentage.append(float(loan/total_owed)) 

for i in range(0,MAX):
    number_payments.append(0)
    loan = loan_table[i][0] * MULTIPLIER
    #yearly_rate = 4.5 This is the average apr.
    yearly_rate = loan_table[i][1] #here I am using the actual APR for each loan. I could however set the APR to be the same for all the loans
    monthly_rate = (yearly_rate/100)/12
    list_payments.append(0.0)
    monthly_percentage_payment = monthly_payment * percentage[i]
    interest.append(0.0)
    amount = 0.0
    #print("monthly rate = ",monthly_rate)
    while loan > 0:
        number_payments[i] += 1
        interest[i] += loan*(1 + monthly_rate) - loan
        loan = (loan*(1 + monthly_rate))
        if loan > monthly_percentage_payment :             
            amount =  monthly_percentage_payment
        else:
            amount = loan
            #print("last maount for "+str(loan_table[i][0])+" = "+str(amount))
        total_payments += amount
        list_payments[i] += amount
        loan -= amount
      
    
#Print the list of payments
for i in range(0,len(list_payments)):
    print("For loan : "+str(loan_table[i][0]*MULTIPLIER)+" we paid a total of "+str(list_payments[i])+" an interest of "+str(interest[i]),end="")
    print(" number of payments made : "+str(number_payments[i]))
print("Total owed = ",total_owed," total paid = ",total_payments)
    
    
