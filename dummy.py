# encoding:utf-8
from utils.meta import Singleton
from queue import Queue
from collections import namedtuple
from time import sleep

Step = namedtuple("Step", "one two three four")



# pour gérer l'identité d'un marqueur on peut utiliser une instance de base object. Cette instance a sa
# propre identité mémoire, et on peut vérifier son identité par "is". Au final "object" est l'instance minimale
# dans python, donc l'utiliser, c'est optimiser le code et l'espace.
steps = Step(object(), object(), object(), object())
get_out_queue = Queue(maxsize=1)

# il y a 2 singletons de base dans Python, None et Ellipsis. None a une fonction très utilisée, mais Ellispsis
# est moins courant (pour gérer les paramètres), bref, on peut se servir d'Ellipsis comme killer

class Flow(metaclass=Singleton):
    """
    Classe contenant le flux. Singleton
    """

    def __init__(self):
        # Une queue est un outil de pile qui peut passer au travers du threading et de diverses classes
        # Dans le cas d'une suite d'évenement, on peut identifier le contenu en ayant l'assurance qu'il ne
        #  sera extrait qu'une seule fois
        self.process_event = Queue()


class Dummy:
    """
    Classe bidon contenant des opérations à faire durant un cycle
    """

    def danse_on_the_floor(self):
        print("3 I love Lady Gaga, I promess")
        sleep(2)

    def work_hard(self):
        print("1 My boss is a Dumb")
        sleep(2)

    def play_hard(self):
        print("2 Fallout is my religion")
        sleep(2)

    def sleep(self):
        print("4 Even Chuck Norris sleep sometimes")
        sleep(2)