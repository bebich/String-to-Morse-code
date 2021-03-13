STRING_CHARACTER_TO_MORSE_CHARACTER = {'A': '.-', 'B': '-...',
                                       'C': '-.-.', 'D': '-..', 'E': '.',
                                       'F': '..-.', 'G': '--.', 'H': '....',
                                       'I': '..', 'J': '.---', 'K': '-.-',
                                       'L': '.-..', 'M': '--', 'N': '-.',
                                       'O': '---', 'P': '.--.', 'Q': '--.-',
                                       'R': '.-.', 'S': '...', 'T': '-',
                                       'U': '..-', 'V': '...-', 'W': '.--',
                                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                                       '1': '.----', '2': '..---', '3': '...--',
                                       '4': '....-', '5': '.....', '6': '-....',
                                       '7': '--...', '8': '---..', '9': '----.',
                                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                                       '?': '..--..', '/': '-..-.', '-': '-....-',
                                       '(': '-.--.', ')': '-.--.-'}

print("Hello! Welcome to Morse encryption and decryption program!")

while True:
    print("Enter the text you would like to encrypt: ")
    word_to_encrypt = input("").upper()
    encrypted_word = ""
    unfamiliar_character = False

    for letter in word_to_encrypt:
        if letter in STRING_CHARACTER_TO_MORSE_CHARACTER:
            encrypted_word += STRING_CHARACTER_TO_MORSE_CHARACTER.get(letter)
        elif letter == " ":
            encrypted_word += " "
        else:
            print(f"Unfamiliar character in '{word_to_encrypt}'! Please try again.")
            unfamiliar_character = True

    if not unfamiliar_character:
        print(f"Text {word_to_encrypt} in Morse code is:\n {encrypted_word}")

    close_app = input("If you want to exit the program press enter 'Y' or else enter any key:  ").upper()
    if close_app == "Y":
        break

print("Thank you for using our program!")
