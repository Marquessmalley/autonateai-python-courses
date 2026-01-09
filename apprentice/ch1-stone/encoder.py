# Secret Encoder - Your First Real Project!

def encode_message(message):
    """Shift each letter forward by 3"""
    encoded = ""
    
    for letter in message:
        if letter.isalpha():  # if it's a letter
            # Get the letter's code number
            code = ord(letter)
            # Shift by 3
            code = code + 3
            # Convert back to a letter
            encoded = encoded + chr(code)
        else:
            encoded = encoded + letter  # keep spaces
    
    return encoded

# Main program
print("🔐 SECRET ENCODER 🔐")
message = input("Enter your message: ")
secret = encode_message(message)
print("Your secret code is: " + secret)