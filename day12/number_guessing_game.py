from random import randint


EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

turns=0

#function to check user's guess against actual answer 
def check_answer(user_guess, actual_answer,turns ):
    if user_guess > actual_answer:
        print("Too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low:")
        return turns - 1 
    else:
        print(f"You got it! The answer was {actual_answer}")
        
#Function to set difficulty 
def set_difficulty():
    level = input("Choose a difficulty Type 'easy' or 'hard': ")
    if level=="easy":
       return  EASY_LEVEL_TURNS
    else:
       return HARD_LEVEL_TURNS
        
    


#choose a random number between 1 and 100 
def game():
    print("Welcome to the number guessing game!")
    print("I am thinking of number between 1 and 100")
    answer = randint(1,100)

    turns=set_difficulty()
    

    guess=0
    while guess!= answer:
        print(f"You have {turns} attemps remaining to guess the number.")
        #let the user guess a number
        guess = int(input("Make a guess: "))

        turns= check_answer(guess,answer,turns)
        if turns == 0:
            print("You have run out of guesses, you lose.")
            return 
        elif guess != answer:
            print("Guess Again")
        
        
game()
