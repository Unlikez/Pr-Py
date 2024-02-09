import doctest


class Juice:
    """
    Документация на класс
    Класс описывает модель Сока
    """
    def __init__(self, volume: float, drunk: float, pack: float) -> float:
        """Проверка аргументов на допустимость значений"""

        if not isinstance(bottle, float):
            raise TypeError("объем упаковки должен быть вещественным числом")
        if pack < 0:
            raise ValueError("объем упаковки должен быть положительным числом")
        self.pack = pack

        if not isinstance(volume, float):
            raise TypeError("объем сока должен быть вещественным числом")
        if volume < 0 or volume > bottle:
            raise ValueError("объем сока должен быть положительным числом или не больше объема упаковки")
        self.volume = volume

        if not isinstance(drunk, float):
            raise TypeError("объем выпитого сока должен быть вещественным числом")
        if drunk < 0:
            raise ValueError("объем выпитого сока должен быть положительным числом")
        self.drunk = drunk

    """Метод выпитый объем"""
    def drunk_volume(self):
        """
        return:
        volume = drunk_volume()
        """
        ...

    """Метод оставшегося объема"""
    def ostatoc_volume(self):
        """
        return:
        ostatoc = ostatoc_volume()
        """
        ...

class Market:
    """
    Документация на класс
    Класс описывает модель Рынка
    """
    def __init__(self, fructs: int, vegetables: int) -> int:
        """Проверка аргументов на допустимость значений"""

        if not isinstance(fructs, int):
            raise TypeError("количество фруктов должно быть целым числом")
        if fructs < 0:
            raise ValueError("количество фруктов должно быть положительным числом")
        self.fructs = fructs

        if not isinstance(vegetables, int):
            raise TypeError("количество овощей должно быть целым числом")
        if vegetables < 0:
            raise ValueError("количество овощей должно быть положительным числом")
        self.vegetables = vegetables

    """ Метод количества фруктов при определенном изменении их числа в рынка"""
    def count_fructs(self):
        """
        return:
        count_f = count_fructs()
        """
        ...

    """ Метод количества овощей при определенном изменении их числа в рынка"""
    def count_vegetables(self):
        """
        return:
        count_o = count_vegetables()
        """
        ...


class Man:
    """
    Документация на класс
    Класс описывает модель человека
    """
    def __init__(self, height: float, mass: float) -> float:

        """Проверка аргументов на допустимость значений"""

        if not isinstance(height, float):
            raise TypeError("рост человека должен быть вещественным числом")
        if height <= 0:
            raise ValueError("рост человека должен быть положительным числом")

        """Инициализация экземпляра класса"""
        self.height = height

        if not isinstance(mass, float):
            raise TypeError("вес человека должен быть вещественным числом")
        if mass <= 0:
            raise ValueError("вес человека должен быть положительным числом")
        self.mass = mass

    """Метод увеличение роста человека"""
    def uvelichenie_rosta(self):
        """
        return:
        rost = yvelichenie_rosta()
        """
        ...

    """Метод изменения веса человека"""
    def izmenenie_vesa(self):
        """
         return:
        ves = izmenenie_vesa()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()