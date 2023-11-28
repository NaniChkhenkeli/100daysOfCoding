# num_char = len(input("what is your name?"))
# new_num_char = str(num_char)
# print("your name contains " + new_num_char + " characters.")   

# a=str(125)
# print(type(a)) 

#print(round(8 / 3, 2))

#print(8 // 3)


# height = input()
# weight = input()
# weight_as_int = int(weight) 
# height_as_float = float(weight) 
# bmi = weight_as_int/height_as_float ** 2 


# score = 0
# height = 1.8
# isWinning = True
# print(f"your score is {score}, 
#      your height is {height}, you are winning is {isWinning}")


# age = input()
# years = 90 - int(age) 
# week = years * 52
# print(f"you have {week} weeks left.") 

# two_digit_number = input()
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
# two_digit_number = first_digit + second_digit
# print(f"sum is {two_digit_number} .")  

# height = input()
# weight = input() 
# BMIi = int(weight) / float(height) ** 2 
# BMI = int(BMIi)
# print(BMIi)

# print("welcome to the tip calculator") 
# bill = float(input("what is the total bill? $"))
# tip = int(input("how much tip would u like to give? 10, 12, 15? "))
# people = int(input("how many people pay the bill? ")) 
# bill_with_tip = tip / 100 * bill + bill 
# print(bill_with_tip)
# amount_per_person = int(bill_with_tip / people) 
# print("Each person needs to pay: $", amount_per_person)


# print("welcome! ")
# height = int(input("what is your height? "))
# bill = 0
# if height >= 120 :
#     print("you can ride the rollercoaster! ")
#     age = int(input("what is your age? "))
#     if age < 12:    
#         print("childs tickets are $5. ")
#         bill = 5
#     elif age <= 18: 
#        print("Youth tickets are $7. ")
#        bill = 7
#     else: 
#        print("Adults tickets are $12. ")
#        bill = 12
#     wants_photo = input("do you want a photo taken? yes/ no.")
#     if wants_photo == "yes" :
#         bill = bill + 3

#     print(f"Your final bill is ${bill}")
        
# else :
#     print("sorry, failed. ")  



# number = int(input()) 
# if number % 2 == 0:
#   print(f"the number {number} is even. ")
# else :
#    print(f"the number {number} is odd. ")



# year = int(input()) 

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#     print("not leap year")







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

print("Thank you for choosing Python Pizza Deliveries!")
size = input()
add_pepperoni = input()
extra_cheese = input() 
bill = 0
if size == "S" :
    bill += 15
elif size == "M" :
    bill += 20 
else: 
    bill += 25 

if add_pepperoni == 'Y' :
    if size == 'S' :
        bill += 2
    else :
        bill += 3 

if extra_cheese == 'Y' :
    bill += 1

size = print(f" your final bill is ${bill}")
