print("Boolean Operation : Between two numbers, wheather they are egual, greater than or less than")

num1 = float(input("Please enter the First Number :   "))
num2 = float(input("Please enter the Second Number :   "))

if(num1 > num2):
    print(num1, "  is Greater than  ", num2)

elif(num1 == num2):
    print(num1, "  is Equal to  ", num2)

else:
    print(num1, "  is Less than  ", num2)
