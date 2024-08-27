"""
Created on Mon Aug 26 16:22:40 2024

Escreva um programa que simule um caixa eletrônico,
solicitando ao usuário que insira o valor do saque e informando quantas notas de cada valor serão entregues (considere notas
de R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2).

@author: mauricio
"""

############################################################

n = int(input("Digite o valor a ser sacado: "))

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0

while(n >= 100):
    n1 = n1 + 1
    n = n - 100
    
while(n >= 50):
    n2 = n2 + 1
    n = n - 50
    
while(n >= 20):
    n3 = n3 + 1
    n = n - 20
    
while(n >= 10):
    n4 = n4 + 1
    n = n - 10
    
while(n >= 5):
    n5 = n5 + 1
    n = n - 5
    
while(n >= 2):
    n6 = n6 + 1
    n = n - 2
    
    
print(f"Notas de R$100 = [{n1}]\nNotas de R$50 = [{n2}]\nNotas de R$20 = [{n3}]\nNotas de R$10 = [{n4}]\nNotas de R$5 = [{n5}]\nNotas de R$2 = [{n6}]\n")
    
############################################################

