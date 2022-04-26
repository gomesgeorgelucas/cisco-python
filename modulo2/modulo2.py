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
print("    *     " * 2)
print("   * *    " * 2)
print("  *   *   " * 2)
print(" *     *  " * 2)
print("***   *** " * 2)
print("  *   *   " * 2)
print("  *   *   " * 2)
print("  *****   " * 2)

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
print(+11_111 - 11)

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

# Operadores numéricos - +, -, *, /, //, %, **

print(2 + 2)

# Operações com flots vs integers sempre resultam em flots, exceto em divisão inteira de inteiros.

print(2 ** 0b11)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

print(6 / 3)
print(6 / 3.)
print(6. / 8)
print(6. / 3.)

print(6 // 3)
print(6 // 3.)
print(6. // 8)
print(6. // 3.)

# Isto é muito importante: o arredondamento vai sempre para o número inteiro menor.
print(6 // 4)
print(6. // 4)

print(6 / 4)
print(6. / 4)

# Como o resultado é negativo, o resultado é pro negativo menor mais próximo.
# Conhecida como floor division.
print(-6 // 4)
print(6. // -4)

print(4 % 14)
print(4 % -14)

print(12 % 4.5)

print(-4 + 4)
print(-4. + 8)

print(0.0 * -1)

print(+2)

# O resultado mostra claramente que o operador de exponenciação
# utiliza a ligação do lado direito.
print(2 ** 2 ** 3)

# Variáveis:

# o nome da variável deve ser composto por letras maiúsculas ou minúsculas,
# dígitos e o caratere _ (underscore)
# o nome da variável deve começar com uma letra;
# o caratere underscore é uma letra;
# letras maiúsculas e minúsculas são tratadas como diferentes
# (um pouco diferente do que no mundo real - Alice e ALICE são os mesmos nomes próprios,
# mas em Python são dois nomes de variáveis diferentes, e consequentemente, duas variáveis diferentes);
# o nome da variável não deve ser nenhuma das palavras reservadas de Python
# (as keywords - explicaremos mais sobre isto em breve).
# Além disso, o Python permite-lhe utilizar não só letras latinas mas também carateres
# específicos de línguas que utilizam outros alfabetos.

# Uma variável passa a existir como o resultado da atribuição de um valor a ela.
# Ao contrário de outras linguagens, não precisa de a declarar de nenhuma forma especial.
# Se atribuir qualquer valor a uma variável inexistente, a variável será automaticamente criada.
# Não precisa de fazer mais nada.
var = "1"
print("Text " + var)

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=",")
total_apples = john + mary + adam
print(total_apples)

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

x = float(-1)
y = (3 * (x ** 3)) - (2 * (x ** 2)) + (3 * x) - 1
print("y =", y)

# this program computes the number of seconds in a given number of hours
# this program has been written two days ago

a = 2  # number of hours
seconds = 3600  # number of seconds in 1 hour

print("Hours: ", a)  # printing the number of hours
print("Hours in seconds: ", a * seconds)  # printing the number of seconds in a given number of hours

# here we should also print "Goodbye", but a programmer didn't have time to write any code
print("Goodbye!")
# this is the end of the program that computes the number of seconds in 2 hours

# print("Tell me anything...")
# anything = input()
# print("Hmm...", anything, "... Really?")
#
# anything = input("Tell me anything...")
# print("Hmm...", anything, "...Really?")

# anything = input("Enter a number: ")
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

# anything = float(input("Enter a number: "))
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# hypo = (
# print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5))

# fnam = input("May I have your first name, please? ")
# lnam = input("May I have your last name, please? ")
# print("Thank you.")
# print("\nYour name is " + fnam + " " + lnam + ".")

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# int(arg1) float(arg2) são os parsers de string e str(arg1) é o parser de números

# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

# # input a float value for variable a here
# a = float(input("Input a: "))
# # input a float value for variable b here
# b = float(input("Input b: "))
# # output the result of addition here
# print(str(a+b))
# # output the result of subtraction here
# print(str(a-b))
# # output the result of multiplication here
# print(str(a*b))
# # output the result of division here
# print(str(a/b))

# print("\nThat's all, folks!")
#
# x = float(input("X = "))
# y = 1/(x + 1/(x + 1/(x + 1/x)))
# print(str(y))


# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
#
# dura_horas = dura // 60  # 10 h
# dura_mins = dura % 60  # 42 min
#
# horas_acumuladas = hour + dura_horas  # 33
# mins_acumulados = mins + dura_mins  # 100
#
# horas_correcao = mins_acumulados // 60  # 1
# mins_correcao = mins_acumulados % 60  # 40
#
# hora_final = (horas_acumuladas + horas_correcao) % 24
# mins_final = mins_correcao
#
# print(str(hora_final) + ":" + str(mins_final))

