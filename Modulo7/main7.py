class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())


# Tal componente é chamado público, pelo que não se pode começar o seu nome com dois
# (ou mais) underscores. Há mais um requisito - o nome não deve ter mais do que um
# underscore à direita. Uma vez que nenhum underscore à direita satisfaz totalmente o requisito,
# pode-se assumir que o nome é aceitável.

# self
# Isto significa que um método é obrigado a ter pelo menos um parâmetro,
# que é utilizado pelo próprio Python - não tem qualquer influência sobre ele.

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0


# Uma tal abordagem tem algumas consequências importantes:
#
# objetos diferentes da mesma classe podem possuir conjuntos diferentes de propriedades;
# deve haver uma forma de verificar com segurança se um objeto específico possui a propriedade
# que pretende utilizar (a menos que queira provocar uma exceção - vale sempre a pena considerar)
# cada objeto carrega o seu próprio conjunto de propriedades - eles não interferem uns
# com os outros de forma alguma.
# Tais variáveis (propriedades) são chamadas variáveis de instância.

class ExampleClass:
    def __init__(self, val=1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5  # cria nova var de instancia

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)


# Os objetos Python, quando criados, são dotados de um pequeno conjunto de propriedades
# e métodos pré-definidos. Cada objeto tem-nos, quer os queira ou não.
# Um deles é uma variável chamada __dict__ (é um dicionário).

class ExampleClass:
    def __init__(self, val=1):
        self.__first = val

    def set_second(self, val=2):
        self.__second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)


# var de classes

class ExampleClass:
    counter = 0

    def __init__(self, val=1):
        self.__first = val
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
print(example_object_1.__dict__, example_object_1.counter)
example_object_2 = ExampleClass(2)
print(example_object_2.__dict__, example_object_2.counter)
example_object_3 = ExampleClass(4)
print(example_object_3.__dict__, example_object_3.counter)


# vriavél de classo pode se assemelhar ao static

class ExampleClass:
    varia = 1

    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print(example_object.__dict__)


# O Python fornece uma função capaz de verificar com segurança se algum objeto/classe
# contém uma propriedade especificada. A função é chamada hasattr,
# e espera que lhe sejam transmitidos dois argumentos:
#
# A classe ou o objeto a ser verificado;
# o nome da propriedade cuja existência tem de ser comunicada
# (nota: tem de ser uma string contendo o nome do atributo, e não apenas o nome)
# A função devolve True ou False.


class ExampleClass:
    a = 1

    def __init__(self):
        self.b = 2


example_object = ExampleClass()

print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))


class Classy:
    pass


print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)


class Classy:
    pass


print(Classy.__module__)
obj = Classy()
print(obj.__module__)


class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


# Nota: uma classe sem superclasses
# explícitas aponta para o objeto (uma classe Python predefinida) como seu antepassado direto.

def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


# Nota: apenas as classes têm este atributo - os objetos não o têm.

printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)


# introspeção, que é a capacidade de um programa para examinar o tipo
# ou propriedades de um objeto em runtime;
# reflexão, que vai um passo além, e é a capacidade de um programa para
# manipular os valores, propriedades e/ou funções de um objeto em runtime.

class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)


# issubclass(ClassOne, ClassTwo)
# pode verificar se uma determinada classe é uma subclasse de qualquer outra classe.

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()


# Há uma observação importante a fazer: cada classe é considerada como uma subclasse de si mesma.

# Herança: isinstance()
# Como já sabe, um objeto é uma incarnação de uma classe.
# Isto significa que o objeto é como um bolo cozido utilizando uma receita que
# está incluída dentro da classe.

# Herança: o operador is .
# Há também um operador Python que vale a pena mencionar,
# pois refere-se diretamente a objetos - aqui está ele:

# Não se esqueça que as variáveis não armazenam os objetos em si,
# mas apenas os manípulos que apontam para a memória interna do Python.

# Atribuir um valor de uma variável de objeto a outra variável não copia
# o objeto, mas apenas o seu manípulo. É por isso que um operador como
# is pode ser muito útil em circunstâncias particulares.


class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2, string_1 is string_2)


# super() método de subclasse que acessa a superclasse
# Nota: pode utilizar este mecanismo não só para invocar
# o construtor da superclasse, mas também para ter acesso a qualquer
# um dos recursos disponíveis dentro da superclasse.

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


obj = Sub("Andy")

print(obj)


# Quando se tenta aceder à entidade de qualquer objeto, o Python tentará (por esta ordem):
#
# encontrá-lo dentro do próprio objeto;
# encontrá-lo em todas as classes envolvidas na linha de herança do objeto, de baixo para cima;
# Se ambos os itens acima falharem, uma exceção (AttributeError) é levantada.

