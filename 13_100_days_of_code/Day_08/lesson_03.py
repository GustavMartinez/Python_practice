"""

💪 This is a difficult challenge! 💪 

You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

2. Then check for the number of times the letters in the word LOVE occurs.   

3. Then combine these numbers to make a 2 digit number and print it out. 

"""

def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    
    # name 1
    T = name1.count("t") + name2.count("t")
    R = name1.count("r") + name2.count("r")
    U = name1.count("u") + name2.count("u")
    E = name1.count("e") + name2.count("e")

    L = name1.count("l") + name2.count("l")
    O = name1.count("o") + name2.count("o")
    V = name1.count("v") + name2.count("v")
    E2 = name1.count("e") + name2.count("e")

    true = T+R+U+E
    love = L+O+V+E2


    print(f"Love Score = {str(true)+str(love)}")



calculate_love_score("Kanye West", "Kim Kardashian")