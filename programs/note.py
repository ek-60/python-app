import time
time = time.strftime("%X %x")


def notepad():
    print("===========\nNOTEPAD\n===========")

    while True:
        print("(1) Read notepad\n(2) Add notes\n(3) Delete notes\n(4) Stop")

        sel = input("Choose program: ")
        f = open("muistio.txt", "a")
        f.close()

        if sel == "1":
            f = open("muistio.txt", "r")
            print(f.read())
            f.close()
        if sel == "2":
            f = open("muistio.txt", "a")
            f.write(input("Add new note: ") + "-" + time + "\n" )
            f.close()
        if sel == "3":
            f = open("muistio.txt", "w")
            print("Notes deleted!")
            f.close()
        if sel == "4":
            break

def main():
    notepad()

if __name__ == "__main__":
    main()