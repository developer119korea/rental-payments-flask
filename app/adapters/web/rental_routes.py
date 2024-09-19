from flask import Blueprint, jsonify, request

from ...core.use_cases.create_rental import CreateRental
from ...core.use_cases.get_rental_by_key import GetRentalByKey
from ...core.use_cases.get_rentals import GetRentals
from ...repositories.rental_repository import RentalRepository
from ...services.rental_service import RentalService

rental_bp = Blueprint('rental', __name__)
rental_repository = RentalRepository()
rental_service = RentalService(rental_repository)

create_rental_use_case = CreateRental(rental_service)
get_rentals_use_case = GetRentals(rental_service)
get_rental_by_key_use_case = GetRentalByKey(rental_service)

@rental_bp.route('', methods=['POST'])
def add_rental():
    data = request.get_json()

    if not data:
        return jsonify({"message": "No input data provided"}), 400

    result = create_rental_use_case.execute(data)
    return result

@rental_bp.route('', methods=['GET'])
def get_rentals():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        result = get_rentals_use_case.execute(page, per_page)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "Error retrieving rentals", "error": str(e)}), 500

@rental_bp.route('/<string:key>', methods=['GET'])
def get_rental_by_key(key):
    result = get_rental_by_key_use_case.execute(key)
    return result
