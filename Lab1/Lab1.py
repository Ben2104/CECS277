'''
    Name: Hoang Khoi Do
    Date: 08/26/2024
    Guessing Game Program:
    prompt the user to guess
    a number between 1 and 100. Test that the user’s input is an integer within the range, if it isn’t,
    tell them that it is invalid and allow them to continue guessing. Compare the user’s number to
    the computer’s number, if the user’s number is lower than the computer’s, tell them that it is too
    low, if it is higher, tell them that it is too high. Repeat until the user guesses the correct value.
    Keep count of the number of guesses and display it when the user win
'''
import random
import Lab4.check_input as check_input
def main():
    numGuesses = 1
    number = random.randint(1, 100)
    print("-Guessing Number-")
    userinput = check_input.get_int_range("I'm thinking of a number. Make guess(1-100): ", 1, 100)
    	
    while(True):
        if (userinput > number):
            print("Too High!" + "")
            userinput = check_input.get_int_range("Guess again(1-100): ", 1, 100)
            numGuesses += 1
            continue
        elif(userinput < number):
            print("Too Low!" + '')
            userinput = check_input.get_int_range("Guess again(1-100): ", 1, 100)
            numGuesses += 1
            continue
        else:
            print(f"Correct, you got it in {numGuesses} tries")
            break
main()	