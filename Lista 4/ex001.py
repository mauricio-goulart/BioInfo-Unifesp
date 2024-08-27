"""
Created on Mon Aug 26 21:51:40 2024

Escreva um programa que leia duas strings. Verifique se a segunda ocorre
dentro da primeira e imprima a posição de início.
1a string: AABBEFAATT
2a string: BE

@author: mauricio
"""

############################################################

p1 = str(input("Palavra 1 = "))
p2 = str(input("Palavra 2 = "))

p3 = p1.find(p2)

if(p3 >= 0):
    print(f"Palavra 2 existe na palavra 1 e começa na posição = [{p3}]")
    
else:
    print("Palavra 2 não existe na palavra 1")

############################################################

