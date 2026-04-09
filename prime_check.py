n = 12
a = False
for i in range(2, n):
    if n % i == 0:
        a = True
    else:
        a = False

if a == True:
    print("not prime")
else:
    print("prime number")
