height = input("Enter your height in feet and inches (e.g. 5 7): ")
height_ft, height_in = map(int, height.split())
weight_lb = float(input("Enter your weight in pounds: "))
# height_m = ((height_ft*12) + height_in ) * 0.025
# weight_kg = weight_lb * 0.45
# Create a function that calculates the BMI based on the height in inches and weight in pounds
# BMI = (weight in pounds / (height in inches * height in inches)) * 703

# bmi = weight_kg / (height_m ** 2)
bmi = (weight_lb/ (((height_ft*12) + height_in ) ** 2)) * 703
catergory = ""
if bmi < 18.5:
    catergory += "underweight"
elif 18.5 <= bmi <= 24.9:
    catergory += "of normal weight"
    
elif 25 <= bmi <= 29.9:
    catergory += "overweight"
   
else:
    catergory += "obese"
   

print("Your BMI is: {:.2f} and you are {}".format(bmi, catergory))