from ...schemas.rental_schema import rental_schema


class CreateRental:
    def __init__(self, rental_service):
        self.rental_service = rental_service

    def execute(self, data):
        schema = rental_schema
        errors = schema.validate(data)
        if errors:
            return {"message": "Validation error", "errors": errors}, 400

        return self.rental_service.create_rental(data)