# from module import suml, prodl
#
# zeroes = [0 for i in range(5)]
# ones = [1 for i in range(5)]
# print(suml(zeroes))
# print(prodl(ones))

# import sys
#
# for p in sys.path:
#     print(p)

#Nota: a pasta em que a execução começa é listada no elemento do primeiro caminho.

# Nota mais uma vez: há um ficheiro zip listado como um dos elementos do caminho
# - não é um erro. O Python é capaz de tratar ficheiros zip como pastas normais
# - isto pode poupar muito armazenamento.

from sys import path

path.append('.\\modules')
print(path)

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))

# A primeira pergunta tem uma resposta surpreendente: os pacotes, como os módulos,
# podem precisar de inicialização.
#
# A inicialização de um módulo é feita por um código unbound (não vinculado)
# (não faz parte de nenhuma função) localizado dentro do ficheiro do módulo.
# Como um pacote não é um ficheiro, esta técnica é inútil para inicializar pacotes.
#
# Em vez disso, é preciso usar um truque diferente - o Python espera que haja um
# ficheiro com um nome muito único dentro da pasta do pacote: __init__.py.
#
# O conteúdo do ficheiro é executado quando qualquer um dos módulos do pacote é importado.
# Se não quiser inicializações especiais, pode deixar o ficheiro vazio, mas não o deve omitir.