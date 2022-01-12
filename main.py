import exchangerates
import countrycurrency


def main_console():
    loop = True
    while loop:
        print('''Welcome to MoneyConverter! This program helps you convert one currency into another!
Currently, we are only accepting some conversions, but others will come later!
We can also tell you what kind of currency is accepted in certain countries!

MONEY CONVERSIONS LAST UPDATED: June 28, 2021
''')
        print('''Which mode would you like to access?
1. Money Converter
2. Countries Currencies

Type in the mode number, 1 or 2, in the input below:''')
        mode_input = input(">")
        if mode_input == "1":
            print("-" * 15)
            exchangerates.output(country="")
            print("-" * 15)
            loop = exit_program()
        elif mode_input == "2":
            print("-" * 15)
            countrycurrency.output()
            print("-" * 15)
            loop = exit_program()
        else:
            print("Invalid input")
    print("You have successfully ended the program!")


def exit_program():
    exit_loop = True
    while exit_loop:
        exit_input = input("Do you wish to continue? (y/n): ").lower()
        if exit_input == "y":
            print("-" * 15)
            loop = True
            break
        elif exit_input == "n":
            loop = False
            break
        else:
            print("Invalid input")
    return loop


main_console()
