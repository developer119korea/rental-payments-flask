from ...repositories.rental_repository import RentalRepository
from ...services.rental_service import RentalService
from .create_rental import CreateRental
from .get_rental_by_key import GetRentalByKey
from .get_rentals import GetRentals

def create_use_cases():
    rental_repository = RentalRepository()
    rental_service = RentalService(rental_repository)

    return (
        CreateRental(rental_service),
        GetRentals(rental_service),
        GetRentalByKey(rental_service)
    )
