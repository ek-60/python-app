

def calculator():
    print("===========\nCALCULATOR\n===========")
    raw_num = input("Give a number: ")
    raw_num_two = input("Give a number: ")

    num = int(raw_num)
    num_two = int(raw_num_two)

    while True:
        print("(1) +\n(2) -\n(3) *\n(4) /\n(5) Change numbers\n(6) Stop")
        print("Numbers", num, num_two)

        val = input("Choose program: ")

        if val == "1":
            print("Total is: ", num + num_two)
        if val == "2":
            print("Total is: ", num - num_two)
        if val == "3":
            print("Total is: ", num * num_two)
        if val == "4":
            print("Total is: ", num / num_two)
        if val == "5":
            raw_new_num = input("Change number: ")
            raw_new_num_two = input("Change number: ")
            new_num = int(raw_new_num)
            new_num_two = int(raw_new_num_two)
            num = new_num
            num_two = new_num_two
        if val == "6":
            print("You stopped the program!")
            break

def main():
    calculator()

if __name__ == "__main__":
    main()