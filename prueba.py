balance=484
annualInterestRate=0.2
monthlyPaymentRate=0.04
i=0

while i<12 and balance >=0:
    unpaid=balance-monthlyPaymentRate*balance
    interest=annualInterestRate/12*unpaid
    balance=unpaid+interest
    i+=1

print('Remaining balance:', round(balance, 2))