# Python suporta herança múltipla

class SuperA:
    var_a = 10

    def fun_a(self):
        return 11


class SuperB:
    var_b = 20

    def fun_b(self):
        return 21


class Sub(SuperA, SuperB):
    pass


obj = Sub()

print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())


# Agora é tempo de introduzir um termo completamente novo - overriding.

class Level1:
    var = 100

    def fun(self):
        return 101


class Level2(Level1):
    var = 200

    def fun(self):
        return 201


class Level3(Level2):
    pass


obj = Level3()

print(obj.var, obj.fun())


# A entidade definida mais tarde (no sentido da herança)
# sobrepõe-se à mesma entidade definida mais cedo.
# Podemos também dizer que o Python procura uma entidade de baixo para cima,
# e está plenamente satisfeito com a primeira entidade do nome desejado.

class Left:
    var = "L"
    var_left = "LL"

    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"

    def fun(self):
        return "Right"


class Sub(Left, Right):
    pass


obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())


# Podemos dizer que o Python procura componentes de objeto na seguinte ordem:
#
# dentro do próprio objeto;
# nas suas superclasses, de baixo para cima;
# se houver mais do que uma classe num determinado caminho de herança,
# o Python analisa-os da esquerda para a direita.


class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it from Two")


one = One()
two = Two()

one.doanything()
two.doanything()

# Nota: a situação em que a subclasse é capaz de modificar o seu comportamento
# de superclasse (tal como no exemplo) é chamada polimorfismo.

import time


class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)


# O que é o Method Resolution Order (MRO) e porque é que nem todas as heranças fazem sentido?

class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()


# MRO, em geral, é uma forma (pode-se chamar-lhe uma estratégia) em que uma determinada
# linguagem de programação analisa a parte superior da hierarquia de uma classe, a fim de encontrar
# o método de que ela necessita atualmente. Vale a pena salientar que línguas diferentes
# utilizam ligeiramente (ou mesmo completamente) diferentes MROs.
# O Python é uma criatura única a este respeito, contudo, e os seus costumes são
# um pouco específicos.

# o codigo abaixo quebra pq não á m_middle em Top nem em Bottom

# class Top:
#     def m_top(self):
#         print("top")
#
#
# class Middle(Top):
#     def m_middle(self):
#         print("middle")
#
#
# class Bottom(Top, Middle):
#     def m_bottom(self):
#         print("bottom")
#
#
# object = Bottom()
# object.m_bottom()
# object.m_middle()
# object.m_top()

# Algumas linguagens de programação proíbem a herança múltipla, e como consequência,
# não o deixam construir um diamante - esta é a rota que Java e
# C# escolheram seguir desde as suas origens.
# O Python, contudo, escolheu uma rota diferente - permite herança múltipla, e não se
# importa se escrever e executar um código como o que está no editor.
# Mas não se esqueça do MRO - é sempre ele que manda.

class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()

print()
print("Estrutura diamante")


class Top:
    def m_top(self):
        print("top")


class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")


class Bottom(Middle_Left, Middle_Right):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()


# 1. Um método chamado __str__() é responsável pela conversão do conteúdo de um
# objeto numa string (mais ou menos) legível. Pode redefini-la se
# quiser que o seu objeto se possa apresentar de uma forma mais elegante. Por exemplo:

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        return None
    else:
        print("Everything went fine")
        return n


print(reciprocal(2))
print(reciprocal(0))


# Nota: estas duas variantes (else e finally) não são de modo algum dependentes,
# e podem coexistir ou ocorrer independentemente.

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
        return n


print(reciprocal(2))
print(reciprocal(0))

# ezxceptions as classes

try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())


# Nota: o scope do identificador  (as e) abrange o seu ramo except ,
# e não vai mais longe.

def print_exception_tree(thisclass, nest=0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)


# custom exceptions

def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))


try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

try:
    raise Exception("my exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

try:
    raise Exception("my", "exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)


# custom exception ZeroDiv

class MyZeroDivisionError(ZeroDivisionError):
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:
        raise ZeroDivisionError("some bad news")


for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('Division by zero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('My division by zero')
    except ZeroDivisionError:
        print('Original division by zero')

print("custom errors pizza\n")


class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)


#  sintaxe except Exception_Name as an exception_object:
#  permite-lhe interceptar um objeto portador de informação sobre uma exceção pendente.
#  A propriedade do objeto chamada args (um tuple) armazena todos os argumentos passados
#  para o construtor do objeto.