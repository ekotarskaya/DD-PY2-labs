# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Brick:
    def __init__(self, brick_square: float, brick_type: str):
        """
        Создание и подготовка к работе объекта "Кирпич".
        :param brick_area: Площадь поперечного сечения кирпича.
        :param brick_type: Вид кирпича.
        Примеры:
        >>> brick = Brick(1250, "Облицовочный")
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
        >>> brick = Brick(1500, "Силикатный")
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
        >>> brick = Brick(1200, "Огнеупорный")
        >>> brick.water_absorption(1000)
        :return: Информация о водопоглощении кирпича.
        """
        if not isinstance(water_mass, (int, float)):
            raise TypeError("Масса поглощенной воды должна быть типа int или float")
        if water_mass < 0:
            raise ValueError("Масса воды, поглощенная кирпичом не может быть отрицательной")
        ...
class radio:
    def __init__(self, colour: str, model: str):
        """
        Создание и подготовка к работе объекта "Радиоприемник".
        :param colour: Цвет радиоприемника.
        :param model: Модель радиоприемника.
        Примеры:
        >>> radio = RADIO('черный', 'Hyundai')  # инициализация экземпляра класса
        """
        if not isinstance(colour, (str)):
            raise TypeError("Цвет должен быть типа str")
        self.colour = colour

        if not isinstance(model, (str)):
            raise TypeError("Модель радиоприемника должна быть типа str")
        self.model = model

    def turn_on(self) -> str:
        """
        Включение радио.
        Примеры:
        >>> radio = RADIO('черный', 'Hyundai')
        >>> radio.turn_on()
        :return: Сообщение о включении.
        """
        ...
    def change_wave(self, wave: int) -> str:
        """
        Смена частоты радиоприемника.
        :param wave: Номер новой частоты. Должен быть положительным числом.
        Примеры:
        >>> radio = RADIO('черный', 'Hyundai')
        >>> radio.change_wave(5)
        :return: Сообщение о смене частоты.
        """
        if wave < 1:
            raise ValueError("Номер частоты должен быть положительным числом.")
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
        >>> car = Car('Porshe', 'Cayenne', 2018, 15000.0)
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
        >>> car = Car('Porshe', 'Cayenne', 2018, 15000.0)
        >>> car.drive(500.0)
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
        >>> car = Car('Porshe', 'Cayenne', 2018, 15000.0)
        >>> car.car_age()
        :return: Возраст автомобиля.
        """
        ...


if __name__ == "__main__":
    doctest.testmod()#TODO работоспособность экземпляров класса проверить с помощью doctest

