# 📋 Clipboard Typing Script

This project provides a Python script that simulates typing text from the clipboard into any active application window.  
It is useful for situations where **pasting is not supported** (e.g., password fields, RDP sessions, restricted apps, terminals, or game chat windows).

---

## 🚀 Features
- ✅ Reads text directly from the system clipboard (`Ctrl+C` first, then trigger).
- ✅ Simulates human typing (configurable typing delay).
- ✅ Works even in applications where **Ctrl+V paste is disabled**.
- ✅ Hotkey trigger: **Ctrl + Shift + T**.
- ✅ Press **Esc** to exit the script.
- ✅ Lightweight and runs on Windows with minimal setup.

---

## 🖥️ Requirements
- **OS**: Windows 10 / 11  
- **Python**: 3.7 or newer  

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/XploitXpert/Enable-Paste.git
   cd Enable-Paste
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### requirements.txt
```
keyboard
pyperclip
pywin32
```

⚠️ **Important:** Run the script with **Administrator privileges** if you want it to work inside apps launched as admin.

---

## ▶️ Usage

1. Copy some text to the clipboard (`Ctrl+C`).
2. Place your cursor inside a text field.
3. Press **Ctrl + Shift + T**.
4. The script will "type out" the clipboard content character by character.
5. Press **Esc** to stop the script.

Example run:
```bash
python Paste.py
```

Console output:
```
Press 'ctrl+shift' to type the clipboard contents. Press 'esc' to exit.
Debug: Active window class='Notepad', title='Untitled - Notepad'
Typing started...
Typing finished.
```

---

## 🎥 Demo

![Demo of Clipboard Typing Script](path/to/demo.gif)
*Note: Replace `path/to/demo.gif` with the actual path to your demo GIF after uploading it to your GitHub repository.*

---

## ⚙️ Configuration

Inside `clipboard_typing.py`, you can adjust the typing speed:
```python
TYPE_DELAY = 0.07   # delay between characters (seconds)
```

* Increase if characters are skipped.
* Decrease for faster typing.
* Add randomness if you want more "human-like" typing.

---

## 📂 Project Structure

```
Enable-Paste/
│
├── Paste.py     # Main script
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

---

## 🔒 Limitations

* Works only on **Windows** (uses Win32 APIs).
* Requires **Administrator privileges** for typing into elevated apps.
* Some modern UWP apps may block simulated keystrokes.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch (`feature/your-feature`)
3. Commit your changes
4. Push and open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use, modify, and distribute.

---

## 🙌 Acknowledgments

* [`keyboard`](https://pypi.org/project/keyboard/) – for global hotkeys and key simulation.
* [`pyperclip`](https://pypi.org/project/pyperclip/) – for clipboard access.
* [`pywin32`](https://pypi.org/project/pywin32/) – for interacting with Windows APIs.
