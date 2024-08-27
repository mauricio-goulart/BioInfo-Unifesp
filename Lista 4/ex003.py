"""
Created on Mon Aug 26 22:09:55 2024

Escreva um programa que leia uma string e imprima quantas vezes cada
caractere aparece nessa string. String: TTAAC Resultado: T: 2x A: 2x C: 1x

@author: mauricio
"""

############################################################

s1 = "TTAACT"
chars = []
cont = []

for char in s1:
    if (char in chars):
        indice = chars.index(char)
        cont[indice] += 1
        
    else:
        chars.append(char)
        cont.append(1)


print("Resultado:")
for i in range(len(chars)):
    print(f"{chars[i]}: {cont[i]}x")

############################################################


