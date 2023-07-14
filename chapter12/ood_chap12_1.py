print(" *** BMI ***")
weight,height = (input("Enter your weight(kg) and height(m) : ")).split()


BMI = float(weight)/ (float(height)*float(height))
def calculator(BMI):
    if BMI < 18.5:
        return("Below normal weight.")
    if 18.5 <= BMI < 25:
            return("Normal weight.")
    if 25 <= BMI < 30:
            return ("Overweight.")
    if 30 <= BMI < 35:
            return("Case I Obesity.")
    if 35 <= BMI < 40:
            return("Case II Obesity.")
    if BMI >= 40:
            return("Case III Obesity.")

print("Your status is :",calculator(BMI))   