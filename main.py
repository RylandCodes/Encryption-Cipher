
Encryption_Shift = None


letters = list("abcdefghijklmnopqrstuvwxyz")

def encrypt():

    message = input("Enter message (Messages will become lower case): ").lower()
    Encryption_Shift = int(input("Enter Encryption Shift: "))
    encoded_message = ""


    for letter in message:
        if letter in letters:
            letter_index = letters.index(letter)
            letter_index = (letter_index - Encryption_Shift) % 26 
            letter = letters[letter_index]
        
        encoded_message += letter

    print(f"Encoded Message: {encoded_message}")
    return encoded_message


def decrypt():
    encoded_message = input("Enter encoded message (Messages will become lower case): ").lower()
    Encryption_Shift = int(input("Enter Encryption Shift: "))
    decoded_message = ""
    

    for letter in encoded_message:
        if letter in letters:
            letter_index = letters.index(letter)
            letter_index = (letter_index + Encryption_Shift) % 26  
            letter = letters[letter_index]
        decoded_message += letter


    print(f"Decrypted Message: {decoded_message}")
    return decoded_message


while True:
    mode = input("What mode do you want [encrypt/decrypt]: ").lower()

    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        continue

    if mode == "encrypt":
        encrypt()
    elif mode == "decrypt":
        decrypt()