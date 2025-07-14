"""

TO DO-1: \nImport and print the logo from art.py when the program starts.

TO DO-2: \nWhat happens if the user enters a number/symbol/space that's not in the List `alphabet`?\n\nCan you fix the code to keep the number/symbol/space when the text is encoded/decoded?

TO DO-3: \n\nCan you figure out a way to restart the cipher program?

"""



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, original_text, shift_amount):

    # Encrypt
    def encrypt(original_text, shift_amount):
        
        encrypted = ""

        for i in original_text:
            if i.isalpha():
                position = alphabet.index(i) + shift_amount
                position %= len(alphabet)
                encrypted = encrypted + alphabet[position]
            else:
                encrypted += i
        print(encrypted)

    # Decrypt
    def decrypt(original_text, shift_amount):
        
        decrypt = ""
        
        for i in original_text:
            if i.isalpha():
                position = alphabet.index(i) - shift_amount
                position %= len(alphabet)
                decrypt = decrypt + alphabet[position]
            else:
                decrypt += i
        print(decrypt)
        

    if direction == "encrypt":
        encrypt(original_text, shift_amount)
    
    elif direction == "decrypt":
        decrypt(original_text, shift_amount)

    else:
        print("No funciono")



again = True

while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)


    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    
    if restart == 'yes':
        again = True
    else:
        again = False
