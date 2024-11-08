# Password creator

**A versatile Python script to create strong, customizable passwords.**

## Objective

This tool empowers you to create strong, personalized passwords. Easily adjust the password length and complexity by selecting the desired mix of symbols, numbers, uppercase letters, and custom words. For added security, you can even generate random password phrases.

### Features:

* **Customizable Length:** Set the desired password length.
* **Character Set Selection:** Choose from uppercase, lowercase, numbers, and symbols.
* **Word Inclusion:** Incorporate a custom word into the password.
* **Random Phrase Generation:** Create secure password phrases from a word list.
* **Recommended Settings:** Generate highly secure passwords based on recommended practices.
* **User-Friendly Interface:** Easy-to-use command-line interface.


### Librarys Used

- random
- string
- argparse
- nltk
- pyfiglet
- shutil
- colorama

### Installation:

1. **Clone the Repository:**
   
   `git clone https://github.com/daniel-pedrozo/My-backpack-tools.git`
   
3. **Enter the folder:**
   
   `cd My-backpack-tools/backpack/password-creator`
  
4. **install requirements:**

   `pip install -r requirements.txt`


### Usage:

`python3 passCreator.py -h`

We only tested on **linux** so far, but it can run on windows too.


### Skills Learned

#### Librarys

- **random:** Effectively utilized the `random` library to generate random characters for password creation.
- **string:** Demonstrated understanding of the `string` module by leveraging its built-in constants for different character sets (lowercase, uppercase, symbols, digits)
- **argparse:** Code showcases ability to implement command-line arguments using the `argparse` library, allowing users to customize password generation.
- **nltk:** Including `nltk` demonstrates my exploration of Natural Language Toolkit for text-based project.
- **colorama:** Using `colorama` knowledge of adding color and styling to text output, enhancing user experience.
- **pyfiglet:** Including pyfiglet showcases ability to integrate libraries for creating ASCII art, adding a creative touch to the project.

#### Functionality and Algorithms

- **Password Generation:** Your code demonstrates your understanding of creating random passwords with varying complexity based on user input.
- **Customizable Password Options:** You implemented functionalities for users to choose password length, character sets (uppercase, lowercase, symbols, numbers), and word inclusion.
- **Optional Password Phrases:** If you keep the phrase generation, you implemented basic text processing using `nltk` to filter words for appropriate password phrases.

#### User Interaction

- Command-line arguments: Using `argparse` allows users to configure password generation through command-line options, showcasing your understanding of user input handling.


### Contributing:

Feel free to contribute to this project by:

  - Reporting Issues: If you encounter any bugs or have suggestions, please open an issue.
  - Submitting Pull Requests: Fork the repository, make your changes, and submit a pull request.

**Let me know if you have any other questions or require further assistance.**
