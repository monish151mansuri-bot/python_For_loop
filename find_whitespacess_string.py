str = "he llo ev ery one"
count = 0
for i in range(len(str)):
    if str[i] == " ":
        count = count + 1
print(count)
