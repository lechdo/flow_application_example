# encoding:utf-8

class Singleton(type):
    """
    Meta class, permet d'isoler le principe du singleton à toutes les classes qui hériterons.

    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
