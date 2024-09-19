from .rental_routes import rental_bp


def register_blueprints(app, create_rental_use_case, get_rentals_use_case, get_rental_by_key_use_case):
    rental_bp.create_rental_use_case = create_rental_use_case
    rental_bp.get_rentals_use_case = get_rentals_use_case
    rental_bp.get_rental_by_key_use_case = get_rental_by_key_use_case
    app.register_blueprint(rental_bp, url_prefix='/rentals')