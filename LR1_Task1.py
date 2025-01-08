# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Brick:
    def __init__(self, brick_area: float, brick_type: str):
        """
        Создание и подготовка к работе объекта "Кирпич".
        :param brick_area: Площадь поперечного сечения кирпича.
        :param brick_type: Вид кирпича.
        Примеры:
        >>> brick = Brick(1500, "силикатный")
        """

        if not isinstance(brick_area, (int, float)):
            raise TypeError("Вес кирпича должен быть типа int или float")
        if brick_area <= 0:
            raise ValueError("Вес кирпича должен быть положительным числом")
        self.brick_area = brick_area

        if not isinstance(brick_type, (str)):
            raise TypeError("Вид кирпича должен быть str")
        self.brick_type = brick_type

    def durability_test(self, pressure: float) -> int:
        """
        Испытание кирпича на прочность.
        :param pressure: Давление, прилагаемое на кирпич.
        Примеры:
        >>> brick = Brick(1500, "силикатный")
        >>> brick.durability_test(5000)
        :return: Марка кирпича.
        """

        if not isinstance(pressure, (int, float)):
            raise TypeError("Давление должно быть типа int или float")
        if pressure <= 0:
            raise ValueError("Для испытания необходимо, чтобы давление было и было положительным")
        ...
    def water_absorption(self, water_mass: float) -> str:
        """
        Испытание кирпича на водопоглощение.
        :param water_mass: Масса воды, поглощенной за время испытания.
        Примеры:
        >>> brick = Brick(1500, "силикатный")
        >>> brick.water_absorption(1000)
        :return: Информация о водопоглощении кирпича.
        """
        if not isinstance(water_mass, (int, float)):
            raise TypeError("Масса поглощенной воды должна быть типа int или float")
        if water_mass < 0:
            raise ValueError("Масса воды, поглощенная кирпичом не может быть отрицательной")
        ...
class TV:
    def __init__(self, colour: str, diagonal: float):
        """
        Создание и подготовка к работе объекта "Телевизор".
        :param colour: Цвет телевизора.
        :param diagonal: Диагональ телевизора.
        Примеры:
        >>> tv = TV('черный', 7.8)  # инициализация экземпляра класса
        """
        if not isinstance(colour, (str)):
            raise TypeError("Цвет должен быть типа str")
        self.colour = colour

        if not isinstance(diagonal, (int, float)):
            raise TypeError("Диагональ телевизора должна быть типа int или float")
        if diagonal <= 0:
            raise ValueError("Диагональ телевизора должна быть положительным числом")
        self.diagonal = diagonal

    def turn_on(self) -> str:
        """
        Включение телевизора.
        Примеры:
        >>> tv = TV('черный', 7.8)
        >>> tv.turn_on()
        :return: Сообщение о включении.
        """
        ...
    def change_channel(self, channel: int) -> str:
        """
        Смена канала телевизора.
        :param channel: Номер нового канала. Должен быть положительным числом.
        Примеры:
        >>> tv = TV('черный', 7.8)
        >>> tv.change_channel(5)
        :return: Сообщение о смене канала.
        """
        if channel < 1:
            raise ValueError("Номер канала должен быть положительным числом.")
        ...
class Car:
    def __init__(self, brand: str, model: str, year: int, mileage: float):
        """
        Создание объекта "Автомобиль".
        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска автомобиля
        :param mileage: Пробег автомобиля в километрах
        Примеры:
        >>> car = Car('Toyota', 'Corolla', 2020, 15000.0)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть str.")
        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть str.")
        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть целым числом.")
        if year < 1886:
            raise ValueError("Год выпуска не может быть раньше 1886 года.")
        if not isinstance(mileage, (int, float)) or mileage < 0:
            raise ValueError("Пробег автомобиля должен быть положительным числом.")
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, distance: float) -> None:
        """
        Увеличивает пробег автомобиля на указанное расстояние.
        :param distance: Пройденное расстояние в километрах.
        Примеры:
        >>> car = Car('Toyota', 'Corolla', 2020, 15000.0)
        >>> car.drive(200.0)
        :return: Новое значение пробега с учетом пройденного расстояния.
        """
        if distance < 0:
            raise ValueError("Пройденное расстояние не может быть отрицательным.")
        self.mileage += distance
        ...
    def car_age(self) -> int:
        """
        Вычисляет возраст автомобиля в годах с использованием функции from datetime import date.
        Примеры:
        >>> car = Car('Toyota', 'Corolla', 2020, 15000.0)
        >>> car.car_age()
        :return: Возраст автомобиля.
        """
        ...


if __name__ == "__main__":
    doctest.testmod()#TODO работоспособность экземпляров класса проверить с помощью doctest

