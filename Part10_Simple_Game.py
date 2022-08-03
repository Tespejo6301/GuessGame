###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
# digits = list(range(10))
# random.shuffle(digits)
# print(digits[:3])

# convert the users guess to a type list of integers
def con_guess(guess):
    x = []
    if len(guess) == 0:
        return x
    for i in range(0, 3):
        x.append(int(guess[i]))
    return x    

# generate a code
def generate_code ():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]

# check the users guess if it is same as the code
def test_guess(code, guess):
    if code == guess:
        return True
    print_feedback(code, guess)    
    return False    

#provide feedback about user guess    
def print_feedback(code, guess):
    num_wrong = 0
    for i in range(0, 3):
        if code[i] == guess[i]:
            print("Match")
        elif guess[i] in code:
            print("Close")
        else:
            num_wrong = num_wrong + 1
    if num_wrong == 3:
        print("Nope")        


#run the code
isMatch = False
code = generate_code()
print(code)
while isMatch != True:
    x = (input("What is your guess? "))
    if len(x) != 3:
        print("Need a three digit guess\n")
    else: 
        guess = con_guess(x)
        isMatch = test_guess(code, guess)
        if isMatch == True:
            print("Congrats on breaking the Code!")    
    

    
    
        






