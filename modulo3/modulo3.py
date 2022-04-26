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