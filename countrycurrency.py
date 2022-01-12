import json
import exchangerates


def continent_identification():
    count = 0
    country_list = []
    wrong = True
    while wrong:
        print('''Type in which continent your country is located below:''')
        continent_input = input(">").title()
        with open('countries.json') as f:
            data = json.load(f)
        for country in data['countries']['country']:
            if country['continentName'] == continent_input:
                wrong = False
                if count == 0:
                    print("-" * 15)
                print(country['countryName'], end=" | ")
                country_list.append(country['countryName'].lower())
                count += 1
                if count % 10 == 0:
                    print("")
        if wrong:
            print("Invalid input")
            print("-" * 15)
    return country_list


def country_identification(country_list):
    loop = True
    currencies = ["cad", "usd", "eur", "jpy", "hkd"]
    while loop:
        print("Type in which country from that list you want to know the currency of:")
        country_input = input(">").lower()
        if country_input in country_list:
            loop = False
            with open('countries.json') as f:
                data = json.load(f)
            for country in data['countries']['country']:
                if country['countryName'] == country_input.title():
                    print("Currency of " + country_input.title() + ": " + country['currencyCode'])
                    if country['currencyCode'].lower() in currencies:
                        loop = True
                        while loop:
                            print("-" * 15)
                            print("This is type of conversion is part of our database! Would you like to access it? (y/n)")
                            money_conversion = input(">").lower()
                            if money_conversion == "y":
                                print("-" * 15)
                                exchangerates.output(country=country['currencyCode'])
                                loop = False
                            elif money_conversion == "n":
                                loop = False
                            else:
                                print("Invalid input")
        else:
            print("not valid")


def output():
    loop = True
    while loop:
        country_list = continent_identification()
        print("\n" + "-" * 15)
        country_identification(country_list)
        loop = False