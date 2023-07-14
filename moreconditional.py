hrs = input("Enter Hours:")
pph = input("Enter hourly pay:")
h = float(hrs)
p = float(pph)

if h <= 40:
    pay = h * p
elif h > 40:
    overtime_hrs = h - 40
    overtime_pay = overtime_hrs * p * 1.5
    regular_pay = 40 * p
    pay = regular_pay + overtime_pay
    
print(pay)