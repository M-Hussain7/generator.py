import re
import string
import random

# Optimized character set for Steam (Excludes I, O, S, Z to prevent confusion)
VALID_CHARS = "".join([c for c in string.ascii_uppercase if c not in 'IOSZ']) + string.digits

def process_code(user_input):
    # Detect non-ASCII characters (emojis / special symbols)
    emoji_pattern = re.compile(r'[^\x00-\x7F]+')
    match = emoji_pattern.search(user_input)
    
    if not match:
        print("\n❌ Error: No emoji or missing character placeholder found in that code. Please try again.\n")
        return

    placeholder = match.group()
    # Generate codes using only valid Steam characters
    generated_codes = [user_input.replace(placeholder, char) for char in VALID_CHARS]
    
    # Randomly shuffle the codes without duplication for this session
    randomized_codes = random.sample(generated_codes, len(generated_codes))

    print(f"\n✅ Generated {len(randomized_codes)} randomized combinations for: {user_input} (Steam Rules Applied)\n")
    print("=" * 45)
    for code in randomized_codes:
        print(code)
    print("=" * 45)

    # Save the randomized output to a text file
    filename = "generated_codes.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for code in randomized_codes:
            f.write(code + "\n")
    print(f"Saved all randomized codes to '{filename}'\n")

def main():
    print("--- Interactive Steam Code Generator (Randomized) ---")
    print("Paste your code with an emoji placeholder and press Enter.")
    print("Type 'exit' or 'q' to quit the script.\n")

    while True:
        user_input = input("Enter code: ").strip()
        
        if user_input.lower() in ['exit', 'q']:
            print("Exiting generator. Good luck in the race!")
            break
            
        if not user_input:
            continue

        process_code(user_input)

if __name__ == "__main__":
    main()