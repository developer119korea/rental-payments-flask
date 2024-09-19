from ..core.use_cases.create_rental import CreateRental
from ..entities.rental import Rental
from ..interfaces.rental_interface import RentalInterface
from ..repositories.rental_repository import RentalRepository
from ..schemas.rental_schema import rental_schema


class RentalService(RentalInterface):
    def __init__(self, rental_repository: RentalRepository):
        self.rental_repository = rental_repository
        self.create_rental_use_case = CreateRental(self)

    def create_rental(self, rental_data):
        schema = rental_schema
        errors = schema.validate(rental_data)
        if errors:
            return {"message": "Validation error", "errors": errors}, 400

        if self.rental_repository.get_by_key(rental_data['key']):
            return {"message": "Rental with this key already exists"}, 400

        new_rental = Rental(**rental_data)
        try:
            self.rental_repository.add(new_rental)
            return schema.jsonify(new_rental), 201
        except Exception as e:
            return {"message": "Error creating rental", "error": str(e)}, 500

    def get_all_rentals(self, page, per_page):
        return self.rental_repository.get_rentals(page, per_page)

    def get_rental_by_key(self, key):
        rental = self.rental_repository.get_by_key(key)
        if rental is None:
            return {"message": "Rental not found"}, 404
        return rental_schema.jsonify(rental), 200