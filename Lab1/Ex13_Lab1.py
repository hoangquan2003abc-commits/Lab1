weight=float(input("Enter your weight(kg):"))
height=float(input("Enter your height(m):"))
BMI=weight/(height**2)
if BMI<18.5:
    print("BMI=",BMI,"-> Underweight")
elif BMI<25:
    print("BMI=",BMI,"-> Normal")
elif BMI<30: 
    print("BMI=",BMI,"-> Overweight")
else: 
    print("BMI=",BMI,"->Obese")
     