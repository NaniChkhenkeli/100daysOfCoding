print("welcome to the island! mission is to find treasure! ")
choice1 =input("you are at a crossroad, where do you want to got? type left or right? - ").lower()
if choice1 == "left" :
        choice2 = input("do you wanna swin or wait? ").lower()
        if choice2 == "wait" :
            choice3 = input("which door to choose? red / blue / yellow / else - ")
        else: print("get attacked. ")
else: print("game over ((")

if choice3 == "red" :
        print("just burned in a fire ")
elif choice3 == "blue" :
        print("eaten by beasts(( ")
elif choice3 == "yellow" :
        print("you win! congrats ")
else: print("game over! ")
