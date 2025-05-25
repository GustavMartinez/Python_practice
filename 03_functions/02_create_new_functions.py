# A function definition specifies the name of a new function and the sequence of statements that run when the function is called.


# Function: A block of reusable code.

# Example of a new function:

def print_lyrics():
    print("So close, no matter how far")
    print("Couldn't be much more from the heart")
    print("Forever trusting who we are")
    print("And nothing else matters")

print_lyrics()


# Once you have defined a function, you can use it inside another function.

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    print_lyrics()
    

repeat_lyrics()
