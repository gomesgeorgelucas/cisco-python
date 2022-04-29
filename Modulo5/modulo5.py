# modulos

# Todos estes módulos, juntamente com as funções integradas,
# formam a Python standard library

# math

# A instrução pode estar localizada em qualquer parte do seu código,
# mas deve ser colocada antes da primeira utilização de qualquer uma das entidades do módulo.


# Um namespace é um espaço (entendido num contexto não físico) no qual alguns nomes existem,
# e os nomes não entram em conflito entre si (ou seja, não existem dois objetos
# diferentes com o mesmo nome). Podemos dizer que cada grupo social é um namespace
# - o grupo tende a nomear cada um dos seus membros de uma forma única (por exemplo,
# os pais não dão aos seus filhos os mesmos nomes próprios).


# import math
# import sys
#
# print(math.sin(10))
#
# # Nota: a utilização desta qualificação é obrigatória se um módulo tiver
# # sido importado pela instrução do módulo import .
#
# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None
#
#
# pi = 3.14
#
# print(sin(pi/2))
# print(math.sin(math.pi/2))

import math

# Nota: nenhuma outra entidade é importada.
# Além disso, não se pode importar entidades adicionais utilizando
# uma qualificação - uma linha como esta:

print(math.sin(math.pi/2))

#  Nnome de uma entidade (ou a lista de nomes das entidades)
#  é substituído por um único asterisco (*).
#
# Tal instrução importa todas as entidades do módulo indicado.

# from moduel import *

# as :  Aliasing faz com que o módulo seja identificado com um nome diferente do original.
# Isto também pode encurtar os nomes qualificados.

# import module as alias

# Por sua vez, quando utiliza a variante from module import name e precisa de mudar o nome
# da entidade, faz um alias para a entidade. Isto fará com que o nome seja substituído
# pelo alias que escolher.

# from module import name as alias
# from module import n as a, m as b, o as c

# for name in dir(math):
#     print(name, end="\n")

# Nota: a função pow() .
#
# pow(x, y) → encontrar o valor de xy (atenção aos domínios)
# Esta é uma função integrada, e não tem de ser importada.

print(pow(math.e, 1) == math.exp(math.log(math.e)))
print(pow(2, 2) == math.exp(2 * math.log(2)))
print(math.log(math.e, math.e) == math.exp(0))

from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

# Os algoritmos não são aleatórios - são deterministas e previsíveis.
# Apenas os processos físicos que estão completamente fora do nosso controlo
# (como a intensidade da radiação cósmica) podem ser utilizados como fonte de dados
# aleatórios reais. Os dados produzidos por computadores determinísticos não podem ser
# aleatórios de forma alguma.


from random import random, seed

#seed(0)

for i in range(5):
    print(random())


# Se quiser valores inteiros aleatórios, uma das seguintes funções encaixar-se-ia melhor:
# Note-se a exclusão implícita do lado direito!
# randrange(end)
# randrange(beg, end)
# randrange(beg, end, step)
# randint(left, right)

from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

#lidando com numeros repetivos

from random import randint

for i in range(10):
    print(randint(1, 10), end=',')

# A primeira variante escolhe um elemento "aleatório" a partir da sequência de input e devolve-o.
#
# O segundo constrói uma lista (uma amostra; em inglês, uma sample) que consiste no
# elemento elements_to_choose “sorteado” a partir da sequência de input.

# choice(sequence)
# sample(sequence, elements_to_choose)

print()
print("choice")

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

from platform import platform

print(platform(False, False, ))

from platform import machine

print(machine())

from platform import processor

print(processor())

from platform import system

print(system())

from platform import version

print(version())

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)


