import keyboard
import time
import win32gui
import pyperclip  # install with: pip install pyperclip

TYPE_DELAY = 0.05  # delay per character

def get_clipboard_text():
    """Read text from clipboard."""
    try:
        return pyperclip.paste()
    except Exception as e:
        print(f"Error reading clipboard: {e}")
        return None

def simulate_typing(text):
    """Simulate keyboard typing for the given text."""
    for char in text:
        keyboard.write(char)
        time.sleep(TYPE_DELAY)

def is_text_field_active():
    """Check if active window is likely a text field."""
    try:
        hwnd = win32gui.GetForegroundWindow()
        class_name = win32gui.GetClassName(hwnd)
        window_title = win32gui.GetWindowText(hwnd)
        print(f"Debug: Active window class='{class_name}', title='{window_title}'")

        text_field_classes = [
            'Edit', 'RichEdit', 'RichEdit20A', 'RichEdit20W',
            'Chrome_WidgetWin_1', 'MozillaWindowClass', 'WindowsForms10.EDIT',
            'Scintilla', 'TkChild', 'Notepad'
        ]
        return class_name in text_field_classes
    except Exception as e:
        print(f"Error checking active window: {e}")
        return False

def trigger_typing():
    """Fetch text from clipboard and type it."""
    text = get_clipboard_text()
    if text:
        if is_text_field_active():
            print("Typing started...")
            simulate_typing(text)
            print("Typing finished.")
        else:
            print("Unknown input field. Fallback mode.")
            simulate_typing(text)
    else:
        print("Clipboard is empty or not readable.")

def main():
    hotkey = "ctrl+shift"
    print(f"Press '{hotkey}' to type the clipboard contents. Press 'esc' to exit.")

    keyboard.add_hotkey(hotkey, trigger_typing)
    keyboard.wait("esc")
    print("Exiting program.")

if __name__ == "__main__":
    main()
