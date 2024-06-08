import random 

colors = ["G", "R", "B", "W"]

def generate_code():
    code = []
    for _ in range(3):
        color = random.choice(colors)
        code.append(color)
    
    return code


def guess_code():
    while True:
        guess = input("Guess: ").upper().split()
        if len(guess) != 3:
            print(f"You must guess 3 colors")
            continue

        for color in guess:
            if color not in colors:
                print(f"Invalid color.Please try again")
                break
        else:
            break

    return guess


def main():
    tries = 5
    com_guess = generate_code()
    user_guess = guess_code()
    if com_guess == user_guess:
        print(f"You have guessed correct in {tries} tries")
    else:
        tries -= 1
        print(f"You have guessed wrong.Please try again you left with {tries} tries")



main()













