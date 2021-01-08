# Check a person is underweight, normal or obese given your weight and height
import math

weight = eval(input("What is your weight in pounds?: "))
height = eval(input("What is your height in inches?:" ))

KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254

weightInKilograms = weight * KILOGRAMS_PER_POUND
heightInMeters = height * METERS_PER_INCH
bmi = weightInKilograms / math.pow(heightInMeters,2)

print("BMI is: ", format(bmi, ".2f"))
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

    