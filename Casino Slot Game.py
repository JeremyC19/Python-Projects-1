MAX_LINES = 3


def deposit():
    while True:  # continue the loop until it breaks out
        amount = input("What would you like to deposit? $")
        if amount.isdigit():  # ensure that the amount is a valid number
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")  # incase the amount isn't a valid number

    return amount


def get_number_of_lines():
    while True:  # continue the loop until it breaks out
        lines = input("How many lines would you like to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():  # ensure that the amount is a valid number
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")  # incase the amount isn't a valid number

    return lines


def main():  # allows the game to be played again by calling this function
    balance = deposit()



main()
