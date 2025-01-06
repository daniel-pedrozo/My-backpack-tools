# 🔒 Password Strength Checker (In Development)  

## 🎯 **Objective**  
This project aims to create a robust password strength checker tool that evaluates the security of passwords based on various criteria. The tool will help users improve their password practices and identify weak or common passwords.  

## 💡 **Features (Planned)**  
- **Password Strength Evaluation**:  
  - Check for password length, character variety, and common patterns.  
- **Enhanced Verification**:  
  - Integrate APIs to check for password leaks.  
  - Test against wordlists to identify common or weak passwords.  
- **Hash Strength Testing**:  
  - Evaluate the strength of password hashes (planned for future implementation).  
- **Customizable Arguments**:  
  - Allow users to pass additional options via the command line for flexible usage.  
- **Ascii Art & Aesthetic Enhancements**:  
  - Add visually appealing ASCII art for better user interaction.  

## 📚 **Libraries Used**  
- **argparse**: For parsing command-line arguments.  
- **re**: For regex-based pattern matching in password validation.  

## ⚙️ **Installation**  
1. Clone this repository:  
   ```bash
   git clone https://github.com/daniel-pedrozo/My-backpack-tools.git
   cd password-strength
   ```  

2. Run the script directly:  
   ```bash
   python password_checker.py --help
   ```  

## 🌱 **Usage**  
### **Check Password Strength**  
Run the script with a password to evaluate its strength:  
```bash
python password_checker.py "YourPasswordHere"
```  

Example Output:  
```plaintext
Password too short. Minimum 8 characters required.
```

### **Planned Enhancements**  
- Use additional libraries and APIs for comprehensive checks.  
- Add options to specify custom rules for strength evaluation.  
- Implement hash strength testing and ASCII art visuals.

## 💪 **Skills Learned**  
- Writing modular and scalable Python scripts.  
- Using `argparse` for command-line argument handling.  
- Applying regular expressions for text pattern matching.  
- Designing for extensibility and future enhancements.  

---

⚠️ **Disclaimer**  
This tool is currently under development. It is not yet suitable for production use or comprehensive password analysis. Stay tuned for updates!  
