import json


def currency_type():
    print('''Which type of currency would you like to convert?
- CAD
- USD
- EUR
- JPY
- HKD

Please type in the currency:''')
    currencies = ["cad", "usd", "eur", "jpy", "hkd"]
    loop = True
    while loop:
        currency_input = input(">").lower()
        if currency_input in currencies:
            print("-" * 15)
            break
        else:
            print("Invalid input")
    return currency_input


def mode_type(currency):
    print("What would you like to do with " + currency.upper() + "?")
    print("1. Convert " + currency.upper() + " into another currency")
    print("2. Convert another currency into " + currency.upper())
    print("\nEnter in the mode type, 1 or 2, below:")
    loop = True
    while loop:
        mode_input = input(">")
        if mode_input == "1":
            print("-" * 15)
            money_conversion(currency)
            loop = False
        elif mode_input == "2":
            print("-" * 15)
            to_money_conversion(currency)
            loop = False
        else:
            print("Invalid input")


def money_conversion(currency):
    loop = True
    while loop:
        print("Type in the code of the currency (ex. USD) you would like " + currency.upper() + " to be converted into:")
        currency_type = input(">").lower()
        try:
            with open(currency + '.json') as f:
                data = json.load(f)
            exchange_rate = float(data[currency_type]['rate'])
            while loop:
                try:
                    print("Type in how much in " + currency.upper() + " do you want to be converted into " + currency_type.upper() + ":")
                    money_amount = float(input(">"))
                    conversion = money_amount * exchange_rate
                    print("-" * 15)
                    print("$" + str(money_amount) + " in " + currency.upper() + " is $" + "\033[1m" + str(round(conversion, 2)) + "\033[0m" +
                          " in " + currency_type.upper())
                    break
                except ValueError:
                    print("You entered in a letter/character. Please only enter numbers.")
            loop = False
        except KeyError:
            print("Invalid currency")


def to_money_conversion(currency):
    loop = True
    while loop:
        print("Type in the currency code (ex. USD) of the currency you want to convert to " + currency.upper() + " below:")
        currency_type = input(">").lower()
        try:
            with open(currency + '.json') as f:
                data = json.load(f)
            exchange_rate = float(data[currency_type]['inverseRate'])
            loop = True
            while loop:
                try:
                    print("Type in how much in " + currency_type.upper() + " you want to be converted into " + currency.upper() + ":")
                    currency_money = float(input(">"))
                    conversion = currency_money * exchange_rate
                    print("-" * 15)
                    print("$" + str(currency_money) + " in " + currency_type.upper() +
                          " is $" + "\033[1m" + str(round(conversion, 2)) + "\033[0m" + " in " + currency.upper())
                    break
                except ValueError:
                    print("You entered in a character/letter. Please only input numbers")
            loop = False
        except KeyError:
            print("Invalid currency")


def output(country):
    loop = True
    while loop:
        if country == "":
            currency = currency_type()
        else:
            currency = country
        mode_type(currency)
        loop = False

