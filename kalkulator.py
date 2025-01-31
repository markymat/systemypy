#!/usr/bin/env python3

def kalkulator():
    print("Prosty Kalkulator")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    wybor = input("Wybierz operację (1/2/3/4): ")

    if wybor in ('1', '2', '3', '4'):
        liczba1 = float(input("Podaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))

        if wybor == '1':
            print(f"{liczba1} + {liczba2} = {liczba1 + liczba2}")
        elif wybor == '2':
            print(f"{liczba1} - {liczba2} = {liczba1 - liczba2}")
        elif wybor == '3':
            print(f"{liczba1} * {liczba2} = {liczba1 * liczba2}")
        elif wybor == '4':
            if liczba2 != 0:
                print(f"{liczba1} / {liczba2} = {liczba1 / liczba2}")
            else:
                print("Dzielenie przez zero!")
    else:
        print("Nieprawidłowy wybór operacji")

kalkulator()
