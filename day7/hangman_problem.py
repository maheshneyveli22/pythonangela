word_list = ["aardvark","baboon","camel"]

import random

# 1 Randomly choose a word from word_list and assign to
#variable called chosen_word, then print it 
# Then create a "placeholder" with the same number of blanks as the 
# chosen_word 
chosen_word = random.choice(word_list)

print(chosen_word)
placeholder = ""
for position in range (0,len(chosen_word)):
    placeholder+="_"
print(placeholder)

correct_letters =[]

# 2 Quess a letter and assign their answer to a variable called guess and make guess lowercase 
while not game_over:
    guess= input("Guess a letter ").lower()

print(guess)


#Create a "display" that puts the guess letter in the right positions and  rest positions as blank 
display =""


# 3 Check if the letter in the user guessed(guess) is one of the 
# letters in chosen_word. Print "Right" if it matches any of the ltters and "wrong" if it does not match 
for letter in chosen_word:
   if letter == guess:
       display+=letter
    
   else:
       display +="_"
       
print(display)