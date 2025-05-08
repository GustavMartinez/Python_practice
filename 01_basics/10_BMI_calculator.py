# BMI = weight (kg)/height**2 (meters**2)

height = float(input("Ingrese la altura: "))
weight = float(input("Ingrese su peso: "))

BMI = weight/height**2
print(BMI)

#Para arredondar un numero se utiliza la funcion round():
print(round(8/3)) #esta funcion va a devolver un numero arredondado.
print(round(8/3, 2))  #esta funcion va a devolver un numero arredondado con dos decimales


#manipulacion de una variable en base al valor de la variable anteriormente definida
# var+= 2 ---- var = var + 2