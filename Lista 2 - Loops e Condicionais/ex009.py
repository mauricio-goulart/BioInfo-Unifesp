"""
Created on Mon Aug 26 16:35:04 2024

Crie um programa que determine se um número é um
número de Armstrong ou não. Um número de Armstrong é
aquele que é igual à soma de seus dígitos elevados à potência
do número de dígitos.

@author: mauricio
"""

############################################################

n = input("Digite um numero: ")
l = int(len(n))
n1 = int(n)
tot = 0

for num in n:
    tot = tot + int(int(num) ** l)
    
if (n1 == tot):
    print("É de armstrong")
    
else:
    print("Nao é de armstrong")

############################################################

