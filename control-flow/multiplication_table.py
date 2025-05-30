# Multiplication Table Generator.

number = int(input("Enter a number to see its multiplication table: "))

# the nested loop 
for i in [number]:
    # print(number)
    for j in range(1,11):
        print(f"{number} * {j} = {number*j}")