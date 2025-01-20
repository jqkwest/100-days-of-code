import random

words = ["one","two","three","four","five","six"]

hang_state = [
    '''+-------+
       |    |
            |
            |
            |
            |''',
    '''+-------+"
       |    |
       O    |
            |
            |
            |''',
    '''+-------+
       |    |
       O    |
       |    |
       |    |
       |    |''',
    '''+-------+
       |    |
       O    |
     --|--  |
       |    |
       |    |''',
    '''+-------+
       |    |
       O    |
     --|--  |
       |    |
      /     |''',
    '''+-------+
       |    |
       O    |
     --|--  |
       |    |
      / \   |'''
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
        if guess not in word:
            bad_guess_count += 1
        for letter in word:
            if letter == guess:
                display += letter
                current_guess_state.append(letter)
            elif letter in current_guess_state:
                display += letter
            else:
                 display += "_ "
             
                        
        print(hang_state[bad_guess_count])
        print(display)
        if bad_guess_count == len(word):
            stil_guessing = False
    
    print("Sorry! Better luck next time!")

        




main()