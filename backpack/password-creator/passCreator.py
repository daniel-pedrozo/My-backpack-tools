import random
import string
import argparse
from colorama import Fore, Style, init


init(autoreset=True)

def generate_password(length=12, use_symbols=False, use_numbers=False, use_uppercase=False, use_word=False, use_recommend=False):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if use_recommend:
        length = 22
        characters += string.punctuation
        characters += string.digits
        characters += string.ascii_uppercase

    #Generate the initial random password 
    password = ''.join(random.choice(characters) for _ in range(length))

    if use_word:
        custom_word = input("Enter the word to include in the password: ")
        password += custom_word

    # Shuffle the password to ensure randomness with the new word
    #password = ''.join(random.sample(password, len(password)))

    return password

def main():
    parser = argparse.ArgumentParser(description="Custom strong passwords creator.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Adjust the length for password")
    parser.add_argument("-s", "--symbols", action="store_true", help="Use symbols")
    parser.add_argument("-n", "--numbers", action="store_true", help="Use numbers")
    parser.add_argument("-u", "--uppercase", action="store_true", help="Use uppercase letters")
    parser.add_argument("-w", "--word", action="store_true", help="Add your word on the password")
    parser.add_argument("-r", "--recommend", action="store_true", help="Make the password on ours ecommendations")
    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        use_symbols=args.symbols,
        use_numbers=args.numbers,
        use_uppercase=args.uppercase,
        use_word=args.word,
        use_recommend=args.recommend
    )

    print(f"{Fore.RED}New password: {Fore.GREEN}{Style.BRIGHT}{password}")

if __name__ == "__main__":
    main()