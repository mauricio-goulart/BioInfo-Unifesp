"""
Created on Tue Aug 27 19:35:08 2024

Crie um programa que gerencia o aproveitamento de um jogador
de futebol. o programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos em
cada partida. No final, tudo isso será guardado em um dicionário
incluindo o total de gols realizados durante o campeonato

@author: mauricio
"""

############################################################

jogador = {}

jogador["Nome"] = input("Nome: ")
jogador["Partidas"] = int(input("Partidas: "))

listgol = []

for i in range(0, jogador["Partidas"], +1):
    gol = int(input(f"{i + 1}º Partida| Quantidas de gol: "))
    listgol.append(gol)
    
jogador["Gols"] = sum(listgol)

############################################################