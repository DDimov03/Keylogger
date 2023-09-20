# Keylogger with Tkinter GUI

This Python script demonstrates a simple keylogger with a Tkinter GUI for setting the log file path. It records keystrokes and saves them to a log file. The log file's name is generated based on the current date and time.

## Features

- Records keystrokes and saves them to a log file.
- Allows you to specify the log file path using a Tkinter GUI.
- Excludes certain keys from recording (e.g., Shift, Backspace, Caps Lock, etc.).
- Limits the number of characters per line in the log file.

## Requirements

To run this script, you need the following libraries installed:

- `tkinter`: For the GUI.
- `pynput`: For monitoring and recording keyboard input.

You can install `pynput` using pip:

```bash
pip install pynput
```

## Usage
Clone this repository to your local machine.
#
```
git clone https://github.com/DDimov03/Keylogger
```
#
Navigate to the project directory.
```
cd your-repo
```
#

Run the script.
```
python keylogger.py
```
#
A GUI window will open. Click the "Browse and Start Logging" button to specify the log file path. The keylogger will start recording after you select a file path.
Press Ctrl+C or close the terminal to stop the keylogger.


## Customization
You can customize the keylogger by modifying the keylogger.py script:

Change the max_characters_per_line variable to adjust the maximum number of characters per line in the log file.
Modify the excluded_keys list to exclude specific keys from recording.

## Note
This script is for educational purposes only. Be responsible and use it only for legal and ethical purposes.
Respect privacy and obtain proper consent before recording keystrokes on someone else's computer.
