# Decisões em Python

# 1	+, -	       unário
# 2	**
# 3	*, /, //, %
# 4	+, -	       binário
# 5	<, <=, >, >=
# 6	==, !=

# n = float(input("N=")) >= 100
#
# print(n)

# uma expressão (uma pergunta ou uma resposta) cujo valor será interpretado unicamente em termos de True
# (quando o seu valor é diferente de zero) e False (quando é igual a zero);
# Python 3 não permite a mistura de espaços e tabs para indentação.

# O segundo caso especial introduz outra nova keyword de Python: elif.
# Como provavelmente suspeitará, é uma forma mais curta de else if.

# Nota: se algum dos ramos if-elif-else contiver apenas uma instrução,
# pode codificá-la de uma forma mais abrangente
# (não precisa de fazer uma linha indentada após a keyword,
# mas apenas continuar a linha após os dois pontos).

# Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# # Choose the larger number
# if number1 > number2: larger_number = number1
# else: larger_number = number2
#
# # Print the result
# print("The larger number is:", larger_number)

# Neste caso, utilizaremos uma espécie de notação que não é uma linguagem de programação real
# (não pode ser compilada nem executada),
# mas que é formalizada, concisa e legível. Chama-se pseudo-código.

# # Read three numbers.
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
#
# # Check which one of the numbers is the greatest
# # and pass it to the largest_number variable.
#
# largest_number = max(number1, number2, number3)
#
# # Print the result.
# print("The largest number is:", largest_number)

# plant = input("Plant = ")
#
# if plant == "Spathiphyllum":
#     print("Yes - " + plant + " is the best plant ever!")
# elif plant == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print("Spathiphyllum! Not " + plant + "!")

# income = float(input("Enter the annual income: "))
#
# if income <= 85_528:
#     tax = 0.18 * income - 556.2
# elif income > 85_528:
#     tax = 14_839.2 + 0.32 * (income - 85_528)
#
# if tax <= 0:
#     tax = 0.0
#
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")
#

# year = int(input("Enter a year: "))
#
# if year >= 1528:
#     if year % 4 != 0:
#         print("Common year")
#     elif year % 100 != 0:
#         print("Leap year")
#     elif year % 400 != 0:
#         print("Common year")
#     else:
#         print("Leap year")
# else:
#     print("Not within the Gregorian calendar period.")

# Certas expressões podem ser simplificadas sem alterar o comportamento do programa.
#
# Tente lembrar-se de como o Python interpreta a verdade de uma condição e observe que estas duas formas
# são equivalentes:
#
# while number != 0: e while number:.
#
# A condição que verifica se um número é ímpar também pode ser codificada nestas formas equivalentes:
#
# if number % 2 == 1: e if number % 2:.

# A propósito, olha para a função print() . A forma como a utilizámos aqui chama-se
# impressão multi-linha. Pode usar aspas triplas para imprimir strings em várias linhas a fim de
# tornar o texto mais fácil de ler, ou criar um desenho especial baseado em texto. Experimente-o.

# secret_number = 777
#
# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)
# #
# guess = int(input("Guess and integer number: "))
#
# while guess != 777:
#     print("Ha ha! You're stuck in my loop!")
#     guess = int(input("Guess and integer number: "))
# print("Well done, muggle! You ae free now.")

#
# for i in range(100):
#     # do_something()
#     pass

# nota: neste caso, a função range() começa o seu trabalho a partir do 0 e termina
# um passo (um número inteiro) antes do valor do seu argumento;

# range(início, limite superior não inclusivo, passo)
for i in range(10):
    print("The value of i is currently", i)
print()
for i in range(2, 8):
    print("The value of i is currently", i)
print()
for i in range(2, 8, 3):
    print("The value of i is currently", i)
print()

# for não quebra se o passo extrapolar o limite
for i in range(3, 8, 3):
    print("The value of i is currently", i)

# Won't execute
for i in range(1, 1):
    print("The value of i is currently", i)

# Nota: o conjunto gerado pelo range() tem de estar ordenado por ordem crescente.
# Não há como forçar o range() a criar um conjunto de uma forma diferente quando
# a função range() aceita exatamente dois argumentos. Isto significa que o segundo argumento
# de range() deve ser maior que o primeiro.

power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

# import time

# Write a for loop that counts to five.
# Body of the loop - print the loop iteration number and the word "Mississippi".
# Body of the loop - use: time.sleep(1)

# Write a print function with the final message.
# for count in range(1,6):
#     print(str(count) + " Mississippi")
#     time.sleep(1)
# print("Ready or not, here I come!")

# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

# largest_number = -99999999
# counter = 0
#
# while True:
#     number = int(input("Enter a number or type -1 to end program: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number
#
# if counter != 0:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")

# largest_number = -99999999
# counter = 0
#
# number = int(input("Enter a number or type -1 to end program: "))
#
# while number != -1:
#     if number == -1:
#         continue
#     counter += 1
#
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to end program: "))
#
# if counter:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")

# secret = "chupacabra"
#
# guess = input("Guess the word: ")
#
# while True:
#     guess = input("Guess the word: ")
#     if guess == secret:
#         break
# print("You've successfully left the loop")

# Prompt the user to enter a word
# and assign it to the user_word variable.
# user_word = input("Vowel eater: ").upper()
#
# for letter in user_word:
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#     else:
#         print(letter)

# user_word = input("Vowel eater: ").upper()
#
# word_without_vowels = ""
#
# for letter in user_word:
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#     else:
#         word_without_vowels += letter
# print(word_without_vowels)

# i = 1
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("else:", i)

# i = 5
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("else:", i)

# i = 1
# while i < 5:
#     print(i)
#     break
#     i += 1
# else:
#     print("else:", i)
#
# for i in range(5):
#     print(i)
# else:
#     print("else:", i)

# lu = 111
# for lu in range(2, 1):
#     print(lu)
# else:
#     print("else:", lu)

# blocks = int(input("Enter the number of blocks: "))
#
# #
# # Write your code here.
# #
#
# height = 0
# lineBricks = 0
# if blocks >= 1:
#     while True:
#         lineBricks += 1
#         if (blocks - lineBricks) == 0:
#             height += 1
#             break
#         elif (blocks - lineBricks) >= (lineBricks + 1):
#             blocks -= lineBricks
#             height += 1
#             continue
#         else:
#             height += 1
#             break
#
# print("The height of the pyramid:", height)

# c0 = int(input("c0 = "))
# steps = 0
# if c0 > 0:
#     while True:
#         if c0 % 2 == 0:
#             c0 /= 2
#             print("new c0 = " + str(int(c0)))
#         else:
#             c0 = 3 * c0 + 1
#             print("new c0 = " + str(int(c0)))
#         steps += 1
#         if c0 != 1:
#             continue
#         else:
#             break
# else:
#     print("Invalid integer! Must be a non-null integer.")
#
# print("final c0= " + str(int(c0)))
# print("steps = " + str(steps))

# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")
print()
# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

print()

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")

# not
# Sua prioridade é muito alta: a mesma que o unário + e -
# and
# É um operador binário com uma prioridade que é inferior à expressa pelos operadores de comparação.
# or
# É um operador binário com uma prioridade inferior a and ( assim como + comparado com *).

# Pode estar familiarizado com as leis de De Morgan. Dizem que:
#
# A negação de uma conjunção é a disjunção das negações.
#
# A negação de uma disjunção é a conjunção das negações.

# not (p and q) == (not p) or (not q)
# not (p or q) == (not p) and (not q)

# Os operadores lógicos tomam os seus argumentos como um 'todo'
# independentemente da quantidade de bits que contenham.
# Os operadores só estão conscientes do valor:
# zero (quando todos os bits são redefinidos) significa False;
# não zero (quando pelo menos um bit está definido) significa True.
print()

i = 1
j = not not i
print(j)

i = 0b101
j = not not i
print(j)

i = 0b000
j = not not i
print(j)

# Aqui estão todos eles:
#
# & (e comercial) - conjunção bitwise;
# | (barra) - disjunção bitwise;
# ~ (til) - negação bitwise;
# ^ (acento circunflexo) - bitwise exclusive ou (xor).

# Acrescentemos uma observação importante: os argumentos destes operadores devem ser inteiros;
# não devemos utilizar floats aqui.
#
# A diferença no funcionamento dos operadores lógicos e de bit é importante:
# os operadores lógicos não penetram no nível de bits do seu argumento.
# Eles só estão interessados no valor inteiro final.

# Negação binária utiliza complementos de dois
print("Nosso bit é o quarto bit")
flag_register = 0b01000010000111111000010001101000
print(format(flag_register, '#b'))
the_mask = 8
print("Nossa máscara é 8, 2^3 representando a casa onde o bit se encontra - " +
      format(the_mask, '#b'))
if flag_register & the_mask:
    print("My bit is set")
else:
    print("My bit is not set")
