from ...services.rental_service import RentalService


class GetRentals:
    def __init__(self, rental_service: RentalService):
        self.rental_service = rental_service

    def execute(self, page, per_page):
        return self.rental_service.get_all_rentals(page, per_page)