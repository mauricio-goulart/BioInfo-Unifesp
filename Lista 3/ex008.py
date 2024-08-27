"""
Created on Mon Aug 26 17:44:14 2024

Escreva uma função que recebe uma lista de strings e retorna a
string mais longa.

@author: mauricio
"""

############################################################

list1 = []
maior = ""

for i in range (2):
    
    str1 = str(input(f"{i + 1} Palavraº: "))
    list1.append(str1)
    

for palavra in list1:
    maior = palavra
    
    if (len(maior) < len(palavra)):
        maior = palavra
    
print(f"Maior = {maior}")

############################################################