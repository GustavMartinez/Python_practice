
"""

TODO-1: \nCreate a function called `encrypt()` that takes `original_text` and `shift_amount` as 2 inputs.

TODO-2: \nInside the 'encrypt' function, shift each letter of the `original_text` forwards in the alphabet by the `shift_amount` and print the encrypted text.

TODO-3: \nCall the `encrypt()` function and pass in the user inputs. You should be able to test the code and encrypt a message.

TODO-4: \nWhat happens if you try to shift the letter 'z' forwards by 9? Can you fix the code?

"""


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    
    encrypted = ""

    for i in original_text:
        position = alphabet.index(i) + shift_amount
        #if position>=25:
        #    position%=25 + 1
        position %= len(alphabet)
        encrypted = encrypted + alphabet[position]
    print(encrypted)

encrypt(text, shift)