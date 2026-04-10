n = 120
count = 0
for i in range(2, n + 1):
    if n % i == 0:
        n = n // i
        print("prime facotr", i)
