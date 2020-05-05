print("Calculation of Body Mass Index (BMI) " )

weight = float(input("Please enter your Weight :  "))
height = float(input("Please enter your Height :  "))

bmi = weight / (height * height)

print("Your Body Mass Index (BMI) is :  ", round(bmi , 2))

if(bmi <= 18.5):
    classification = "Underweight"
elif(bmi > 18.5 and bmi < 24.9):
    classification = "Normal Weight"
elif(bmi >24.5 and bmi <29.9):
    classification = "Overweight"
else:
    classification = "Obesity"

print("Your BMI Classification is :  " , classification)
