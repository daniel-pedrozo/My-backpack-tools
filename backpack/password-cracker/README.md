![Sample_Text](https://github.com/user-attachments/assets/f9f869d6-d995-48b9-bc2f-1bf59af9f435)


# Password Cracker

A Python-based tool to perform brute-force and dictionary attacks on hashed passwords. With support for multiple hashing algorithms, this tool is built to test password strength and showcase cybersecurity concepts.

## 🎯 Objective

The main goal of this project is to demonstrate password-cracking techniques, using brute-force and wordlist-based approaches, optimized with multithreading for faster execution.

## 💡 Features

- Brute-force attack with adjustable character set and password length.
- Dictionary attack using a custom wordlist.
- Supports various hash algorithms (e.g., MD5, SHA256) using Python’s `hashlib`.
- Optional detailed output to track each password attempt.
- Shows all available hash algorithms in `hashlib`.
- Multithreaded to improve brute-force speed.

## 📚 Libraries Used

- `hashlib`: For hashing passwords and verifying hash matches.
- `itertools`: For generating password combinations during brute-force attacks.
- `string`: To generate character sets for brute-forcing.
- `argparse`: For handling command-line arguments.
- `time`: To track the time taken for cracking.
- `concurrent.futures`: To implement multithreading and speed up the brute-force process.

## ⚙️ Installation

1. **Clone the Repository:**
   
   `git clone https://github.com/daniel-pedrozo/My-backpack-tools.git`
   
3. **Enter the folder:**
   
   `cd My-backpack-tools/backpack/password-creator`
  
4. **install requirements:**

   `pip install -r requirements.txt`


 ### 🌱 Usage:
- Brute force attacak:

`python3 password_cracker.py <password_to_crack> --max_length 4 --hash_type md5 -o`

- Dictionary Attack:

 `python3 password_cracker.py <password_to_crack> --wordlist /path/to/wordlist.txt --hash_type sha256 -o`

- List Available Hash Algorithms:

`python3 password_cracker.py --hashs_available`

We only tested on **linux** so far, but it can run on windows too.


### 💪 Skills Learned

- Understanding and implementing brute-force and dictionary attacks.
- Working with hashlib for various hashing algorithms.
- Optimizing code with multithreading using concurrent.futures.
- Command-line interface design with argparse.


### 🗃️ Contributing:

Feel free to contribute to this project by:

  - Reporting Issues: If you encounter any bugs or have suggestions, please open an issue.
  - Submitting Pull Requests: Fork the repository, make your changes, and submit a pull request.

**Let me know if you have any other questions or require further assistance.**
