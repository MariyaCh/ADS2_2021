import random
import string

message = "Version Control System is fun"
message = message.lower()
endmessage = ""
list1 = list(string.ascii_lowercase)
list2 = []
crypto = {}

number = random.randint(1, 26)

print("ROT " + str(number) + " cipher")

firstchange = list1[:number]
secondchange = list1[number:]

for letter in secondchange:
    list2.append(letter)
for letter in firstchange:
    list2.append(letter)

for (x, y) in zip(list2, list1):
    crypto[x] = y

for encryptedletter in message:
    if encryptedletter == " ":
        endmessage = endmessage + " "
    else:
        endmessage = endmessage + crypto[encryptedletter]

print(endmessage)
