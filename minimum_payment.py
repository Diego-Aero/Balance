annualInterestRate=0.2
balance=3926

def PayingDebt(minimumPayment, balance, annualInterestRate):
    i=0
    while i<12:
        unpaid=balance-minimumPayment
        interest=annualInterestRate/12*unpaid
        balance=unpaid+interest
        i+=1
    return balance

balanceInitial=balance
minimumPayment=0
while balance:
    balance=balanceInitial
    balance=PayingDebt(minimumPayment, balance, annualInterestRate)
    if balance<=0:
        break
    else:
        minimumPayment+=10

print('Lowest payment:', minimumPayment)
