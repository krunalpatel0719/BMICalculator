class bmi_class:

    def bmi_category(self, bmi):
        if bmi < 18.4:
            return "underweight"
        elif 18.4 <= bmi <= 24.9:
            return "of normal weight"
        elif 25 <= bmi <= 29.9:
            return "overweight"
        else:
            return "obese"

    def calculate_bmi(self):
        height = input("Enter your height in feet and inches (e.g. 5 7 or 5 0): ")
        height_ft, height_in, *_ = map(int, height.split())
        weight_lb = float(input("Enter your weight in pounds: "))
        height_m = ((height_ft*12) + height_in ) * 0.025
        weight_kg = weight_lb * 0.45
        if height_ft < 0 or height_in < 0:
            raise ValueError("Height must be positive")
        elif height_ft == 0:
            raise ValueError("Height must be non-zero")
        elif height_in > 11:
            raise ValueError("Height in inches must be less than 12")
        elif weight_lb < 0:
            raise ValueError("Weight must be positive")
        elif weight_lb == 0:
            raise ValueError("Weight must be non-zero")
        

        bmi = weight_kg / (height_m ** 2)
        category = self.bmi_category(bmi)
        output = "Your BMI is: {:.2f} and you are {}".format(bmi, category)
        return output



def main():
    bmi = bmi_class()
    print(bmi.calculate_bmi())

if __name__ == "__main__":
    main()



    