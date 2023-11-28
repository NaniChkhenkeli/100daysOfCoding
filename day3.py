# height = float(input()) 
# weight = int(input()) 

# bmi = weight / (height ** 2) 
# if bmi < 18.5:
#     print(f"your bmi is{round(bmi, 2)}, you are underweight. ")
# elif bmi < 25:
#     print(f"your bmi is {round(bmi, 2)}, you are normal weight! ")
# elif bmi < 30: 
#     print(f"yout bmi is {round(bmi, 2)}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"your bmi is {round(bmi, 2)}, you are obese. ")
# else:
#     print(f"your bmi is {round(bmi, 2)}, you are clinically obese. ")



# PizzaProblem 
# Based on a user's order, work out their final bill.

# Small pizza (S): $15

# Medium pizza (M): $20

# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2

# Add pepperoni for medium or large pizza (Y or N): +$3

# Add extra cheese for any size pizza (Y or N): +$1
# code is : 


# print("Thank you for choosing Python Pizza Deliveries!")
# size = input()
# add_pepperoni = input()
# extra_cheese = input() 
# bill = 0
# if size == "S" :
#     bill += 15
# elif size == "M" :
#     bill += 20 
# else: 
#     bill += 25 

# if add_pepperoni == 'Y' :
#     if size == 'S' :
#         bill += 2
#     else :
#         bill += 3 

# if extra_cheese == 'Y' :
#     bill += 1

# size = print(f" your final bill is ${bill}")


# love calculator 
print("love calculator is calculating your score...")
name1 = input() 
name2 = input()

combined_names = name1 + name2 
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u") 
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v") 
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if(score < 10) or (score > 90) :
    print(f"your score is {score}, you go together like coke and mentos.")
elif(score >= 40) and (score <= 50) :
    print(f"your score is {score}, you are alright together, RUN")
else :
    print(f"your score is {score}. keep looking around. xaxa ")
