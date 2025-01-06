# 🔑 Keylogger (In Development)  

## 🎯 **Objective**  
This project aims to create a keylogger for educational and ethical purposes, demonstrating how keystrokes can be captured programmatically. It also serves as a foundation for exploring advanced functionalities such as remote logging and integration with IoT devices.  

## 💡 **Features (Planned)**  
- **Keystroke Logging**:  
  - Captures and logs all keyboard input.  
- **Periodic Reporting**:  
  - Sends logged data at specified intervals.  
- **Future Enhancements**:  
  - Add support for sending logs via email or SMS.  
  - Explore Wi-Fi-based data transfer.  
  - Integrate with ESP8266 for IoT applications.  
  - Implement command-line arguments for more customization.  

## 📚 **Libraries Used**  
- **pynput**: For capturing keyboard input.  
- **threading**: To handle periodic reporting without blocking keystroke capture.  
- **os**: For interacting with the operating system (future enhancements).  

## ⚙️ **Installation**  
1. Clone this repository:  
   ```bash
   git clone https://github.com/daniel-pedrozo/My-backpack-tools.git
   cd My-backpack-tools/backpack/keylogger
   ```  

2. Install the required libraries:  
   ```bash
   pip install pynput
   ```  

3. Run the script directly:  
   ```bash
   python keylogger.py
   ```  

## 🌱 **Usage**  
### **Keylogger Execution**  
The keylogger starts automatically when you run the script. It logs keystrokes and reports them at a defined interval.  

- **Default Settings**:  
  - **Log Interval**: 10 seconds  
  - **Log File**: `keylog.txt`  

### **Stopping the Keylogger**  
To stop the keylogger, use the interrupt signal (Ctrl+C) in the terminal.  

### **Planned Enhancements**  
- Add email/SMS integration for remote log delivery.  
- Implement Wi-Fi-based data transfer for logs.  
- Connect to an ESP8266 device for IoT demonstrations.  
- Add argument parsing for configuring log intervals, output files, and other settings.  

## 💪 **Skills Learned**  
- Working with the `pynput` library for keylogging.  
- Implementing threading for periodic tasks.  
- Designing extensible Python applications.  

---

⚠️ **Disclaimer**  
This project is intended for **educational purposes only** to understand the concepts of keylogging and how such tools are created. Use responsibly and only with explicit consent. Unauthorized use of keyloggers is illegal and unethical.  
``` 

Let me know if you’d like adjustments or additional details!
