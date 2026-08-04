"""
TO DO-1: \nCreate a function called `encrypt()` that takes `original_text` and `shift_amount` as 2 inputs.

TO DO-2: \nInside the 'encrypt' function, shift each letter of the `original_text` forwards in the alphabet by the `shift_amount` and print the encrypted text.

TO DO-3: \nCall the `encrypt()` function and pass in the user inputs. You should be able to test the code and encrypt a message.

TO DO-4: \nWhat happens if you try to shift the letter 'z' forwards by 9? Can you fix the code?
"""
"""
TO DO-1: \nCreate a function called `decrypt()` that takes `original_text` and `shift_amount` as 2 inputs

TO DO-2: \nInside the `decrypt()` function, shift each letter of the `original_text` forwards in the alphabet *backwards* by the `shift_amount` and print the decrypted text.

TO DO-3: \n- Combine the `encrypt()` and `decrypt()` functions into a single function called `caesar()`. \n- Use the value of the user chosen `direction` variable to determine which functionality to use. \n- call the caesar function instead of encrypt/decrypt and pass in all three variables `direction`/`text`/`shift`.
"""



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, original_text, shift_amount):

    if direction == 'encode':
        shift_amount*= 1
    elif direction == 'decode':
        shift_amount*= -1
    else:
        return print('Wrong direction')
        

    output = ""

    for letter in original_text:
        if letter not in alphabet:
            output+=letter
        else:
            index_letter = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output += alphabet[index_letter]

    print(output)



new_process = True

while new_process:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction=direction, original_text=text, shift_amount=shift)

    restart = input("Do you want to restart? y or n: \n\t")

    if restart == 'n':
        new_process = False


