hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)
base = 40
m = 1.5
if h <= base:
    pay = h*r
else:
     pay = ((h - base) * m + base) * r
print(pay)