print("Atribui 0 ao bit fazendo a conjunção com a negação da máscara")
flag_register &= ~the_mask
print(format(flag_register, '#b'))
print("Reatribui 1 ao bit fazendo a disjunção com a máscara")
flag_register |= the_mask
print(format(flag_register, '#b'))
print("Utiliza o xor como switch 0 e 1")
flag_register ^= the_mask
print(format(flag_register, '#b'))
flag_register ^= the_mask
print(format(flag_register, '#b'))

var = 17
print("var = " + format(var, '#b'))
var_right = var >> 1
print("var shifted right 1 bit = " + format(var_right, '#b'))
var_left = var << 2
print("var shifted left 2 bita = " + format(var_left, '#b'))
print(var, var_left, var_right)

# E aqui está a tabela de prioridades atualizada, contendo todos os operadores introduzidos até agora:
#
# Prioridade	   Operador
#       1	        ~, +, -         unário
#       2	        **
#       3	        *, /, //, %
#       4	        +, -	        binário
#       5	        <<, >>	        (bitwise)
#       6	        <, <=, >, >=
#       7	        ==, !=
#       8	        &
#       9	        |
#       10	        =, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=

#Listas

# Os elementos dentro de uma lista podem ter tipos diferentes.
# Alguns deles podem ser inteiros, outros floats, e outros ainda podem ser listas.

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list content:", numbers)  # Printing current list content.

print(numbers)  # Printing the whole list.

# Se quiser verificar o comprimento atual da lista, pode usar uma função chamada len()
# (o seu nome vem de length (comprimento)).
#
# A função toma o nome da lista como argumento, e devolve o número de elementos atualmente
# armazenados dentro da lista (por outras palavras - o comprimento da lista).

print(len(numbers))  # Printing the whole list.

# Qualquer elemento da lista pode ser removido a qualquer momento
# isto é feito com uma instrução chamada del (delete).
# Nota: é uma instrução, não uma função.
#
# É preciso apontar o elemento a ser removido - desaparecerá da lista,
# e o comprimento da lista será reduzido em um.

del numbers[1]
print(len(numbers))
print(numbers)

# Um elemento com um index igual a -1 é o último na lista.
numbers = [111, 7, 2, 1]
print(numbers[-1])
print(numbers[-2])

# hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
#
# # Step 1: write a line of code that prompts the user
# # to replace the middle number with an integer number entered by the user.
# new_number = int(input("New number to replace middle number: "))
# hat_list[2] = new_number
# # Step 2: write a line of code that removes the last element from the list.
# del hat_list[-1]
# # Step 3: write a line of code that prints the length of the existing list.
# print(len(hat_list))
# print(hat_list)

# Funções vs. métodos
# Um método é um tipo específico de função - comporta-se como uma função e parece uma função,
# mas difere na forma como atua, e no seu estilo de invocação.
#
# Uma função não pertence a nenhum dado - recebe dados, pode criar novos dados
# e (geralmente) produz um resultado.
#
# Um método faz todas estas coisas, mas também é capaz de alterar o estado de uma entidade selecionada.
#
# Um método é propriedade dos dados para os quais trabalha,
# enquanto uma função é propriedade de todo o código.

# result = function(arg) vs result = data.method(arg)

# O método comportar-se-á como uma função, mas pode fazer algo mais
# pode alterar o estado interno dos dados a partir dos quais foi invocado.

# Adicionar elementos a uma lista (métodos): append(value) e insert(location, value)
# location mostra a localização necessária do elemento a ser inserido;
# nota: todos os elementos existentes que ocupam locais à direita do novo elemento
# (incluindo o que se encontra na posição indicada) são deslocados para a direita,
# a fim de criar espaço para o novo elemento;
print("Append e Insert")
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#

numbers.insert(1, 333)
print(numbers)

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

# swap em Python

variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary

# swap otimizado

variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

# # step 1
# beatles = []
# print("Step 1:", beatles)
#
# # step 2
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
# print("Step 2:", beatles)
#
# # step 3
# for new_member in range(2):
#     beatles.append(input("New member: "))
# print("Step 3:", beatles)
# # step 4
# del beatles[-1]
# del beatles[-1]
# print("Step 4:", beatles)
#
# # step 5
# beatles.insert(0, "Ringo Starr")
# print("Step 5:", beatles)
#
#
# # testing list legth
# print("The Fab", len(beatles))

# A lista é um tipo de dados em Python usada para armazenar vários objetos.
# É uma coleção ordenada e mutável de ítens separados por vírgulas, entre parêntesis retos

#bubblesort

print("Bubble Sort")


my_list = [8, 10, 6, 2, 4]

