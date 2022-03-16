import random


def guess_number():
    print("===========\nGuess number\n===========")
    number = random.randint(1, 9)
    
    while True:
        raw_guess = input("What is the correct number: ")
        guess = int(raw_guess)

        if guess == number:
            print("You get correct answare!!")
            break
        if guess > number:
            print("Lower..")
        if guess < number:
            print("Higher")

def main():
    guess_number()

if __name__ == "__main__":
    main()