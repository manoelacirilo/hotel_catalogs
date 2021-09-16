from src.catalog import Catalog
from src.hotel import Hotel

hc = Hotel(name='Mirror', price=500.00, stars=5)
# print(hc.show_data())

ch = Catalog()
# print(ch.__dict__)

ch.create_hotel(name='Energias', price=500, stars=7)
# print(ch.__dict__)

ch.create_hotel(name='Like', price=300, stars=3)
# print(ch.__dict__)

# print(ch.list_hotels(price_sort=True, hotel_filter='ene'))
#
try:
    # print(ch.search_hotel(hotel_id=4))
    # ch.delete_hotel(hotel_id=5)
    ch.edit_hotel(hotel_id=2, name='Risque', price=600, stars=6)
except BaseException as error:
    print(f'Internal Error: {error}')

ch.add_hotels(hotels=[hc])
print(ch.list_hotels())
# print(ch.search_hotel(hotel_id=2))
#
# ch.delete_hotel(hotel_id=2)
# print(ch.list_hotels())
