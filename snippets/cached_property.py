import functools


class Address:
    def __init__(self, city: str, zip_code: str, street: str, building: str, apartment: str = None):
        self.city = city
        self.zip_code = zip_code
        self.street = street
        self.building = building
        self.apartment = apartment

    @functools.cached_property
    def address_text(self) -> str:
        print('Building address text...')
        text = f'Ulica {self.street} '
        if self.apartment:
            text += f'{self.building}/{self.apartment}, '
        else:
            text += f'{self.building}, '
        text += f'{self.zip_code} {self.city}'
        return text


address = Address('Kraków', '30-136', 'Przykładowa', '21', '37')

print(address.address_text)
print(address.address_text)
