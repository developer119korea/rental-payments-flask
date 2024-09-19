from ...services.rental_service import RentalService


class GetRentalByKey:
    def __init__(self, rental_service: RentalService):
        self.rental_service = rental_service

    def execute(self, key):
        return self.rental_service.get_rental_by_key(key)