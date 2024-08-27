"""
Created on Wed Aug 21 22:55:20 2024

Em química, o pH de uma solução aquosa é uma medida da sua
acidez.Os
Valores de pH variam entre 0 e 14. Soluções ácidas tem pH maior
que 7. Soluções básicas tem pH menor que 7. Soluções neutras tem
pH igual a 7. Escreva duas funções que recebem um número
correspondente ao pH de uma solução aquosa e exibem na tela o
tipo de solução (algo como “A solução é ácida”).

@author: mauricio
"""

############################################################

ph = int(input("Digite o Ph: "))

if ph == 7:
    print("Neutra")

elif ph < 7 and ph >= 0:
    print("Basica")
    
elif ph > 7 and <= 14:
    print("Acida")
    
else:
    print("Não existe, digite um numero de 0 a 14")

############################################################


