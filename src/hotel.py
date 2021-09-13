class Hotel:
    counter: int = 0

    def __init__(self, name, price, stars) -> None:
        self.__id: int = Hotel.counter + 1
        self.__name: str = name
        self.__price: float = price
        self.__stars: float = stars
        Hotel.counter = self.__id

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, new_name) -> None:
        self.__name = new_name

    def get_price(self) -> float:
        return self.__price

    def get_formatted_price(self) -> str:
        return f'${self.__price}'

    def set_price(self, new_price) -> None:
        self.__price = new_price

    def get_stars(self) -> float:
        return self.__stars

    def set_stars(self, new_stars) -> None:
        self.__stars = new_stars

    def show_data(self) -> str:
        return f'Id: {self.get_id()}; Name: {self.get_name()}; Price: {self.get_formatted_price()};' \
               f' Stars: {self.get_stars()}'
