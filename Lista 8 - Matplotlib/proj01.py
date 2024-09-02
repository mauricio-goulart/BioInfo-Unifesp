"""
Created on Wed Aug 28 19:16:25 2024

Instruções:
1. Crie um array unidimensional chamado dados com 1000 elementos
inteiros aleatórios no intervalo de 1 a 100.
2. Utilizando NumPy, calcule a média, mediana, desvio padrão e
variância dos valores no array dados. Armazene cada resultado em
uma variável correspondente.
3. Crie um histograma com 20 bins utilizando a função plt.hist() para
visualizar a distribuição dos valores no array dados.
4. Crie um novo array chamado dados_filtrados que contenha apenas
os valores maiores que a média calculada no passo 3.
5. Utilizando a função plt.boxplot(), crie um boxplot para visualizar a
distribuição dos valores no array dados_filtrados.
6. Imprima na tela as estatísticas resumidas dos valores no array
dados_filtrados utilizando a função np.stats.describe().

@author: mauricio
"""
#Imports:
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

############################################################

m = np.random.randint(1,100, (1000))

media_m = np.mean(m)
mediana_m = np.median(m)
desvm_m = np.std(m)

plt.figure()
plt.hist(m, bins=20, edgecolor="black")
plt.title("Histograma")
plt.xlabel("Valor")
plt.ylabel("Frequencia")

fm = m[m > media_m]

plt.figure()
plt.boxplot(fm)
plt.title("Dados filtrados")
plt.xlabel("Valor")

print(stats.describe(fm))
############################################################

