"""
Created on Wed Aug 28 17:41:07 2024

Aprendendo usar matplotlib

@author: mauricio
"""
#Imports:
import matplotlib.pyplot as plt
import numpy as np

############################################################

#Plotando no grafico
x = np.arange(0,20)
y = np.random.randint(0,10,(20))

plt.figure() # Reinicia um plot novo pra nao misturar os graficos
plt.scatter(x,y)

plt.figure()
plt.plot(x,y)

plt.figure()
plt.bar(x,y)

plt.figure()
plt.pie(x)

############################################################

#Customizando o grafico e multiplos graficos

x = np.arange(-20,21)
y = x**2 -1
yy = x + 2

plt.figure()
plt.plot(x,y, "bo", linewidth=2) #bo b - blue o - circulo, linewidth tamanho linha
plt.plot(x, yy, "r")
plt.title("Meu grafico") # Titulo no grafico
plt.xlabel("Eixo X") # Titulo no Eixo x
plt.ylabel("Eixo Y") # Titulo no Eixo y
plt.grid() # Quadricula o fundo

#Multiplos graficos com for

plt.figure()

for i in range(1,5):
    plt.plot(x**i, y)
    
############################################################

#Multiplos graficos com Subplot

plt.figure()
plt.subplot(2,2,1) #informa a matriz da tela (2,2) e em qual lugar vai botar 1 a 4 no caso e depois plot
plt.plot(x,x)
plt.subplot(2,2,2)
plt.plot(x,x**2)
plt.subplot(2,2,3)
plt.plot(x,x**3)
plt.subplot(2,2,4)
plt.plot(x,x**4)

############################################################
