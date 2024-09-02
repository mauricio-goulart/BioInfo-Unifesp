"""
Created on Tue Aug 27 19:57:35 2024

Crie uma função chamada "calculadora" que recebe três
parâmetros: dois números e uma operação matemática (+,
-, *, /). A função deve retornar o resultado da operação.

@author: mauricio
"""

############################################################

def calculadora(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:  # Verifica se o divisor não é zero
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"

n = calculadora(3, 6, "*")

############################################################

