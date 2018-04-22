import random


def take_input(guess_list):
    user_guess = ''
    while user_guess == '':
        user_guess = input("Enter a guess between 1-100: ")
        user_guess = int(user_guess)

        if user_guess in guess_list:
            print("You already guessed that, try again: ")
            user_guess = ''
            continue

        if user_guess < 1 or user_guess > 100:
            print("Number was not in the allowed range of 1 - 100. Try again: ")
            user_guess = ''
            continue
        else:
            guess_list.append(user_guess)
            return user_guess


def check_input(guess, num):
    if guess > num:
        print("Guess lower \n")
        return False
    elif guess < num:
        print("Guess higher \n")
        return False
    else:
        print("you got it!")
        return True


def main():
    rand_number = random.randint(1, 100)
    flag = False
    guesses = []

    while not flag:
        user_input = take_input(guesses)
        flag = check_input(user_input, rand_number)


main()
