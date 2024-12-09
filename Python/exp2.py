# WAP to illustrate iteration over the list and dictionary

lst = [10, 20, 30, 40, 50, 100]
for i in lst:
    print(i, end=" ")
dictionary = {"name" : ["i","n","p","d","h","s"], "age":[18,19,18,19,19,19]}
print("\n")
for j in dictionary.keys():
    print(j, end=" ")

print()

for i in dictionary.values():
    print(i,end=" ")