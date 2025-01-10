import random

words = ["one","two","three","four","five","six"]

hang_state = [
    "+-------+"
    "   |    |"
    "        |"
    "        |"
    "        |"
    "        |",
     "+-------+"
    "   |    |"
    "   O    |"
    "        |"
    "        |"
    "        |",
    "+-------+"
    "   |    |"
    "   O    |"
    "   |    |"
    "   |    |"
    "        |",
    "+-------+"
    "   |    |"
    "   O    |"
    " --|--  |"
    "   |    |"
    "        |",
    "+-------+"
    "   |    |"
    "   O    |"
    " --|--  |"
    "   |    |"
    "  /     |",
    "+-------+"
    "   |    |"
    "   O    |"
    " --|--  |"
    "   |    |"
    "  / \   |"
]

def main():
    
    empty_char = "_ "

    word = random.choice(words)
    word_length = len(word)
    stil_guessing = True
    current_guess_state=[]
    bad_guess_count = 0 
    
    print("Welcome to hangman... you know what to do!")

    while stil_guessing:
        display = ""

        print("\n" *4)
        print(word)  # temp for checking the game

        guess = input("Please guess a letter: " )
        for letter in word:
            if letter == guess:
                display += letter
                current_guess_state.append(letter)
            elif letter in current_guess_state:
                display += letter
            else:
                display += "_ "
                bad_guess_count += 1 #there is a bug here. It is counting  each iteration istead of just once
        
                
       # print(hang_state[bad_guess_count])
        print(display)
        print(bad_guess_count)




main()