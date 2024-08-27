"""
Created on Wed Aug 21 22:43:31 2024

Escreva um script que pergunte a quantidade de km
percorridos por um carro alugado pelo usuário e a
quantidade de dias pelo qual o carro foi alugado. Calcule o
preço a pagar sabendo que o carro custa 60 reais por dia e
15 centavos por Km rodado.

@author: mauricio
"""

############################################################

km = float(input("Km: "))
dias = int(input("Dias: "))

tot = (dias * 60) + (km * 0.15)

print(f"Valor a ser pago = [R${tot}]")

############################################################
