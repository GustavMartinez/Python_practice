#tip calculator

#The program returns the valeu of the tip of a bill.
#so, it's needed: the valeu of the bill, the number of people and the percentage of the tip.

bill = float(input("digite el valor de la cuenta: $"))
people = input("Ingrese el numero de personas: ")
tip = float(input("Que porcentaje de propona le gustaria dar: 10, 12 o 15 porciento? "))


tip /= 100

propina = tip*bill

resultado = bill + propina

valor_final = resultado / int(people)

print(round(valor_final, 2))