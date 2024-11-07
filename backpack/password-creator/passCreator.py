import random
import string
import argparse
import nltk
import pyfiglet
import shutil
from nltk.corpus import words
from colorama import Fore, Style, init


init(autoreset=True)


def generate_password(length=12, use_symbols=False, use_numbers=False, use_uppercase=False, use_word=False, use_recommend=False, use_phrases=False):

    if use_phrases:
        password = generate_phrase()
        return password  # Pass the rest of the modifications
        
    # Initialize characters with lowercase letters
    characters = string.ascii_lowercase

    # Modify characters based on options
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

def generate_phrase():
    print(f"{Fore.RED}Downloading word list for better experience!")
    nltk.download('words')

    try:
        num_words = int(input("Enter the number of words to include in the password: "))
    except ValueError:
        print(f"{Fore.RED}Only numbers are expected! \nTry again..")
        exit()  # Stop the program if input is not a number

    

    #word_list = words.words()
    word_list = [word for word in words.words() if len(word) <= 7 and word.isalpha()]
    phrase = ' '.join(random.choices(word_list, k=num_words))
    return phrase

def ascii_art():
    # Nice fonts: smbraille, pagga
    ascii_art1 = pyfiglet.figlet_format("-Pass.Creator-", font="smbraille")
    ascii_art2 = pyfiglet.figlet_format("For help use -h or -help", font="term")

    # Get the terminal width
    terminal_width = shutil.get_terminal_size().columns

    # Center each line of the ASCII art
    centered_ascii_art1 = "\n".join(line.center(terminal_width) for line in ascii_art1.splitlines())
    centered_ascii_art2 = "\n".join(line.center(terminal_width) for line in ascii_art2.splitlines())

    print("\n")
    # Print the centered ASCII art in green
    print(f"{Fore.GREEN}{centered_ascii_art1}")
    print(f"{Fore.GREEN}{centered_ascii_art2}")
    print("\n")

    # To know others fonts run this comand
    #print(pyfiglet.FigletFont.getFonts())

def main():

    ascii_art()

    parser = argparse.ArgumentParser(description="Custom strong passwords creator.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Adjust the length for password")
    parser.add_argument("-s", "--symbols", action="store_true", help="Use symbols")
    parser.add_argument("-n", "--numbers", action="store_true", help="Use numbers")
    parser.add_argument("-u", "--uppercase", action="store_true", help="Use uppercase letters")
    parser.add_argument("-w", "--word", action="store_true", help="Add your word on the password")
    parser.add_argument("-r", "--recommend", action="store_true", help="Make the password on ours recommendations")
    parser.add_argument("-p", "--phrases", action="store_true", help="Make a safe phrase for passwords")
    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        use_symbols=args.symbols,
        use_numbers=args.numbers,
        use_uppercase=args.uppercase,
        use_word=args.word,
        use_recommend=args.recommend,
        use_phrases=args.phrases
    )
    
    print(f"{Fore.GREEN}New password: {Fore.RED}{Style.BRIGHT}{password}")

if __name__ == "__main__":
    main()
