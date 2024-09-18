from flask import Blueprint, jsonify, request

from .. import db
from ..models.rental_model import Rental
from ..schemas.rental_schema import rental_schema, rentals_schema

rental_bp = Blueprint('rental', __name__)

@rental_bp.route('', methods=['POST'])
def add_rental():
    data = request.get_json()
    schema = rental_schema  # RentalSchema 인스턴스 사용

    if not data:
        return jsonify({"message": "No input data provided"}), 400

    errors = schema.validate(data)
    if errors:
        return jsonify({"message": "Validation error", "errors": errors}), 400

    if Rental.query.filter_by(key=data['key']).first() is not None:
        return jsonify({"message": "Rental with this key already exists"}), 400

    try:
        new_rental = Rental(
            key=data['key'],
            status=data['status'],
            billing_code=data['billing_code'],
            product_name=data['product_name'],
            installment_plan=data['installment_plan'],
            installment_amount=data['installment_amount'],
            payment_day=data['payment_day'],
            payment_period=data['payment_period']
        )
        db.session.add(new_rental)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error creating rental", "error": str(e)}), 500

    return rental_schema.jsonify(new_rental), 201

@rental_bp.route('', methods=['GET'])
def get_rentals():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        pagination = Rental.query.paginate(page=page, per_page=per_page)

        result = {
            "total_rentals": pagination.total,
            "total_pages": pagination.pages,
            "current_page": pagination.page,
            "per_page": pagination.per_page,
            "rentals": rentals_schema.dump(pagination.items),  # 현재 페이지의 렌탈 목록
            "has_next": pagination.has_next,  # 다음 페이지 여부
            "has_prev": pagination.has_prev,  # 이전 페이지 여부
            "next_num": pagination.next_num,  # 다음 페이지 번호
            "prev_num": pagination.prev_num   # 이전 페이지 번호
        }

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": "Error retrieving rentals", "error": str(e)}), 500

@rental_bp.route('/<string:key>', methods=['GET'])
def get_rental_by_key(key):
    rental = Rental.query.filter_by(key=key).first()
    if rental is None:
        return jsonify({"message": "Rental not found"}), 404

    return rental_schema.jsonify(rental), 200
