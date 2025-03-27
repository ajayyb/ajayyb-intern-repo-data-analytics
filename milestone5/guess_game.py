import random

def guess_checker(num, answer):
    return num == answer
    
def play_game():
    answer = random.randint(1,10)
    guess = None
    while guess_checker is not True:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess_checker(guess, answer):
            print("Congratulations! You guessed correctly. The number was ", answer, ".")
            break
        else:
            print("Incorrect, try again.")
1

if __name__ == '__main__':
    play_game()