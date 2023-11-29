# make a welcome text
# enter character name and display to welcome
# define a function for day 1 to 5
# declare variables for health, hatred, black coffee = 5, coffee with milk = 5
# if sadness > happiness, character suicide
# if day 5 achieve with greater than 5 health, display nothing
# THIS WAS CREATED ON NOV 26

import time
import sys
import random

black_coffee = 5
coffee_with_milk = 5
happiness = 10
sadness = 0
day = 1

menu = ["Cappuccino",
        "Latte",
        "Frappuccino"]


def character_info():

    display_text_obo(f"Information: \n "

                     f"1. Health = {happiness}\n"
                     f" 2. Sadness = {sadness}\n"
                     f"\n Press r to return")

    press5 = input(": ")

    if press5 == "r":
        return welcome()
    else:
        display_text_obo(f"\nInvalid input\n")
        return character_info()


def display_text_obo(text, delay=0.01):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def loading():
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print("..", end="")
    time.sleep(1)
    return "..."


def increment_absent():
    global day
    day += 1
    print(loading())
    return day_start()


def arrived_on_shop():
    global day
    print(loading())
    display_text_obo(f"\nDay {day}")
    display_text_obo("Arrived on shop\n")
    return at_work()


def home():
    global happiness
    global sadness
    global day
    day += 1
    display_text_obo(f"STATUS\n"
                     f"Happiness points: {happiness}\n"
                     f"Sadness points: {sadness}")
    while day < 7:
        display_text_obo("Thank you for playing!")

        if sadness > happiness:
            print("Your character has committed suicide. Thank you for playing.")
            sys.exit()
        else:
            return day_start()


def close_open():
    display_text_obo("\nCHOICE\n"
                     "1. Remain Open\n"
                     "2. Close shop")
    shop_choice = input(": ")

    if shop_choice == "1":
        return at_work()
    elif shop_choice == "2":
        display_text_obo("Going home..")
        return home()
    else:
        print("Invalid input")
        return close_open()


def at_work():
    global happiness
    global sadness

    customer_count = 0

    while True:
        print("Waiting for customer")
        random_customer = random.randint(2, 7)
        time.sleep(random_customer)
        print("Customer Arrives")

        random_order = random.choice(menu)
        display_text_obo(f"Customer wants: {random_order}")
        customer_count += 1

        if customer_count == 5:
            print("Stop")
            break

        display_text_obo(f"\nORDER\n"
                         f"1. Process order\n"
                         f"2. Dont process order")

        user_choice = input(": ")

        if user_choice == "1":
            display_text_obo("Order is processing..")
            print(loading())
            print("Order processed")
            happiness += 1
            display_text_obo(f"Plus 1 to your happiness points\n"
                             f"Happiness points: {happiness}\n"
                             f"Sadness points: {sadness}")
            return close_open()
        elif user_choice == "2":
            sadness += 2
            happiness -= 2
            display_text_obo(f"Plus 1 to your happiness points\n"
                             f"Happiness points: {happiness}\n"
                             f"Sadness points: {sadness}")
            return close_open()
        else:
            print("Invalid input: ")
            return at_work()


def day_start():
    global day
    display_text_obo(f"Day {day}")
    display_text_obo("Are you going to work today? \n"
                     "1. Go to work\n"
                     "2. Leave\n")

    go_to_work = input(": ")

    while True:

        if go_to_work == "1":
            print("Going to work...")
            return arrived_on_shop()

        elif go_to_work == "2":
            display_text_obo(f"You are absent Today")
            return increment_absent()

        else:
            print("Invalid input")
            return day_start()


def welcome():

    display_text_obo(f"CHOICES\n"
                     f"Click 1. To display your information\n"
                     f"Click 2. To start game\n"
                     f"Click 3. To quit job")
    option = input(": ")

    if option == "1":
        return character_info()
    elif option == "2":
        print(loading())
        return day_start()
    elif option == "3":
        display_text_obo(f"Thank you for playing, {character_name}")
        sys.exit()
    else:
        print("Invalid input")
        return welcome()


if __name__ == "__main__":

    display_text_obo(f"NOTICE: On this game, you are currently working on your own Coffee shop\n"
                     f"Your goal is to remain your Happiness points higher than Sadness points. Good luck!\n")
    character_name = input("Please input your name: ")
    display_text_obo(f"\nWelcome, {character_name}. Today is your first day on this world. To begin with,\n")
    welcome()
