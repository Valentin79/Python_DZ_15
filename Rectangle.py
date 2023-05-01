import argparse
import logging
from datetime import datetime

logging.basicConfig(filename="DZ_15\Rectangle.log", filemode="a", encoding="utf-8", level=logging.INFO)
logger = logging.getLogger(__name__)

class Rectangle:

    def __init__(self, width, height: None = None):
        if height == None:
            logger.info(f"Будем считать, что это квадрат со сторонами {width} и {width}") # <<<<<<<<<<<<<<<
        self.width = Rectangle.validate(self, width)
        self.height = Rectangle.validate(self, height or width)

    def get_perimeter(self) -> float:
        result = 2 * (self.width + self.height)
        logger.info(f"Периметр = {result}") # <<<<<<<<<<<<<<<<<<<<<<
        return result

    def get_area(self) -> float:
        result = self.width * self.height
        logger.info(f"Площадь = {result}") # <<<<<<<<<<<<<<<<<<<<<<<<,
        return result

    def validate(self, value): # Проверка введеных значений на число и отрицательное число.
        if type(value) == int or type(value) == float:
            if value < 0:
                logger.error(f"Значение не должно быть отрицательным: {value}") # <<<<<<<<<<<<<<<<<<
                raise Exception(f"Значение не должно быть отрицательным: {value}")

        else:
            logger.error(f"Введено не число: {value}") # <<<<<<<<<<<<<<<<<<<<<<<<<<
            raise Exception(f"Введено не число: {value}")

        return value

def get_args():
    logger.info(f"{(datetime.now())}") # <<<<<<<<<<<<<<<<<<<<<<<<<<<
    width = None
    height = None
    args = argparse.ArgumentParser(description="Получаем аргументы")
    args.add_argument("-W", "--width", default=0)
    args.add_argument("-H", "--height", default=0) # Видимо маленькая h зарезервирована. С ней выдает ошибку
    result = args.parse_args()
    print(f"{result.width}, {result.height}")
    try:
        width = int(result.width)
    except ValueError as ex:
        logger.error(f"Введено не число {ex}; Значение по умолчанию = 0") # <<<<<<<<<<<<
        print(ex)
    try:
        height = int(result.height)
    except ValueError as ex:
        logger.error(f"Введено не число {ex}; Значение по умолчанию = 0") # <<<<<<<<<<<<<<<
        print(ex)
    logger.info(f"Стороны прямоугольника: Ширина = {width}, Высота = {height}") # <<<<<<<<<<<<<<<<
    # return [int(result.width), int(result.height)]
    return [width, height]


if __name__ == '__main__':
    rect = Rectangle(*get_args())
    print(rect.get_perimeter())
    print(rect.get_area())

    # square = Rectangle(10)
    # print(square.get_perimeter())
    # print(square.get_area())