"""
Created on Wed Aug 21 21:52:25 2024

Escreva um script que leia a quantidade de dias,horas,
minutos e segundos para o usuário. Calcule o total em
segundos.

@author: mauricio
"""

############################################################

dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))

seg = (dias * 86400) + (horas * 3600) + (minutos * 60)

print(seg)

############################################################

 