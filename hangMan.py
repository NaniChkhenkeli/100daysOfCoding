
import random 

import hangmanWords
chosen_word = random.choice(hangmanWords.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#from hangmanArt import logo 
#print(logo)
import hangmanArt
print(hangmanArt.logo)



print(f'solution is {chosen_word}')

display = [] 
for _ in range(word_length):
    display += "_" 


while not end_of_game:
    guess = input("guess a letter: ").lower() 

    if guess is display:
        print(f"you have already guessed {guess} ")



    for position in range(word_length):
        letter = chosen_word[position] 
        if letter == guess: 
            display[position] = letter 
     #   else:
       #     print("no match") 
    if guess not in chosen_word:

        print(f"you guessed{guess}, lose a life")
        lives -= 1 
        if lives == 0:
            end_of_game = True
            print("you lose.")

    print(f"{' '.join(display)}") 
    if "_" not in display:
        end_of_game = True 
        print("you win))")

    from hangmanArt import stages 
    print(stages[lives]) 

