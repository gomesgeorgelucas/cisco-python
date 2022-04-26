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


for i in range(100):
    # do_something()
    pass