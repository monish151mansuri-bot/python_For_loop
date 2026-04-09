# Write a program to calculate the sum of digits of a number.
n = 10564723
sum = 0
temp = len(str(n))
for i in range(temp):
    rem = n % 10
    sum = sum + rem
    n = n // 10
print(sum)
