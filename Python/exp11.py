# Create a myfile ask the user to write 3 separate lines with 3 input statement from the user

file = open("myfile.txt","w")
a = input("Enter the first line: ")
b = input("Enter the second line: ")
c = input("Enter the third line: ")
file.write(a+"\n")
file.write(b+"\n")
file.write(c+"\n")
print("File created!!")
file = open("myfile.txt","r")
print(file.read())
file.close()