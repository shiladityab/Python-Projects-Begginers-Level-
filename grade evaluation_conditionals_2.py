print("Grade evaluation of a student with input from the user.")

grade1 = float(input("Please enter the secured grade in 1st Term  Examination :  "))
grade2 = float(input("Please enter the secured grade in 2nd Term  Examination :  "))
absence = int(input("Please enter the number of Absent Classes :  "))
total_classes = int(input("Please enter the number of Total Classes :  "))

avg_grade = (grade1 + grade2)/2
attendance = (total_classes - absence) / total_classes

print("Average Grade of the student is :  ", round(avg_grade,2))
print("Attendance Rate of the student is :  " , str(round((attendance * 100),2)) + '%')

if(avg_grade >= 6 and attendance >= 0.8):
        print("The student has been PROMOTED")
elif(avg_grade < 6 and attendance < 0.8):
        print("The  student has FAILED due to Lower Attendance & Grade")
elif(attendance >= 0.8):
    print("The student has FAILED due to Lower Grade")
else:
    print("The  student has FAILED due to Lower Attendance")

