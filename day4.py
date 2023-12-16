import random 

random_integer = random.randint(1, 10)
print(random_integer)  


random_float = random.random()
print(random_float)

love_score = random.randint(1, 100)
print(f"love score is {love_score}")


number = random.randint(0,1)
if number == 1 : 
    print("Heads")
else : 
    print("Tails")


names_string = "Angela, Ben, Jenny, Michael, Chloe "
names = names_string.split(", ")
random_choice = random.randint(0, len(names) - 1)
print(names[random_choice])


fruits = ["apples", "pears", "grapes"]
vegetables = ["potatoes", "tomatoes", "celery"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)






line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Enter the position (e.g., A3): ")

letter = position[0].lower()
abc = ["a", "b", "c"]
if letter in abc:
    col = abc.index(letter)
    row = int(position[1]) - 1

    map[row][col] = 'X'

    print(f"{map[0]}\n{map[1]}\n{map[2]}")

else:
    print("Invalid input. Please enter valid coordinates.")
