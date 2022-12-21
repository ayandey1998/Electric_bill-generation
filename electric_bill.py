unit = int(input("Enter your unit: "))
if unit <= 100:
    bill = unit * 3.5
elif unit >= 101 and unit <= 300:
    bill = 346 + ((unit - 100) * 7.5)
elif unit >= 301 and unit <= 500:
    bill = 346 + 1486 + ((unit - 300) * 10.30)
else:
    bill = 346 + 1486 + 2064 + ((unit - 500) * 11.30)
print("Bill Per Unit:",bill)
bill = bill + (unit*1.45)
print("Bill after adding Line rent:",bill)
bill = bill + 100
print("Bill after adding Meter rent:",bill)
bill = bill + (bill*0.16)
print("Total Bill after adding tax:",bill)