# encoding:utf-8

from datetime import datetime, timedelta
from dummy import Flow, Dummy, steps, get_out_queue

flow = Flow()

# temps de travail
Working_time = 30


class MakeMyCodeDreamsTrue:

    def __enter__(self):
        """
        quand tu utilise le context manager, tu permet une initialisation, tu peux modifier des fonctions,
        des classes, d'autres contextes... etc. mais tu peux aussi simplement initialiser des variables
        ou just le manager, le manager c'est littéralement ce que retourne __enter__ tout simplement
        :return:
        """

        [flow.process_event.put(ele) for ele in steps]
        # initialise une variable de statut
        self.step = None

        def inner():
            nonlocal self
            the_end = datetime.now() + timedelta(seconds=Working_time)

            while True:
                # indication de la fin : condition de temp dépassée ET information non passée encore
                if datetime.now() > the_end and get_out_queue.empty():
                    get_out_queue.put(Ellipsis)

                # indication de fin de programme : alert fin donnée ET dernière étape d'un cycle passée.
                if not get_out_queue.empty() and self.step is steps.four:
                    break

                # réinitialisation d'un cycle, si la queue est vide ou à la dernière étape, on refait le plein
                if self.step is steps.four or None:
                    [flow.process_event.put(ele) for ele in steps]

                # passage à l'étape suivante
                self.step = flow.process_event.get()

                yield True

            self.__exit__(StopIteration, 0, None)

        manager = inner()

        return manager

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        action à faire lorsqu'on sort du contexte.

        :return:
        """

    def main(self):
        """
        Fonction d'exécution; ici pour sortir de la boucle, on va utiliser le temps, ce paramètre peut
        etre assez facilement changé.

        La fonction fonctionne comme suit:
            - la classe utilise son propre contexte. Elle génère un générateur, qui lui même génère un True à chaque
              tour tant qu'on ne lui a pas dit d'arreter
            - on fait un switcher, un dict qui contient en clé un objet évenement, et en valeur la fonction. On
              le laisse appeler la fonction en fonction de la clé fourni.

        Le context manager contient pour chaque tour l'algo technique:
            - comment passer d'une étape à une autre
            - que faire à la fin d'un cycle
            - la vérification de l'alerte d'arrêt
            - la génération de variables en fonction de la situation (heure de fin dans ce cas)

        Par conséquent, cette structure est plus complexe qu'une simple boucle, mais permet de totalement séparer
        le métier de la technique, qu'importe ce que l'on met dans la liste des étapes, qu'importe l'ordre des étapes
        qu'importe le moment d'arrêt : les actions à faire seront placées ici, toujours séparé des regles de contexte.
        La liste des étapes sera toujours du coté où sont codé les étapes, mais à part, et la regle de gestion de
        l'application n'a au final rien à voir avec le contenu de l'application.

        :return:
        """
        dummy = Dummy()

        # on fait un switch case pour lister tour à tour les étapes en fonction de l'identité de step
        switcher = {
            steps.one: dummy.work_hard,
            steps.two: dummy.play_hard,
            steps.three: dummy.danse_on_the_floor,
            steps.four: dummy.sleep
        }


        # le contexte tourne en générateur, il produit True tant qu'il existe, s'il n'existe plus
        # on sort alors de la boucle, puis du contexte.
        with self as manager:
            for _ in manager:
                switcher[self.step]()
            print("time out buddy!")


if __name__ == '__main__':
    MakeMyCodeDreamsTrue().main()
