import random

score = 0
username = ""
health = 3


def login():
    global username
    username = input("USERNAME: ")
    age = int(input("AGE: "))
    if age < 18:
        print("You Are Too Young")
        quit()


def choice():
    in_1 = input("heads or tails: ")
    while in_1.lower() == "":
        print("Enter An Answer")
        in_1 = input("heads or tails: ")

    if in_1.lower() == "heads":
        print('you chose heads')

    elif in_1.lower() == "tails":
        print('you chose tails')
    else:
        print("Incorrect")
        in_1 = input("heads or tails: ")

    list_opt = ["heads", "tails"]
    chosen = random.choice(list_opt)
    print(f"the coin flip chose: {chosen}")
    calc(in_1, chosen)


def calc(in_1, chosen):
    global score
    global health
    if in_1 == chosen:
        print("You Won!")
        score += 1
    elif in_1 != chosen:
        print("You Lost")
        score += 0
        health -= 1
        print(f"Health: {health}")
    return score


def score_check():
    print(f"Goodbye {username}, You Won {score} Times")
    quit()


def main():
    answer = input("Press enter to play (q to quit).")
    if answer.lower() == "q":
        quit()
    login()
    while health > 0:
        choice()
    if health == 0:
        score_check()


main()


