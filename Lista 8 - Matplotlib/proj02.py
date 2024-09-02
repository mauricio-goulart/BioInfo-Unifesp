"""
Created on Wed Aug 28 22:53:05 2024

Desafio: Processamento de Imagens Biomédicas com NumPy
Instruções:
1. Importe as bibliotecas NumPy como np e Matplotlib.pyplot como plt.
2. Carregue uma imagem biomédica em escala de cinza utilizando a
função plt.imread() e atribua-a a uma variável chamada imagem.
3. Converta a imagem para um array NumPy.
4. Normalize a intensidade dos pixels da imagem para o intervalo de 0
a 1 dividindo todos os valores por 255.
5. Aplique uma transformação de negativo na imagem, subtraindo cada
valor do pixel de 1.
6. Realize uma operação de thresholding na imagem, convertendo
todos os valores de pixel abaixo de um determinado limite para 0 e
os valores acima do limite para 1.
7. Crie um filtro de média 3x3 e aplique na imagem.
8. Imprima a imagem original, a imagem com o negativo, a imagem
binarizada após o thresholding e a imagem após o filtro de média.

@author: mauricio
"""
#Imports:
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import uniform_filter

############################################################
imagem = plt.imread('bio.jpg')

imagem_np = np.array(imagem)

imagem_normalizada = imagem_np / 255.0

imagem_negativo = 1 - imagem_normalizada

imagem_threshold = imagem_negativo

limite = 0.5

for l in range(imagem_threshold.shape[0]):
    for c in range(imagem_threshold.shape[1]):
        for k in range(imagem_threshold.shape[2]):
            if imagem_threshold[l, c, k] > limite:
                imagem_threshold[l, c, k] = 1
            else:
                imagem_threshold[l, c, k] = 0
                
imagem_filtrada = uniform_filter(imagem_np, size=(3, 3, 1))

plt.figure()
plt.subplot(2,3, 1)
plt.imshow(imagem_np)
plt.subplot(2,3, 2)
plt.imshow(imagem_normalizada)
plt.subplot(2,3, 3)
plt.imshow(imagem_negativo)
plt.subplot(2,3, 4)
plt.imshow(imagem_threshold)
plt.subplot(2,3, 1)
plt.imshow(imagem_filtrada)

############################################################




        



