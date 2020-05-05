print("Grade evaluation of a student with input from the user.")

data_valid = False
while data_valid == False :
    grade1= float(input("Please enter the secured grade in 1st Term  Examination :  "))
    if grade1 < 0 or grade1 > 10 :
        print("Grade should be in the range of 0 to 10")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False :
    grade2= float(input("Please enter the secured grade in 2nd Term  Examination :  "))
    if grade2 < 0 or grade2 > 10 :
        print("Grade should be in the range of 0 to 10")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False :
    total_classes = int(input("Please enter the number of Total Classes :  "))
    if total_classes <= 0 :
        print("Total Classes should be greater than 0")
        continue
    else :
        data_valid = True

data_valid = False
while data_valid == False :
    absence = int(input("Please enter the number of Absent Classes :  "))
    if absence < 0 or absence > total_classes :
        print("Absense should be in the range of 0 to Total number of Classes")
        continue
    else :
        data_valid = True

avg_grade = (grade1 + grade2)/2
attendance = (total_classes - absence) / total_classes

print("Average Grade of the student is :  ", round(avg_grade,2))
print("Attendance Rate of the student is :  ",  str(round((attendance * 100) , 2)) + '%')

if(avg_grade >= 6):
    if(attendance >= 0.8):
        print("The student has been PROMOTED")
    else:
        print("The student has FAILED due to Less Attendace")
elif(attendance >= 0.8):
    print("The student has FAILED due to Lower Grade")
else:
    print("The  student has FAILED due to Lower Attendance & Grade")

