# WAP to reverse the kth row in a matrix

n = int(input("Enter the number of rows: "))
mat = []
for i in range(n):
    row = [int(x) for x in input(f"Enter row {i+1}: ").split()]
    mat.append(row)
k = int(input("Enter k: "))
mat[k-1] = mat[k-1][::-1]
print("Modified matrix")
for row in mat:
    print(row)