from app import db

from ..entities.rental import Rental
from ..interfaces.rental_interface import RentalInterface


class RentalRepository(RentalInterface):
    def add(self, rental):
        db.session.add(rental)
        db.session.commit()

    def get_rentals(self, page, per_page):
        pagination = Rental.query.paginate(page=page, per_page=per_page)
        return {
            "total_rentals": pagination.total,
            "total_pages": pagination.pages,
            "current_page": pagination.page,
            "per_page": pagination.per_page,
            "rentals": [rental.to_dict() for rental in pagination.items],
            "has_next": pagination.has_next,
            "has_prev": pagination.has_prev,
            "next_num": pagination.next_num,
            "prev_num": pagination.prev_num
        }

    def get_by_key(self, key):
        return Rental.query.filter_by(key=key).first()

    def rollback(self):
        db.session.rollback()