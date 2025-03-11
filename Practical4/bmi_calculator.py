# input the person's weight
# input the person's height
# calculate for the BMI = weight / height**height
# print BMI
# if BMI > 30:
    # print ("obese")
# elif BMI < 18.5:
    # print ("underweight")
# else:
    # print ("normal weight")
weight = float (input("What's your weight in kg? "))
height = float (input("What's your height in m? "))
BMI = weight / height**2
print ("your BMI is" + str(BMI))
if BMI > 30:
    print ("obese")
elif BMI < 18.5:
    print ("underweight")
else:
    print ("normal weight")