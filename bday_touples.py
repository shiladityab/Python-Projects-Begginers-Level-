print("What is your Birthday Month ???")

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

birthday = input("Type your Birth Date in DD-MM-YYYY Format :  ")

index = int(birthday[3:5])-1

bd_month = months[index]

print("Your Birthday Month is :  ", bd_month)
