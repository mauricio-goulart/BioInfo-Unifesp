"""
Created on Tue Aug 27 18:17:39 2024

Crie um dicionário, chamado frutas, de frutas e seus preços.
a. Crie um segundo dicionário chamado compras na qual as
chaves são as frutas e valores é a quantidade a ser comprada
b. Calcule o preço total de um carrinho de compras de frutas
usando o dicionário criado no exercício anterior.
c. Remova todas as frutas do dicionário de frutas que custam
mais de R$ 5,00.

@author: mauricio
"""

############################################################

frutas = {"Uva" : 3.0, "Banana" : 7.0, "Rupias" : 4.0}
compras = {"Uva" : 5, "Banana" : 4, "Rupias" : 2}
soma = 0

for fruta in compras.keys():
    soma = (compras[fruta] * frutas[fruta]) + soma
    
############################################################
