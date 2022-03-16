# HAKEE TIEDOSTOT
# import calc
# import note
# import guess
# import market
# import gui
import programs.note
import programs.calc
import programs.market
import programs.guess


def select_work():
    while True:
        print("Mitä haluat tehdä??")
        print("1. Notepad\n2. Calculator\n3. Supermarket\n4. Guess The Number")
        val = input("Choose 1-4: ")

        if val == "1":
            programs.note.notepad()
        if val == "2":
            programs.calc.calculator()
        if val == "3":
            programs.market.supermarket()
        if val == "4":
            programs.guess.guess_number()


def main():
    select_work()


if __name__ == "__main__":
    main()