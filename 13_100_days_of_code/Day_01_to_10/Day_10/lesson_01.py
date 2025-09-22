
# functions with outputs

def format_name(f_name, l_name):

    """Take the first and last name and format it to
    return the title case version of the name"""

    f_name = f_name.title()
    l_name = l_name.title()


def format(f_name, l_name):
    return f"El nombre es: {f_name}, y el sobre nombre es: {l_name}"


nombre = format("Gustavo", "martinez")

print(nombre)



# New version:

def format_name_2(f_name, l_name):

    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"



print(format_name_2(input("What is your first name?"), input("What is your last name?")))