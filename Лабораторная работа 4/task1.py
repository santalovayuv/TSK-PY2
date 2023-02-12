class Film:
    def __init__(self, name: str, dur: int):
        """
        Создание объекта класса фильм
        :param name: название фильма
        :param dur: длительность фильмаа (в минутах)

        Примеры:
         >>> test_film = Film("Бросок кобры", 118)
         """
         self.name = name
         self.duration = dur
         self._comm = None
         self._accordance = None

    def add_comm(self, message: str):
        """
        Метод, позволяющий оставить комментарий к фильму
        :param message:
        :return:

        Примеры:
        >>> test_film = Film("Бросок кобры", 118)
        >>> test_film.add_comm("Военно-фанатстический боевик")
        """
        self._comm = message

    def write_com(self):
        """
        Метод, позволяющий вернуть ранее оставленный комментарий к фильму
        :return: возвращает комментарий

        Примеры:
        >>> test_film = Film("Бросок кобры", 118)
        >>> test_film.add_comm("Военно-фанатстический боевик")
        >>> test_film.write_com()
        'Военно-фанатстический боевик'
        """
        return self._comm

    def add_accordance(self, rating: float):
        """
        Метод, позволяющий добавить степень соответствия фильму теме
        :param rating: степень соответствия фильма теме (от 0 до 10)

        Примеры:
        >>> test_film = Film("Бросок кобры", 118)
        >>> test_film.add_accordance(9.)
        """

        if isinstance(rating, float):
            if 10. >= rating >= 0.:
                self._accordance = rating
            else:
                raise ValueError("accordance must be from 0 to 10")
        else:
            raise TypeError("accordance must be float")

    def check_accordance(self):
        """
        Метод, печатающий степень соответствия фильма теме. Предварительно необходимо добавить её к экземпляру класса

        Примеры:
        >>> test_film = Film("Бросок кобры", 118)
        >>> test_film.add_accordance(9.)
        >>> test_film.check_accordance()
        Соответствие фильма теме:9.0
        """
        print(f'Соответствие фильма теме:{self._accordance}')


    @property
    def duration(self):
        """
        Геттер для атрибута (длительности) фильма
        :param self:
        :return:
        """
        return self._duration

    @duration.setter
    def duration(self, dur: int):
        """
        Cеттер для атрибута (длительности) фильма
        :param self:
        :param dur: длительность фильма
        :return:
        """
        if isinstance(dur, int):
            if dur > 0:
                self._duration = dur
            else:
                raise ValueError(f'duration of film must be greater than zero, while incoming {dur}')
        else:
            raise ValueError(f'film duration must be int, while incoming is {type(dur)}')


    def __str__(self):
        """
        Магический метод __str__
        :return: Возвращает название и длительность фильма
        Примеры:
        >>> test_film = Film("Бросок кобры", 118)
        >>> print(test_film)
        Фильм "Альфа Центавра", длительность 118
        """
        return f'Фильм "{self.name}", длительность {self.duration}'

    def __repr__(self):
        """
        Магический метод, выдающий строку, необходимую для инициализации фильма
        :return:

        Примеры:
        >>> test_film = Film("Бросок кобры", 118)
        >>> repr(test_film)
        "Film(name='Бросок кобры', dur=118)"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, dur={self.duration})"


class HistoricalFilm(Film):
    def __init__(self, name: str, dur: int, century: str):
        """
        Создание объекта класса исторический фильм
        :param name: название фильма
        :param dur:  длительность фильма
        :param century: век, события которого описывает фильм (римские цифры)

        Примеры:
        >>> test_film = HistoricalFilm("Битва за Севастополь", 122, "XXI")
        """
        super().__init__(name, dur)
        self.century = century
        self._comm = None
        self._accordance = None

    def __str__(self):
        """
        Магический метод __str__
        :return: Возвращает название и длительность фильма

        Примеры:
        >>> test_film = HistoricalFilm("Битва за Севастополь", 122, "XX")
        >>> print(test_film)
        Исторический Фильм "Битва за Севастополь", длительность 122, XX век
        """
        return f'Исторический Фильм "{self.name}", длительность {self.duration}, {self.century} век'

    def __repr__(self):
        """
        Магический метод, выдающий строку, необходимую для инициализации исторического фильма
        :return:

        Примеры:
        >>> test_film = HistoricalFilm("Битва за Севастополь", 122, "XX")
        >>> print(repr(test_film))
        HistoricalFilm(name='Битва за Севастополь', dur=122, century = XX)
        """
        return f"{self.__class__.__name__}(name={self.name!r}, dur={self.duration}, century = {self.century})"

    def check_accordance(self):
        """
        Метод, печатающий степень исторического соответствия фильма, ранее добавленную
        методом add_accordance
        Примеры:
        >>> test_film = HistoricalFilm("Битва за Севастополь", 122, "XX")
        >>> test_film.add_accordance(7.5)
        >>> test_film.check_accordance()
        Степень исторического соответствия:7.5
        """
        print(f'Степень исторического соответствия:{self._accordance}')

if __name__ == "__main__":
    # Write your solution here
    """
    Унаследованы методы add_accordance, add_comm и write_comm. Метод check_accordance перегружен
    Возможные проверки на соответствие века формату цифр опущены, так как век может быть указан
    с модификатором до н.э или н.э.
    """
    pass

