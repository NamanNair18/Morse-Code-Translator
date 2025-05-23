MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
    '0': '-----', ' ': ' '
}

REVERSE_MORSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    # Convert text to Morse code.
    text = text.upper()
    morse_code = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            return f"Error: Character '{char}' not supported in Morse code."
    return ' '.join(morse_code)

def morse_to_text(morse):
    # Convert Morse code to text
    morse = morse.strip()
    morse_words = morse.split('   ')  # Words separated by three spaces
    result = []

    for word in morse_words:
        letters = word.split(' ')
        decoded_word = ''
        for letter in letters:
            if letter in REVERSE_MORSE_DICT:
                decoded_word += REVERSE_MORSE_DICT[letter]
            else:
                return f"Error: Invalid Morse code sequence '{letter}'."
        result.append(decoded_word)
    return ' '.join(result)

def main():
    """Main function to run the Morse code translator."""
    while True:
        print("\nMorse Code Translator")
        print("1. Text to Morse")
        print("2. Morse to Text")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            text = input("Enter text to convert to Morse code: ")
            result = text_to_morse(text)
            print(f"Morse code: {result}")
        elif choice == '2':
            print("Enter Morse code (use '.' and '-' for code, single space between letters, three spaces between words):")
            morse = input()
            result = morse_to_text(morse)
            print(f"Text: {result}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
