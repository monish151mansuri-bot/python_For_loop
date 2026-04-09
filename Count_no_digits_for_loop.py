# Write a program to count the number of digits in a number.
n = 10564723
count = 0
temp = len(str(n))
for i in range(temp):
    count = count + 1

print(count)
