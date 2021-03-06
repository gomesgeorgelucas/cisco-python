
# functions tuples dictionaries and data processing

# Isto leva-nos diretamente à terceira condição: se vai dividir # o trabalho entre vários programadores, decomponha o problema
# para permitir que o produto seja implementado como um conjunto # de funções escritas em separado, embaladas em diferentes módulos.
# Precisa de pelo menos uma instrucao no corpo da funcao.

# def function_name():
# function body

def message():
    print("Enter a value: ")


print("We start here.")
message()
print("We end here.")

# Não se deve ter uma função e uma variável com o memo nome
# funções incorporadas, funções de módulos pré instalados,
# funções definidas pelo programador e funções lambda

# def function(parameter1, parameter2,..,parameterN):
# function body

# É válido e possível ter uma variável no script com nome de
# algum parâmetro de uma função, afinal o parâmetro só existe
# dentro do escopo da função

# sombreamento

number = 123  # ofuscado


def fun():
    number = 321  # ofuscado, var de mesmo nome
    print(number)


fun()

number = 123


def fun():
    print(number)  # vai acessar number global


fun()


# parametros passados e atribuidos em ordem são chamados de parâmetros posicionais e a passagem de passagem de parâmetrop posicional

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)


introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")


# Argumentos de Keyword, é quando passamos argumentos especificando o [nome do argumento = parametro], a posição deles não importa contanto que estejam corretos

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)


introduction(first_name="Skywalker", last_name="Luke")
introduction(last_name="Quick", first_name="Jesse")
introduction("Kent", "Clark")


# a regra para misturar argumentos posicionais com keyword
# é sempre colocar posicionais antes de keyword

def adding(a, b, c):
    print(a + b + c)


adding(3, c=1, b=2)


# adding(c=1,3,b=2) -> erro
# adding(a, a =1, b = 2) -> erro, a já foi atribuido de forma posicional

# valores padrão de parametros em argumentos
def fun(arg1="arg1"):
    print(arg1)


fun()
fun("arg2")

# erro, depois de um argumento padrão, todos devem ser padrão
# def fun2 (a,b=2,c):
#   print(a+b+c)

# utiliza-se return para terminar funções

# valor nulo: None (e é uma keyword)

value = None
if value is None:
    print("Value is none")

# quando a função não retorna nada ou não atinge o return esperado, retorna None
# em Python é possível que a função tenha um return que só é
# atingido dada uma condição, visto que o retorno não é obrigatório
# e não há como expressá-lo
# dessa forma se a função acabar sem atingir algum ponto de
# return, ela retorna None

print("Leap year again")


def is_year_leap(year):
    #
    # put your code here
    #
    if (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True
    else:
        return False


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

print("Leap year modified")


def days_in_month(year, month):
    if (year < 1528 or (month < 1 or month > 12)):
        return None

    if is_year_leap(year):
        if month == 2:
            return 29
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31
    else:
        if month == 2:
            return 28
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


def day_of_year(year, month, day):
    if (day < 1 or day > 31):
        return None
    if (day > days_in_month(year, month)):
        return None

    days_count = 0

    for ano in range(1528, year + 1):
        if is_year_leap(year):
            days_count += 366
        else:
            days_count += 365

    days_count += day
    day_of_week_index = days_count % 7

    return day_of_week_index


print(day_of_year(2022, 4, 25))
print(day_of_year(2000, 12, 31))


##Funcionou de primeira, absurdo!

# fazer primo
def is_prime(num):
    #
    # Write your code here.
    #
    # TODO
    return True


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()


# Em python se uma variavel for decladara depois da função e for acessada dentro da função, ela pode achar a variável pois a mesma é global - isso se não for ofuscada/sombreada por uma variavel de mesmo nome como parametro ou de escopo interno da função

def a():
    print(x)


x = "here"
a()


# Keyword global - ao utilizar a instrução global antes do nome da variavel, ela define que estamos utilizando a variavel global (de fora da função)


def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)


# global também aceita nomes de variáveis, separados por virgulas
def auau():
    global var1, var2, var3
    print(var1, var2, var3)


var1, var2, var3 = 0, 1, 2
auau()


# o global faz com que ao invés de criar
# a variável dentro da função ele acessa
# a variável global preexistente fora
# da função

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

# ou seja, se você passar a referencia de uma lista como parametro, e utilizar qualquer operação/intrução que altere a lista e não a referencia, isso se propaga para a lista original.


# recursividade

# def fib(n):
#     if n < 1:
#          return None
#     if n < 3:
#         return 1

#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum

# funções recursivas consomem muita memória


print("fib recursivo")


def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


for n in range(1, 10):
    print(n, "->", fib(n))

print("fat recursivo")


def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)


print(factorial_function(10))

# sequencias e mutabilidade

# uma sequencia é um dado que pode ser analisado pelo
# loop for

# lista é um exemplo de sequencia

# dois tipos de dados -mutáveis e imutáveis
# mutáveis - podem ser alterados livremente (in situ - latim para no local)

# dados imutaáveis não podem ser modificados dessa maneira - para adicionar um elemento por exemplo, é necessário fazer uma cópia da imutável e adicionar o novo elemento na cópia

# o nome da lista imutável é tuple

# diferentes de listas normais [], tuples usam parenteses () e tem valores separados por viírgulas

# tuples não podem ser modificados in situ

# tb pode-se criar tuples omitindo os parenteses

# tuple = (1,2,3)
# tuple2 = 1,2,3

# assim como as listas, tuples podem conter qualquer
# tipo de dados e são heterogeneas

tupla_vazia = ()

# para criar uma tuple de 1 elemento, é preciso terminar com virgula, para diferencias de um escalar

