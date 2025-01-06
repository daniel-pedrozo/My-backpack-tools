
![🕵️_♂️_Phishing_Simulation_Tool](https://github.com/user-attachments/assets/3148f514-6950-4e6e-8233-7d78ac731e59)
 

## 🎯 **Objective**  
This project demonstrates how phishing pages can be used to capture sensitive user information such as usernames and passwords. **This tool is designed for educational purposes only** to help understand and mitigate phishing attacks.  

## 💡 **Features**  
- **Simulated Phishing Page**: A Flask-based web page mimicking a login form to demonstrate credential harvesting.  
- **Data Capture**: Credentials are logged locally and sent to a mock server for storage.  
- **Separate Server Application**: A Flask server that receives credentials and logs them to a file.  
- **Network Deployment**: Can be hosted on a local network for simulation purposes.  

## 📚 **Libraries Used**  
- **Flask**: For creating the web applications (`phishingSite.py` and `server.py`).  
- **requests**: For sending captured credentials to the mock server.  

## ⚙️ **Installation**  
1. Clone this repository:  
   ```bash
   git clone https://github.com/daniel-pedrozo/My-backpack-tools.git
   cd My-backpack-tools/backpack/password-creator
   ```  

2. Install the required dependencies:  
   ```bash
   pip install flask requests
   ```  

3. Ensure both `phishingSite.py` and `server.py` are in the same directory.  

## 🌱 **Usage**  
### **Step 1: Run the Mock Server**  
Start the mock server to receive credentials:  
```bash
python server.py
```  
The server will run on `http://0.0.0.0:5001`.  

### **Step 2: Launch the Phishing Page**  
Run the phishing site:  
```bash
python phishingSite.py
```  
The phishing page will be hosted on `http://0.0.0.0:5000`.  

### **Step 3: Test the Simulation**  
1. Open the phishing page in a browser on the local network using the IP address of the host (e.g., `http://192.168.x.x:5000`).  
2. Enter dummy credentials in the form and submit.  
3. The credentials will be:  
   - Logged locally in `captured_credentials.txt` by `phishingSite.py`.  
   - Sent to the mock server (`server.py`) and logged in `received_credentials.txt`.  

### **Step 4: Review Logs**  
Check the `captured_credentials.txt` and `received_credentials.txt` files to view the simulated credential data.  

## 📸 **Screenshots and Output**  

### **Phishing Page**  
A screenshot of the simulated phishing page where users can input their credentials.  
![Screenshot from 2025-01-06 14-30-09](https://github.com/user-attachments/assets/f6749d20-8ea0-4895-ac1d-f6993e51b1c9)


### **Captured Credentials Log**  
Example of the `captured_credentials.txt` file logging user credentials locally.  
```plaintext
Username: example_user, Password: example_password
```

### **Terminal output**
#### Phishing Page Output:
![carbon](https://github.com/user-attachments/assets/bac8dc90-814c-45a7-accc-9641abe21892)

#### Server Output:
![carbon(1)](https://github.com/user-attachments/assets/c12bc3f4-e960-4d72-be2a-a2dbb2197428)


## 💪 **Skills Learned**  
- Building web applications using Flask.  
- Capturing and processing form data in Python.  
- Sending POST requests with the `requests` library.  
- Creating a networked application with multiple components.  

---

⚠️ **Disclaimer**  
This project is intended for **educational purposes only** to raise awareness about phishing attacks and how they work. Do not use this tool for malicious purposes, as it would violate ethical principles and may result in legal consequences. Always seek proper authorization when testing or simulating phishing attacks.  

--- 

Let me know if you'd like additional customizations!

### 🗃️ Contributing:

Feel free to contribute to this project by:

  - Reporting Issues: If you encounter any bugs or have suggestions, please open an issue.
  - Submitting Pull Requests: Fork the repository, make your changes, and submit a pull request.

**Let me know if you have any other questions or require further assistance.**
