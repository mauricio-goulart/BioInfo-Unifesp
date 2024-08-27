"""
Created on Wed Aug 21 23:05:04 2024

Em um script, o usuário deve responder à pergunta “Continuar
(s/n)?”. Se o
usuário digitar ‘s’ ou ‘S’, o script deve retornar a mensagem “OK,
continuando...”. Se o usuário digitar ‘n’ ou ‘N’, o script deve retornar
a mensagem “OK, parando...”. Por fim, se o usuário digitar qualquer
outra coisa,
o script deve retornar uma mensagem de erro.

@author: mauricio
"""

############################################################

cond = str(input("Continuar? [S/n]: "))

if cond not in ["S", "s", "N", "n"]:
    print("Digite S ou N")

elif cond in ["S","s"]:
    print("Continuando...")
    
else:
    print("Parando...")

############################################################

