class RentalInterface:
    def add_rental(self, rental_data):
        raise NotImplementedError

    def get_rentals(self, page, per_page):
        raise NotImplementedError

    def get_rental_by_key(self, key):
        raise NotImplementedError