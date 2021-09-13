from src.catalog import Catalog
from src.hotel import Hotel

hc = Hotel(name='Mirror', price=500.00, stars=5)
print(hc.show_data())

ch = Catalog()
print(ch.__dict__)

ch.create_hotel(name='Energias', price=500, stars=5)
print(ch.__dict__)

print(ch.list_hotels())

print(ch.search_hotel(hotel_id=2))

ch.edit_hotel(hotel_id=2, name='Risque', price=600, stars=6)
print(ch.search_hotel(hotel_id=2))

ch.delete_hotel(hotel_id=2)
print(ch.list_hotels())