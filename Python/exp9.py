# Write a program to implement an employee management system using classes, instances, and inheritance.

class Database:
    def insert_data(self, id, name, age, salary):
        self.data = []
        self.data.append((id,name,age,salary))
    def display_data(self):
        print("ID   | Name            | Age | Subject")
        print("-"*30)
        for i in self.data:
            print(f"{i[0]:<4} | {i[1]:<15} | {i[2]:<3} | {i[3]}")
    
class Database2(Database):
    def add_data(self, id, name, age, salary):
        self.data.append((id, name, age, salary))
    def remove_row(self, id):
        self.data.pop(id-1)

d = Database2()
d.insert_data(1, "Shivam Sharma", 25, 50000)
d.add_data(2, "Akshi Singh", 23, 48000)
d.add_data(3, "Mani Gupta", 28, 60000)
d.add_data(4, "Revansh Kumar", 29, 70000)

print("Initial Data")
d.display_data()
d.remove_row(4)
print("\n Updated Data")
d.display_data()