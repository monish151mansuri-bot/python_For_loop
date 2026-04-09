# Write a program to find the first and last digit of a number.
n = 1479752419
temp = len(str(n))
rem = n % 10
f = 0
for i in range(temp):
    n = n // 10
    if n > 0 and n <= 10:
        f = n
print("first digits", f)
print("Last  digits ", rem)
