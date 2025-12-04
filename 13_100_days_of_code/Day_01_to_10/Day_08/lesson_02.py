def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location} ")

# positional arguments
greet_with("Gustavo", "Belo horizonte")
greet_with("Belo horizonte","Gustavo")

# keyword arguments
greet_with(location="Brasilia", name="Gabriela")
