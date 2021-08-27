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
