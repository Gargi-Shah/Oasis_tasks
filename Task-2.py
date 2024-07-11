def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")

    while True:
        c=input('\nEnter y to check your BMI: ')
        if c=='y' or c=='Y':
            weight = float(input("\nEnter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))
            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height must be positive numbers.")
                break
        else:
            break
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print('\nYour BMI is',bmi)
        print("Based on your BMI, you are classified as:",category)
 
main()
