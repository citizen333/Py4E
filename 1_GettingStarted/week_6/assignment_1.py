def computepay(h,r):
    if (h <= 40):
        pay = h * r
    else:
        pay = 40 * r + (h - 40) * r * 1.5
    return pay

hrs = input("Enter Hours:")
hrs = float(hrs)
rt = input("Enter Rate:")
rt = float(rt)
p = computepay(hrs,rt)
print(p)