tuple_um_elemento = 1,

# leitura da tuple é identica a da lista

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

## tentar modificara tuple com del, append, insert etc, causará um erro
# voce pode somar tuples com +, utilizar in ou not in, multiplicar tuples com *

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

# Uma das propriedades mais úteis da tuple é a sua capacidade de aparecer no lado esquerdo do operador de atribuição. Viu este fenómeno há algum tempo, quando foi necessário encontrar uma ferramenta elegante para trocar os valores de duas variáveis.

var = 123

t1 = (1,)
t2 = (2,)
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

# importante, os elementos das tuplas quando criados
# podem ser variáveis

# Além disso, podem ser expressões se estiverem no lado direito do operador de atribuição.


# dicionarios
# é uma estrutura de dados mutável, não sequencial

# estrutura de key : value
# a chave é única
# chave pode ser qualquer tipo de objeto imutável
# chave não pode ser listas
# instrucao len() devolve o comprimento de dicionário, ou seja a quantidade de elementos key:value

# é uma ferramenta de sentido único key -> value!
print("")

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

# modelo dict -> { key1 : value, key2 : value}

# a ordem de acesso ou impressão de todos os dados do dicionário é aleatória, afinal não são sequencias
# estão fora do nosso controle

# NOTA! : no python 3.6x os dicionários tornaram-se
# coleções ordenadas por padrão, dependendo da versão o comportamento de exibição automático pode mudar

print(dictionary['cat'])
print(phone_numbers['Suzy'])

# acesso similar ao de arrays
# print(phone_numbers['inexistent']) throws runtime error, utilizar in ou not in para verificar antes

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

# Example 1:
dictionary = {
    "cat": "chat",
    "horse": "cheval",
    "dog": "chien",
}

# Example 2:
phone_numbers = {'boss': 5551234567,
                 'Suzy': 22657854310
                 }

# Tais formas de formatação de código são chamadas hanging indents (indentações penduradas).
# keys() do dicionário retorna uma lista iteravel de chaves e podemos usar o for
print("Keys")
for key in dictionary.keys():
    print(key, "->", dictionary[key])

# sorted() é uma função que opera em dicionários e pode ser usada no for
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])

# items() da lista retorna tuplas de chave : valor
# for elemento1, elemento2 in dictionary.items():

for english, french in dictionary.items():
    print(english, "->", french)

# values() do dict retorna os valores, de maneira similar ao keys(), uma lista iteravel de valores
for french in dictionary.values():
    print(french)

# Como o dicionário não consegue encontrar automaticamente uma chave para um determinado valor,
# o papel deste método é bastante limitado.
# Dicionários são mutáveis

dictionary["cat"] = "minou"
print(dictionary)
dictionary["nova_chave"] = "novo_valor"
print(dictionary)

# Também pode inserir um item num dicionário utilizando o método update() , por exemplo:
dictionary.update({"duck": "canard"})
print(dictionary)

# quando removemos a chave, removemos o valor junto

del dictionary['dog']
print(dictionary)

# Para remover o último item num dicionário, pode-se utilizar o método popitem() :
dictionary.popitem()
print(dictionary)

# Nota!! - Nas versões mais antigas do Python, ou seja, antes do 3.6.7,
# o método popitem() remove um item aleatório de um dicionário.

# school_class = {}
#
# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
#
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
#         break
#
#     if name in school_class:
#         school_class[name] += (score,)  # Alongar a tuple caso o nome já esteja na lista
#     else:
#         school_class[name] = (score,)  # novo aluno, nova tuple
#
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)

# print(school_class)

# tuplas podem ser deletadas

# Também pode criar um tuple usando uma função Python incorporada chamada tuple()

my_tuple = tuple((1, 2, "string"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list)  # outputs: [2, 4, 6]
print(type(my_list))  # outputs: <class 'list'>
tup = tuple(my_list)
print(tup)  # outputs: (2, 4, 6)
print(type(tup))  # outputs: <class 'tuple'>

# Da mesma forma, quando se pretende converter um iterável numa lista,
# pode-se usar uma função Python integrada chamada list():
tup = 1, 2, 3,
my_list = list(tup)
print(type(my_list))  # outputs: <class 'list'>

# e quiser aceder a um item de dicionário, pode fazê-lo fazendo referência à
# sua chave dentro de um par de parêntesis retos (ex. 1) ou usando o método get() (ex. 2):

pol_eng_dictionary = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil"
}

item_1 = pol_eng_dictionary["gleba"]  # ex. 1
print(item_1)  # outputs: soil

item_2 = pol_eng_dictionary.get("woda")
print(item_2)  # outputs: water

# Para remover todos os itens do dicionário, é necessário utilizar o clear() método:

pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
}

print(len(pol_eng_dictionary))  # outputs: 3
del pol_eng_dictionary["zamek"]  # remove an item
print(len(pol_eng_dictionary))  # outputs: 2

pol_eng_dictionary.clear()  # removes all the items
print(len(pol_eng_dictionary))  # outputs: 0

del pol_eng_dictionary  # removes the dictionary

# Para copiar um dicionário, use o copy() método:

pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
}

copy_dictionary = pol_eng_dictionary.copy()

# descompactação de tuples em variáveis

tup = 1, 2, 3
a, b, c = tup

print(a * b * c)

#  count() acha a quantidade de items que casam com o seu parametro na tuple

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

# tuple() converte para tuples, em caso de dicts, automaticamente converte chaves, se quiser valores,
# precisa especifica com dict.values()

print(duplicates)  # outputs: 4

print(tuple(copy_dictionary.values()))

print("prova")

