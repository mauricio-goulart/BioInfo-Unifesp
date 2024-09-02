"""
Created on Tue Aug 27 18:06:56 2024

Escreva um programa que gere um dicionário, onde cada chave
seja um caractere, e seu valor seja o número desse caractere
encontrado em uma frase lida.
Exemplo: O rato -> { “O”:1, “r”:1, “a”:1, “t”:1, “o”:1}

@author: mauricio
"""

############################################################

s1 = "O rato roeu a roupa do rei de roma"
s2 = set(s1)
dic = {}


for char in s2:
    dic[char] = s1.count(char)
    
    
for k, v in dic.items():
    print(f"{k} = {v}")

############################################################

