import argparse
import re


"""
!!the code is on development!!

To be add:
    Diferent ways to verify your password stength like: other librarys, some kind of API to verify password leacks and test for wordlist.
    More customization for the use on passing arguments.
    Test hash stength.
    Add some ascii art.
    
"""

def password_strength_check(password):
    """Checks password strength based on multiple criteria.

    Args:
        password (str): The password to check.

    Returns:
        str: A message indicating the password strength.
    """

    # Check password length
    if len(password) < 8:
        return "Password too short. Minimum 8 characters required."

    # Check for character variety
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()" for c in password)

    if not (has_upper and has_lower and has_digit and has_special):
        return "Password lacks character variety. Include uppercase, lowercase, numbers, and special characters."

    # Check for common patterns (basic implementation)
    if re.search(r"^(?i)(password|123456|qwerty|asdfg|zxcvbn)$", password):
        return "Password is too common. Avoid using simple patterns."

    return "Password strength is good."

def main():
    parser = argparse.ArgumentParser(description="Password strength test.")
    parser.add_argument("password", help="The password to test the strength")

    args = parser.parse_args()

    result = password_strength_check(args.password)
    print(result)

if __name__ == "__main__":
    main()