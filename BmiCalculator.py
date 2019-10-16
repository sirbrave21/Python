weight = float(input("Enter your weight(kilogram): "))
height = float(input("Enter your height(centimeter): "))
height = height / 100
bmi = weight / height**2
print("Your BMI is: " , bmi)
if(bmi > 30):
    print("Obesity")
elif(bmi > 25 and bmi < 30):
    print("Overweight")
elif(bmi > 18.5 and bmi < 25):
    print("Normal Weight")
else:
    print("Underweight")