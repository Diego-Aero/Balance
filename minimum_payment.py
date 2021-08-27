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

annualInterestRate=0.2
balance=3926
balanceInitial=balance
high=balance*(1+annualInterestRate/12)**12/12
#Un buen valor inicial es la paga del tiron con todos los intereses acumulados en el ultimo mes
#Un buen límite superior para el pago mensual sería una doceava parte del saldo, después de tener sus intereses compuestos mensualmente durante todo un año.
low=balance/12
#Un buen valor inicial es la doceaba parte puesto que si no hay intereses
#la deuda puede pagarse asi en los doce meses
epsilon=0.01
while balance:
    balance=balanceInitial
    minimumPayment=(high+low)/2
    balance=PayingDebt(minimumPayment, balance, annualInterestRate)
    if abs(balance)<=epsilon:
        break
    else:
        if balance>0:
            low=minimumPayment
        elif balance<0:
            high=minimumPayment

print('Lowest payment:', round(minimumPayment, 2))
