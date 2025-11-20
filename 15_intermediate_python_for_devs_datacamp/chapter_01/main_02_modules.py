"""
Modules are Python scripts

- Files ending with .py
- Contain functions and attributes
- Can contain other modules
- Help us avoid rewriting code that already exists

- There are around 200 built-in modules

- Two more popular: OS, string

OS module:

- Used for interacting with our operating system
- Check the current directory
- List available files
- Access environment variables

String module:

- simplifies text processing tasks

"""

import os

# print(help(os)) >>> This get all the info about the module

work_dir = os.getcwd() # Saves the current working directory

print(work_dir) # This returns the current working directory


# Changing directory:
os.chdir("/home/gustavo")
print(os.getcwd())


# info about the local environment:
print(os.environ)



import string

# Attributes:
string.ascii_lowercase
string.digits
string.punctuation