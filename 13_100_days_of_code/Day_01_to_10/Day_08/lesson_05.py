
"""
TODO-1: \nCreate a function called `decrypt()` that takes `original_text` and `shift_amount` as 2 inputs

TODO-2: \nInside the `decrypt()` function, shift each letter of the `original_text` forwards in the alphabet *backwards* by the `shift_amount` and print the decrypted text.

TODO-3: \n- Combine the `encrypt()` and `decrypt()` functions into a single function called `caesar()`. \n- Use the value of the user chosen `direction` variable to determine which functionality to use. \n- call the caesar function instead of encrypt/decrypt and pass in all three variables `direction`/`text`/`shift`.


"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(direction, original_text, shift_amount):

    def encrypt(original_text, shift_amount):
        
        encrypted = ""

        for i in original_text:
            position = alphabet.index(i) + shift_amount
            position %= len(alphabet)
            encrypted = encrypted + alphabet[position]
        print(encrypted)


    def decrypt(original_text, shift_amount):
        
        decrypt = ""
        
        for i in original_text:
            position = alphabet.index(i) - shift_amount
            position %= len(alphabet)
            decrypt = decrypt + alphabet[position]
        print(decrypt)
        

    if direction == "encrypt":
        encrypt(original_text, shift_amount)
    
    elif direction == "decrypt":
        decrypt(original_text, shift_amount)

    else:
        print("No funciono")


caesar(direction, text, shift)
