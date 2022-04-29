# string

# strings são imutáveis

multiline = '''Line #1
Line #2'''

print(len(multiline))

# o comprimento inclui os espaços em branco entre as linha de texto (\n)

multiline = """Line #1
Line #2"""

print(len(multiline))

# Demonstrating the ord() function.

# A função precisa de uma string de um único caratere como seu argumento
# - violar este requisito causa uma exceção TypeError ,
# e devolve um número que representa o code point do argumento.

char_1 = 'ç'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))

# Demonstrating the chr() function.

print(chr(97))
print(chr(945))


print(chr(ord("x")) == "x")
print(ord(chr(120)) == "x")

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)


# Poderá perguntar-se se a criação de uma nova cópia
# de uma string, cada vez que modifica o seu conteúdo, piora a eficácia do código.

print("min")

# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 &amp; 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

# Há uma condição - a sequência (string, lista, não importa) não pode estar vazia,
# ou então terá uma exceção ValueError .

print(min("Aa"))

print("max")

# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 &amp; 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

print(max("Aa"))


# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Demonstrating the list() function:
print(list("abcabc"))

# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))

# Demonstrating the capitalize() method:
print('aBcD'.capitalize())

print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

print('[' + 'gamma'.center(20, '*') + ']')

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

# Demonstrating the find() method:
print("Eta".find("ta"))
print("Eta".find("mma"))

# find() diferente do index() não gera erro quando não encontra o elemente indicado

# Se quiser realizar a procura, não desde o início da string,
# mas a partir de qualquer posição, pode usar uma variante de dois parâmetros do find()
# método. Veja o exemplo:

print('kappa'.find('a', 2))

# O segundo argumento especifica o index em que a
# pesquisa será iniciada (não tem de caber dentro da string).

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

# tambem aceita limite superior

t = 'Six lambdas'
print(t.isalnum())

t = 'ΑβΓδ'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))

# Demonstrating the split() method:
print("phi       chi\npsi".split())

# As únicas comparações que pode efetuar com impunidade são estas simbolizadas pelos == e != .
# O primeiro dá sempre False, enquanto o último produz sempre True.

#exceptions
#
# first_number = int(input("Enter the first number: "))
# second_number = int(input("Enter the second number: "))

# try:
#     print(first_number / second_number)
# except:
#     print("This operation cannot be done.")
#
# print("THE END.")
#
# try:
#     x = int(input("Enter a number: "))
#     y = 1 / x
#     print(y)
# except ZeroDivisionError:
#     print("You cannot divide by zero, sorry.")
# except ValueError:
#     print("You must enter an integer value.")
# except:
#     print("Oh dear, something went wrong...")
#
# print("THE END.")
#
# try:
#     x = int(input("Enter a number: "))
#     y = 1 / x
#     print(y)
# except ZeroDivisionError:
#     print("You cannot divide by zero, sorry.")
# except ValueError:
#     print("You must enter an integer value.")
# except:
#     print("Oh dear, something went wrong...")
#
# print("THE END.")

def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")

# Existe uma restrição grave: este tipo de instrução raise pode ser utilizada dentro
# do ramo except apenas; usá-la em qualquer outro contexto causa um erro.

def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise


try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")



# assert

#  assert expression

# Ela avalia a expressão;
# se a expressão for avaliada para True, ou um valor numérico não nulo, ou
# uma string não vazia, ou qualquer outro valor diferente de None, não fará mais nada;
# caso contrário, levanta automática e imediatamente uma exceção chamada AssertionError
# (neste caso, dizemos que a assertion falhou)

# as assertions não substituem as exceções nem validam os dados - são seus suplementos.


import math

x = float(input("Enter a number: "))
try:
    assert x >= 0.0
    x = math.sqrt(x)
except:
    print("Invalid value")





print(x)

# Todas as exceções Python pré-definidas formam uma hierarquia, ou seja,
# algumas delas são mais gerais (a que se chama BaseException é a mais geral),
# enquanto outras são mais ou menos concretas (por exemplo,
# IndexError é mais concreta do que LookupError).

# Não deve colocar exceções mais concretas antes das mais gerais dentro
# da mesma sequência de ramificações except .
# isso vai resultar em uma parte do código inacessível

try:
    print([1,2,3][5])



except IndexError:
    print("entrei")

except:
    print("entrei2")


# 1. Algumas exceções abstratas incorporadas em Python são:
#
# ArithmeticError,
# BaseException,
# LookupError.
#
# 2. Algumas exceções concretamente incorporadas em Python são:
#
# AssertionError,
# ImportError,
# IndexError,
# KeyboardInterrupt,
# KeyError,
# MemoryError,
# OverflowError.



print("mike" > "Mike")




