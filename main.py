import random
import string

# get the list of all alphabet in both lower and upercase
letters = string.ascii_letters

# All supported symbols
symbols = "!#$%&()*+"

# All number from 0-9
numbers = string.digits

# welcome the user
print("Welcome to the PyPassword Generator!")

while True:
    try:
        value = int(
            input(
                f"\nKindly indicate how long you would want the password to be: "
            ).strip()
        )
        if value < 1:
            raise ValueError
        break
    except ValueError:
        print(
            f"Invalid input. Please provide a positive integer to indicate the length of the password."
        )

letter_count = round(value * 0.6)
number_count = round(value * 0.2)
symbol_count = value - (letter_count + number_count)

# generate the amount of alphabet, num and symbols from the letters, numbers and symbols list
password_list = (
    random.choices(letters, k=letter_count)
    + random.choices(numbers, k=number_count)
    + random.choices(symbols, k=symbol_count)
)
random.shuffle(password_list)

# concatenate the string that has been generated and output the result
password = "".join(password_list)

print(f"Your newly generated password is: {password}")
