import re
import string
import keyboard
import pyperclip
import time

# Full alphanumeric character set (A-Z, 0-9)
CHARACTER_SET = string.ascii_uppercase + string.digits

def load_and_clean_codes(filename="generated_codes.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            codes = []
            for line in f:
                clean_line = line.strip()
                # Skip empty lines or header/separator lines
                if clean_line and not clean_line.startswith("="):
                    # Remove any leftover brackets from generated text
                    clean_line = clean_line.replace("[", "").replace("]", "")
                    codes.append(clean_line)
        return codes
    except FileNotFoundError:
        print(f"❌ Error: Could not find '{filename}'. Check the file name and path.")
        return []

def main():
    codes = load_and_clean_codes()
    if not codes:
        return

    total = len(codes)
    index = 0

    print(f"✅ Loaded {total} cleaned codes from file.")
    print("--------------------------------------------------")
    print("1. First code copied to clipboard.")
    print("2. Press Ctrl + V to paste into Steam.")
    print("3. Next code automatically copies after each paste!")
    print("4. Press 'Esc' to stop.")
    print("--------------------------------------------------\n")

    pyperclip.copy(codes[index])
    print(f"[{index + 1}/{total}] Ready: {codes[index]}")

    def on_paste():
        nonlocal index
        index += 1
        
        if index < total:
            time.sleep(0.1)
            pyperclip.copy(codes[index])
            print(f"[{index + 1}/{total}] Next ready: {codes[index]}")
        else:
            print("\n🎉 All codes completed!")
            keyboard.unhook_all()

    keyboard.add_hotkey('ctrl+v', on_paste)
    keyboard.wait('esc')
    print("Script stopped.")

if __name__ == "__main__":
    main()