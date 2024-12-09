# WAP to perform string operation on "Welcome to Python World"

# Count the number of alphabets in the given string
# To extract characters in the given range from the string
# Check if the string is alphanumeric or not

string = "Welcome to Python World"
count = 0
for i in string:
    if i != " ":
        count += 1
print(count)
print(string[0:17])
print(string.isalnum())