swapped = True

while swapped:
  print(my_list)  
  swapped = False
  for i in range(len(my_list) - 1):
    if my_list[i] > my_list[i + 1]:
      swapped = True
      my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

# my_list = []
# swapped = True
# num = int(input("How many elements do you want to sort: "))

# for i in range(num):
#     val = float(input("Enter a list element: "))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nSorted: ")
# print(my_list)

print("Python native sort: ")
my_list = [8,10,6,2,4]
my_list.sort()
print(my_list)

print("Reverse list: ")
my_list.reverse()
print(my_list)

#procedimentos do python de listas, alteram a lista inicial


##listas podem ser passadas por referencia, diferente de variaveis comuns que sao passadas por valor

# o nome de uma variavel comum eh o nome do seu coteudo

#o nome de uma lista e o nome de um local de memoria onde a lista e armazenada, a copia da copia ainda eh apenas uma copia

list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

# list_2 = list_1 copia o nome da referencia e não o conteudo

print("Slice")

# solucao para copiar valores
# slice [start:end(non-inclusive)]

# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# pode usar valores negativos do slice

print("Slice negativo")

my_list = [10,8,6,4,2]
new_list = my_list[1:-1]
print(new_list)

my_list = [10,8,6,4,2]
new_list = my_list[-1:1]
print(new_list)

# omitir o start do slice, assume que inicia do 0
# se omitir o end do slice, assume que termina no ultimo elemento

#utilizar del com slices

print("Del com slices")

my_list = [1,2,3,4,5,6]
del my_list[1:3]
print(my_list)
del my_list[:]
print(my_list)
del my_list
# del deleta a referencia para a lista
# print(my_list) - gera erro de runtime

print("in e not in")
# funciona como no SQL

# in - verifica se existe dentro da lista
# not in - verifica se não existe na lista

# in e not in retornam booleanos

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

# challenge

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#

my_list.sort()
set = []

for i in range(len(my_list)):
  if my_list[i] not in set:
    set.append(my_list[i])

print("The list with unique elements only:")
print(set)

## List comprehension

squares = [x ** 2 for x in range(10)]

print(squares)

twos = [2 ** i for i in range(8)]

print(twos)

odds = [x for x in squares if x % 2 != 0]

print(odds)

print("Tabuleiro")

EMPTY = "-"
ROOK = "ROOK"
board = []

# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)

board = [[EMPTY for i in range(8)] for j in range(8)]

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)

print("Meteorologia")
# meteorologia
temps = [[0.0 for h in range(24)] for d in range(31)]

print(temps)

total = 0.0
for day in temps:
  total += day[11]
average = total / 31
print("Average temperature at noon:",average)

i=2
while i >= 0:
  print("*")
  i-=2

for i in range(-1,1):
  print("#")

print(10 > 0 or 10 == 0)

l = [0,1,2]
# l[-1] = l[-2]
# print(l)

l[0], l[1] = l[1],l[2]
print(l)

n = []
h = n
h.append(1)

print(n,h)

print([0 for i in range(1,3)])

i = [0,1,2,3]
x = 1

for el in i:
  x *= el
print(x)

a = [1,2,3]
b = []

for v in a:
  b.insert(0,v)
print(b)

l =[3,1,-2]
l.insert(0,1)
del l[1]
print(l)

for i in range(1):
  print("y")
else:
  print("y")

print(l[l[-1]])

t = [[3-1 for i in range(3)] for j in range(3)]
s = 0

for i in range(3):
  s+=t[i][i]
print(s)

i = 0
while i<=3 :
  i+=2
  print("*")

nums=[1,2,3]
vals=nums[-1:-2]
print(nums,vals)

var = 0
while var < 6:
  var += 1
  if var % 2 == 0:
    continue
  print("#")

print(0 < 10 and 10 > 0 or 0 > 10 and 10 < 0)

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

print(c + d + e)

var =1 
while var < 10:
  print("$")
  var = var << 1

i = 0
while i<=5:
  i+=1
  if i %2 ==0:
    break
  print("*")

m = [[0,1,2,3] for i in range(2)]

print(m[0][2])

nums = [1,2,3]
vals =nums
del vals[1:2]

print(nums,vals)

x = 1
x = x == x
print(x)

l = [0,1,2]
l[0], l[2] = l[2], l[0]
print(l)
print(len([i for i in range(-1,2)]))

print([i for i in range(-1,2)])

my = [1,2,3]
for v in range(len(my)):
  my.insert(1,my[v])
print(my)


m = [1,2,3,4]
print(m[-3:-2])

