sentence = input("Enter sentence")
cnt = 0
for i in sentence:
    if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        cnt = cnt + 1

print("Count = ",cnt)
