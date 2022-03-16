

def supermarket():
    print("===========\nSupermarket\n===========")
    lst = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
    cost = 0
    products = ["eggs", "bacon", "pasta", "banana", "bread", "cheese", "butter", "chicken", "pesto", "vegetables"]
    print(*products, sep = ", ")

    while True:
        val = input("Write prodcut you wan to buy! 0 stops programg: ")

        if val == "0":
            print("Total: ", cost)
            raw_cash = input("Give money: ")
            cash = int(raw_cash)
            if cash > cost:
                print("You will get back: ", cash - cost)
                break
            if cash < cost:
                print("You will need more", cost - cash, "money!")
                raw_new_cash = input("Give more money: ")
                new_cash = int(raw_new_cash) + cash
                print(new_cash)
                if new_cash > cost:
                    print("You will get back: ", new_cash - cost)
                    break
                if new_cash < cost:
                    print("You will need more", cost - new_cash, "money!")
                    ask = input("Do you have that much money anymore? Y or N: ")
                    if ask == "Y":
                        raw_two_cash = input("Give me more money!: ")
                        two_cash = int(raw_two_cash) + new_cash
                        if two_cash > cost:
                            print("You will get back: ", two_cash - cost)
                            break
                        if two_cash < cost:
                            print("ARE YOU SERIOUSLY??\n THIS WAS NOW HERE..")
                            break
                    if ask == "N":
                        print("Your borke go to work..")
                        break
         
        if val == "eggs":
            print("Product: ", products[0], "Cost: ", lst[0])
            cost += lst[0]
        if val == "bacon":
            print("Product: ", products[1], "Cost: ", lst[1])
            cost += lst[1]
        if val == "pasta":
            print("Product: ", products[2], "Cost: ", lst[2])
            cost += lst[2]
        if val == "banana":
            print("Product: ", products[3], "Cost: ", lst[3])
            cost += lst[3]
        if val == "bread":
            print("Product: ", products[4], "Cost: ", lst[4])
            cost += lst[4]
        if val == "cheese":
            print("Product: ", products[5], "Cost: ", lst[5])
            cost += lst[5]
        if val == "butter":
            print("Product: ", products[6], "Cost: ", lst[6])
            cost += lst[6]
        if val == "chicken":
            print("Product: ", products[7], "Cost: ", lst[7])
            cost += lst[7]
        if val == "pesto":
            print("Product: ", products[8], "Cost: ", lst[8])
            cost += lst[8]
        if val == "vegetables":
            print("Product: ", products[9], "Cost: ", lst[9])
            cost += lst[9]

def main():
    supermarket()

if __name__ == "__main__":
    main()