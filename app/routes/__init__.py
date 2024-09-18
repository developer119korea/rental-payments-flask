from .rental_routes import rental_bp


def register_blueprints(app):
    app.register_blueprint(rental_bp, url_prefix='/rentals')