from src.hotel import Hotel


class Catalog:

    def __init__(self):
        self.__hotels: [Hotel] = []

    def __find_hotel(self, hotel_id) -> Hotel:
        for hotel in self.__hotels:
            if hotel.get_id() == hotel_id:
                return hotel

    def create_hotel(self, name, price, stars) -> None:
        hotel = Hotel(name, price, stars)
        self.__hotels.append(hotel)

    def list_hotels(self) -> list:
        hotels_show_data = []
        for hotel in self.__hotels:
            hotels_show_data.append(hotel.show_data())
        return hotels_show_data

    def search_hotel(self, hotel_id) -> str:
        return self.__find_hotel(hotel_id).show_data()

    def edit_hotel(self, hotel_id, name, price, stars) -> None:
        hotel = self.__find_hotel(hotel_id)
        hotel.set_name(name)
        hotel.set_price(price)
        hotel.set_stars(stars)

    def delete_hotel(self, hotel_id) -> None:
        self.__hotels.remove(self.__find_hotel(hotel_id))
