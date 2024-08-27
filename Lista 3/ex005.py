"""
Created on Mon Aug 26 17:36:32 2024

Faça um Programa que peça as quatro notas de 5 alunos, calcule e
armazene numa lista a média de cada aluno, imprima o número de
alunos com média maior ou igual a 7.0

@author: mauricio
"""

############################################################

list1 = []

for i in range(5):
    
    print(f"\nAluno {i + 1: }")
    n1 = float(input("Digite a 1º nota: "))
    n2 = float(input("Digite a 2º nota: "))
    n3 = float(input("Digite a 3º nota: "))
    n4 = float(input("Digite a 4º nota: "))
    
    media = (n1+n2+n3+n4) / 4
    
    list1.append(media)

for i in list1:
    
    if (i > 7.0):
        print(i)
        
############################################################
