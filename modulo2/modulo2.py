print("Modulo 2 Starting...")
print("Hello world")

# function_name(argument)
print("George Lucas")

# Nota: o Python faz uma exceção a esta regra
# permite que uma instrução se espalhe por mais do que uma linha
# (o que pode ser útil quando o seu código contém construções complexas).
print("The itsy bitsy spider climbed up the waterspout.")
print("Down came the rain and washed the spider out.")

print("The itsy bitsy spider climbed up the waterspout.")
# Pular linha
print()
print("Down came the rain and washed the spider out.")

print("The itsy bitsy spider\nclimbed up the waterspout.")
print("Down came the rain\nand washed the spider out.")

# print("\") - erro, tentando escapar aspas duplas e não fecha a string
# escapa barra invertida
print("\\")

# escapa aspas duplas
print("\"")

# function_name(argument1, argument2, ..., argumentN)
# !!! print() coloca um espaço em branco entre seus argumentos...
print("The itsy bitsy spider", "climbed up", "the waterspout.")

# argumentos devem ser passados em ordem de forma posicional
# (o segundo argumento será produzido após o primeiro...)
print("My name is", "Python.")
print("Monty Python.")

# argumentos de keyword seguem o padrão ([keyword] [=] [valor]) - deve ser incluído após o último argumento posicional
# print() possui (dois) argumento de keyword
# end - permite escolher os caracteres enviados ao final dos argumentos
# quando omisso, o valor padrão é (end = "\n")
print("My name is", "Python.", end=" ")
print("Monty Python.")
print("My name is", "Python.", end="\n")
print("Monty Python.")
print("My name is ", end="")
print("Monty Python.")

# sep - permite escolhe os caracteres de separação entre argumentos - padrão (sep = " ")
print("My", "name", "is", "Monty", "Python.", sep="-")

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

# Programming***Essentials***in...Python
print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# Tente:
#
# minimizar o número de invocações da função print() inserindo a sequência \n nas strings

print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

# fazer a seta duas vezes maior (mas mantendo as proporções)
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("***           ***")
print("   *         *")
print("   *         *")
print("   *         *")
print("   *         *")
print("   *         *")
print("   *         *")
print("   ***********")

# duplicar a seta, colocando ambas as setas lado a lado; nota:
# uma ‘string’ pode ser multiplicada ao usar o seguinte truque:
# "string" * 2 produzirá "stringstring" (brevemente, falaremos mais sobre o assunto)
print("    *     "*2)
print("   * *    "*2)
print("  *   *   "*2)
print(" *     *  "*2)
print("***   *** "*2)
print("  *   *   "*2)
print("  *   *   "*2)
print("  *****   "*2)

# Substitua algumas das aspas por apóstrofes; observe cuidadosamente o que acontece.
# Atenção ao misturar aspas simples e duplas
print('    ***********   <- utilizando aspas simples \'')

# Literais — São dados cujos valores são determinados pelo próprio literal.
# E esta é a pista: 123 é um literal, e c não é.

print("2")
print(2)

print(11111111)
# Python 3.6 introduziu ‘underscores’ em letras numéricas, permitindo a colocação de ‘underscores’
# únicos entre dígitos e após especificadores de base para melhorar a legibilidade.
# Este recurso não está disponível em versões mais antigas de Python.
print(11_111_111)
print(+11_111-11)

# octal (zero-o ou zero-O)
print(0o123)

# hexadecimal (zero-x ou zero-X)
print(0x123)

# floats - padrão [inteiro].[fração]
print(2.3)
print(.4)
print(4.)

# Quando quiser usar números muito grandes ou muito pequenos, pode usar notação científica.
# 3 x 10E8 -> 3E8 - o expoente (o valor após o E) deve ser um número inteiro
print(3E8)

# Constante de Planck 6.62607 x 10e-34
print(6.62607E-34)

# O Python escolhe sempre a forma económica de apresentação do número
print(0.0000000000000000000001)

# Strings

print("I like \"Monty Python\"")
print('I like "Monty Python"')

print('I\'m Monty Python')

# Booleanos - 'True' ou 'False'
# Não se pode mudar nada — incluindo case-sensitivity.
# True é tradado com 1 em comparações e 0 como False
print(True > 1)
print(1 < False)

print('"I\'m"\n""learning""\n"""Python"""')
print(0b1011)


