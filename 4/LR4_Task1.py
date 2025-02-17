class Transport:
    """
    Базовый класс для всех транспортных средств.

    Атрибуты:
        _brand (str): Марка транспортного средства.
        _model (str): Модель транспортного средства.
        _year (int): Год выпуска.
        _speed (float): Текущая скорость транспортного средства.
    """

    def __init__(self, brand: str, model: str, year: int, speed: float = 0.0):
        """
        Конструктор базового класса Transport.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска.
        :param speed: Текущая скорость (по умолчанию 0.0).
        """
        self._brand = brand
        self._model = model
        self._year = year
        self._speed = speed

    @property
    def brand(self) -> str:
        """Возвращает марку транспортного средства."""
        return self._brand

    @property
    def model(self) -> str:
        """Возвращает модель транспортного средства."""
        return self._model

    @property
    def year(self) -> int:
        """Возвращает год выпуска транспортного средства."""
        return self._year

    @property
    def speed(self) -> float:
        """Возвращает текущую скорость транспортного средства."""
        return self._speed

    @speed.setter
    def speed(self, value: float) -> None:
        """
        Устанавливает текущую скорость транспортного средства.
        Скорость не может быть отрицательной.
        """
        if value < 0:
            raise ValueError("Скорость не может быть отрицательной.")
        self._speed = value

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строка с описанием транспортного средства.
        """
        return f"{self._brand} {self._model} ({self._year}), текущая скорость: {self._speed} км/ч"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        :return: Формальная строка с описанием транспортного средства.
        """
        return f"Transport(brand={self._brand}, model={self._model}, year={self._year}, speed={self._speed})"

    def accelerate(self, increment: float) -> None:
        """
        Увеличивает скорость транспортного средства на заданное значение.

        :param increment: Величина увеличения скорости.
        """
        self.speed += increment

    def brake(self, decrement: float) -> None:
        """
        Уменьшает скорость транспортного средства на заданное значение.

        :param decrement: Величина уменьшения скорости.
        """
        self.speed = max(0, self.speed - decrement)


class Car(Transport):
    """
    Дочерний класс для легковых автомобилей.

    Атрибуты:
        _num_doors (int): Количество дверей.
    """

    def __init__(self, brand: str, model: str, year: int, num_doors: int, speed: float = 0.0):
        """
        Конструктор класса Car.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска.
        :param num_doors: Количество дверей.
        :param speed: Текущая скорость (по умолчанию 0.0).
        """
        super().__init__(brand, model, year, speed)
        self._num_doors = num_doors

    @property
    def num_doors(self) -> int:
        """Возвращает количество дверей автомобиля."""
        return self._num_doors

    @num_doors.setter
    def num_doors(self, value: int) -> None:
        """
        Устанавливает количество дверей автомобиля.
        Количество дверей должно быть положительным числом.
        """
        if value <= 0:
            raise ValueError("Количество дверей должно быть положительным числом.")
        self._num_doors = value

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строка с описанием автомобиля.
        """
        return f"{self.brand} {self.model} ({self.year}), {self.num_doors} дверей, текущая скорость: {self.speed} км/ч"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        :return: Формальная строка с описанием автомобиля.
        """
        return f"Car(brand={self.brand}, model={self.model}, year={self.year}, num_doors={self.num_doors}, speed={self.speed})"

    def open_trunk(self) -> str:
        """
        Открывает багажник автомобиля.

        :return: Сообщение о том, что багажник открыт.
        """
        return "Багажник открыт"

    def accelerate(self, increment: float) -> None:
        """
        Перегруженный метод для увеличения скорости автомобиля.
        У легковых автомобилей ускорение ограничено 120 км/ч.

        :param increment: Величина увеличения скорости.
        """
        self.speed = min(120, self.speed + increment)


class Truck(Transport):
    """
    Дочерний класс для грузовых автомобилей.

    Атрибуты:
        _load_capacity (float): Грузоподъемность в тоннах.
    """

    def __init__(self, brand: str, model: str, year: int, load_capacity: float, speed: float = 0.0):
        """
        Конструктор класса Truck.

        :param brand: Марка грузовика.
        :param model: Модель грузовика.
        :param year: Год выпуска.
        :param load_capacity: Грузоподъемность в тоннах.
        :param speed: Текущая скорость (по умолчанию 0.0).
        """
        super().__init__(brand, model, year, speed)
        self._load_capacity = load_capacity

    @property
    def load_capacity(self) -> float:
        """Возвращает грузоподъемность грузовика."""
        return self._load_capacity

    @load_capacity.setter
    def load_capacity(self, value: float) -> None:
        """
        Устанавливает грузоподъемность грузовика.
        Грузоподъемность должна быть положительным числом.
        """
        if value <= 0:
            raise ValueError("Грузоподъемность должна быть положительным числом.")
        self._load_capacity = value

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строка с описанием грузовика.
        """
        return f"{self.brand} {self.model} ({self.year}), грузоподъемность: {self.load_capacity} тонн, текущая скорость: {self.speed} км/ч"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        :return: Формальная строка с описанием грузовика.
        """
        return f"Truck(brand={self.brand}, model={self.model}, year={self.year}, load_capacity={self.load_capacity}, speed={self.speed})"

    def load_cargo(self, weight: float) -> str:
        """
        Загружает груз в грузовик.

        :param weight: Вес груза в тоннах.
        :return: Сообщение о результате загрузки.
        """
        if weight <= self.load_capacity:
            return f"Груз весом {weight} тонн успешно загружен."
        else:
            return f"Груз весом {weight} тонн превышает грузоподъемность."

    def brake(self, decrement: float) -> None:
        """
        Перегруженный метод для уменьшения скорости грузовика.
        У грузовиков торможение происходит медленнее.

        :param decrement: Величина уменьшения скорости.
        """
        self.speed = max(0, self.speed - decrement * 0.5)


if __name__ == "__main__":
    car = Car("Toyota", "Corolla", 2020, 4)  # speed не указан, используется значение по умолчанию 0.0
    truck = Truck("Volvo", "FH16", 2019, 20.0)  # speed не указан, используется значение по умолчанию 0.0

    print(car)
    print(truck)

    car.accelerate(50)
    truck.accelerate(30)

    print(car)
    print(truck)

    car.brake(20)
    truck.brake(20)

    print(car)
    print(truck)

    print(car.open_trunk())
    print(truck.load_cargo(15))

