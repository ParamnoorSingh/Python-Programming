# WAP that inputs a text file the program should print all unique words in alphabetical order

file = open("text.txt","w")
file.write("hi, how are you?\nI am good wbu\nI am fine too, have a good day then.\n")
file = open("text.txt","r")
f = file.readlines()
file = open("text.txt","w")
un = []
for i in f:
    for j in i.split():
        un.append(j)
un.sort()
for k in un:
    if un.count(k) == 1:
        print(k)
file.close()
file = open("text.txt","r")
print(file.read())
file.close()