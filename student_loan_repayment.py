#Loan repayment plan

loan_table = [[3376.0,4.290],[6601.0,4.290],[1685.0,3.760],[3203.0,3.760],[1755.0,4.450],[3292.0,4.450],[4500.0,5.050],[5752.0,5.050],[2250,4.530],[3021.0,4.530]]
list_payments = []
MAX = len(loan_table)
total_paid = 0
monthly_payment = 367.0
number_payments = []
total_interest = 0.0
interest = []
owed = 0.0
total_payments = 0.0
total_owed = 0.0
#First get the total number of payments
for i in range(0,MAX):
    total_owed += loan_table[i][0]*2
    
#Now we need to know what percentage of the total each loan is
percentage = []
for i in range(0,MAX):
    loan = loan_table[i][0]*2
    percentage.append(float(loan/total_owed)) 

for i in range(0,MAX):
    number_payments.append(0)
    loan = loan_table[i][0]*2
    yearly_rate = loan_table[i][1]
    #yearly_rate = 4.5
    monthly_rate = (yearly_rate/100)/12
    list_payments.append(0.0)
    monthly_percentage_payment = monthly_payment * percentage[i]
    interest.append(0.0)
    amount = 0.0
    #print("monthly rate = ",monthly_rate)
    while loan > 0:
        number_payments[i] += 1
        interest[i] += loan*(1 + monthly_rate) - loan
        total_interest += loan*(1 + monthly_rate) - loan
        loan = (loan*(1 + monthly_rate))
        if loan > monthly_percentage_payment :             
            amount =  monthly_percentage_payment
        else:
            amount = loan
        total_payments += amount
        list_payments[i] += amount
        loan -= amount
      
    
#Print the list of payments

for i in range(0,len(list_payments)):
    print("For loan : "+str(loan_table[i][0]*2)+" we paid a total of "+str(list_payments[i])+" an interest of "+str(interest[i]),end="")
    print(" number of payments for "+str(loan_table[i][0]*2)+" = "+str(number_payments[i]))
print("Total owed = ",total_owed," total paid = ",total_payments)
    
    