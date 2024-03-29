# Define the alphabet for reference
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to perform the Caesar Cipher operation
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    
    # Adjust shift amount based on the desired operation (encode/decode)
    if cipher_direction == "decode":
        shift_amount *= -1
    
    # Iterate through each character in the input text
    for char in start_text:
        # Check if the character is in the alphabet
        if char in alphabet:
            # Find the position of the character in the alphabet
            position = alphabet.index(char)
            
            # Calculate the new position after applying the shift
            new_position = position + shift_amount
            
            # Append the new character to the result
            end_text += alphabet[new_position]
        else:
            # If the character is not in the alphabet, keep it unchanged (e.g., numbers, symbols, spaces)
            end_text += char
    
    # Display the result
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

# Ask the user if they want to restart the cipher program using a while loop
should_end = False
while not should_end:
    # Get user inputs for direction, text, and shift
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    # Ensure the shift number is within the range of the alphabet
    shift = shift % 26

    # Call the caesar function with user inputs
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Ask the user if they want to go again
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")