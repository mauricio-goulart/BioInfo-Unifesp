"""
Created on Wed Aug 21 22:16:43 2024

Faça um script que calcule o aumento de salário. Ele deve
solicitar o valor do salário e a porcentagem de aumento.
Exiba o valor do aumento e do novo salário.

@author: mauricio
"""

############################################################

sal = float(input("Salario: "))
porc = int(input("Porcentagem: "))

reaj = sal + (porc/100 * sal)

print(f"Salario Reajustado = [R${reaj:.2f}]")

############################################################

