from src.hotel import Hotel


class Catalog:

    def __init__(self):
        self.__hotels: [Hotel] = []

    def __find_hotel(self, hotel_id) -> Hotel:
        hotel_to_return = None
        for hotel in self.__hotels:
            if hotel.get_id() == hotel_id:
                hotel_to_return = hotel
        if hotel_to_return is None:
            raise BaseException(f'Hotel not found: id {hotel_id}')
        return hotel_to_return

    def create_hotel(self, name, price, stars) -> None:
        hotel = Hotel(name, price, stars)
        self.__hotels.append(hotel)

    def list_hotels(self, price_sort=False, hotel_filter=None) -> list:
        hotels_show_data = []

        if price_sort:
            self.__hotels.sort(key=lambda hotel_obj: hotel_obj.get_price())

        for hotel in self.__hotels:
            if hotel_filter is not None:
                if hotel_filter.lower() in hotel.get_name().lower():
                    hotels_show_data.append(hotel.show_data())
            else:
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

    def add_hotels(self, hotels) -> None:
        self.__hotels.extend(hotels)