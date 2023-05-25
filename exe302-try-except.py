sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Errot, pleace enter numeric input")
    quit()

# print(fh, fr)
if fh > 40:
    print("Overtime")
    reg = fh * fr
    otp = (fh - 40.0) * (fr * 1.5)
    print(reg, otp)
    xp = reg + otp
else:
    print("Regulartime")
    xp = fh * fr
print("Pay: ", xp)

n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)
