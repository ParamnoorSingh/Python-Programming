# Create a database using list and tuples

database = [(1, "Pankaj Solanki", 17, "Maths"),
            (2, "Shivani Sharma", 18, "English"),
            (3, "Aver Khurana", 18, "Science"),
            (4, "Shaurya Arora", 18, "Hindi")
            ]
def display_data(data):
    print("ID   | Name            | Age | Subject")
    print("-"*30)
    for i in data:
        print(f"{i[0]:<4} | {i[1]:<15} | {i[2]:<3} | {i[3]}")

def add_data(data, id, name, age, subject):
    data.append((id,name,age,subject))

def delete_row(data , id):
    data.pop(id-1)

print("Initial Database: ")
display_data(database)
print()
add_data(database,5,"Reyansh Singh", 10, "Economics")
delete_row(database, 3)
display_data(database)