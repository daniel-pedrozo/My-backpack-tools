import hashlib
import itertools
import string
import argparse
import time
from concurrent.futures import ThreadPoolExecutor

def hash_password(password, hash_type='md5'):
    """Hashes a password using the specified hash algorithm."""
    hash_func = getattr(hashlib, hash_type)()
    hash_func.update(password.encode())
    return hash_func.hexdigest()

def guess_password_worker(characters, hash_to_crack, hash_type, length, output):
    """Worker function for guessing passwords of a specific length."""
    for guess in itertools.product(characters, repeat=length):
        guess_password = ''.join(guess)
        if output:
            print(f"Trying: {guess_password}")
        hashed_guess = hash_password(guess_password, hash_type)
        if hashed_guess == hash_to_crack:
            return guess_password
    return None

def brute_force(hash_to_crack, hash_type='md5', max_length=4, output=False, hashs_available=False):
    """Attempts to brute-force the password that matches the hash."""
    characters = string.ascii_letters + string.digits  # Add more symbols if needed

    if hashs_available:
        hashs_uses()
    
    with ThreadPoolExecutor() as executor:
        for length in range(1, max_length + 1):
            future = executor.submit(guess_password_worker, characters, hash_to_crack, hash_type, length, output)
            result = future.result()
            if result:
                return result
    return None

def hashs_uses():
    print("Available hash algorithms in hashlib:")
    for hashs in hashlib.algorithms_available:
        print(hashs)

def crack_with_wordlist(wordlist_path, hash_to_crack, hash_type='md5', output=False):
    """Attempts to crack the password using a wordlist."""
    try:
        with open(wordlist_path, 'r') as wordlist:
            for word in wordlist:
                word = word.strip()
                if output:
                    print(f"Trying: {word}")
                hashed_word = hash_password(word, hash_type)
                if hashed_word == hash_to_crack:
                    return word
        print("Password not found in wordlist.")
    except FileNotFoundError:
        print(f"Wordlist file '{wordlist_path}' not found.")
    return None

def main():
    parser = argparse.ArgumentParser(description="Brute-force password cracker")
    parser.add_argument("password", help="The password to brute-force")
    parser.add_argument("--hash_type", default="md5", help="The hash type to use (e.g., md5, sha256)")
    parser.add_argument("--max_length", type=int, default=4, help="Maximum length of password to attempt")
    parser.add_argument("-o", "--output", action="store_true", help="Print the brute-force passwords -it's going to be slower-")
    parser.add_argument("-s", "--hashs_available", action="store_true", help="Print every type of hash that can be used for --hash_type")
    parser.add_argument("-w", "--wordlist", help="Path to a wordlist file for dictionary attack")

    args = parser.parse_args()

    # Hash the target password
    hashed_password = hash_password(args.password, args.hash_type)
    print(f"Hashed password (target): {hashed_password}")

    start_time = time.time()

    # Try cracking with wordlist if provided
    cracked_password = None
    if args.wordlist:
        print("Attempting to crack using wordlist...")
        cracked_password = crack_with_wordlist(args.wordlist, hashed_password, args.hash_type, args.output)

    # If no wordlist or password not found, attempt brute-force
    if not cracked_password:
        print("Attempting brute-force attack...")
        cracked_password = brute_force(hashed_password, args.hash_type, args.max_length, args.output, args.hashs_available)

    end_time = time.time()

    # Output results
    if cracked_password:
        print(f"Password found: {cracked_password}")
    else:
        print("Password not found.")
    print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
