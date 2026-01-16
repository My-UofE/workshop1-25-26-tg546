import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):

    #print("possible values", poss_values)

    #get max and min values, floor divide them by 2 and select the middle value as the selection every time
    minimum = min(poss_values)
    maximum = max(poss_values)
    value = (minimum + maximum) // 2

    return poss_values[len(poss_values)//2]

    """
    x = random.choice(poss_values)   
    return x
    """

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if (current_val < next_val) and user_input == "h":
        return True
    if (current_val < next_val) and user_input == "l":
        return False

    if (current_val > next_val) and user_input == "l":
        return True
    if (current_val > next_val) and user_input == "h":
        return False


# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                board[i] = letter
        
        print(f"Well done! {letter} is in the word")
        return True
    else:
        print(f"Sorry, {letter} is not in the word")
        return False
