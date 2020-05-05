print("Error Handling program")

number = input("Please enter the number :  ")

try:
    number = float(number)
    print("The number is :  ", number)
except:
    print("Invalid Input")
