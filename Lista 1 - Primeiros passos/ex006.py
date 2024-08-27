"""
Created on Wed Aug 21 22:30:12 2024

Leia o valor de um produto e calcule o valor final com 10% de
desconto.

@author: mauricio
"""

############################################################

prod = float(input("Valor produto: "))

desc = prod - (10/100 * prod)

print(f"Produto com desconto = [R${desc:.2f}]")

############################################################

