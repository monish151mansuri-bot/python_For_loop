password = input("Enter password:-- ")
A = False
B = False
C = False
size = len(password)
# check at least one number
for i in range(0, size):
    if password[i] >= "a" and password[i] <= "z":
        A = True
    elif password[i] >= "0" and password[i] <= "9":
        B = True
    else:
        C = True

if size >= 10 and A and B and C:
    print("valid password ")
else:
    print("invalid password ")
