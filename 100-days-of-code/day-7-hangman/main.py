import random

word_list = ["one","two","three","four","five","six"]



def main():
    
    empty_char = "_ "
    word = random.choice(word_list)
    word_length = len(word)
    print("Welcome to hangman... you know what to do!")
    print("\n" *4)
    print(word)  # temp for checking the game

    print(empty_char * word_length)
    print("\n" *4)





main()