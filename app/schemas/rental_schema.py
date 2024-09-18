from marshmallow import ValidationError, fields, validates

from .. import ma
from ..models.rental_model import Rental


class RentalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Rental
        load_instance = True

    @validates('key')
    def validate_key(self, value):
        if not value:
            raise ValidationError("키는 필수입니다.")

    @validates('status')
    def validate_status(self, value):
        if value not in ['active', 'inactive']:
            raise ValidationError("상태는 'active' 또는 'inactive'이어야 합니다.")

    @validates('installment_plan')
    def validate_installment_plan(self, value):
        if value <= 0:
            raise ValidationError("분납 개월은 0보다 커야 합니다.")

    @validates('installment_amount')
    def validate_installment_amount(self, value):
        if value <= 0:
            raise ValidationError("분납 금액은 0보다 커야 합니다.")

    @validates('payment_day')
    def validate_payment_day(self, value):
        if value < 1 or value > 28:
            raise ValidationError("지불일은 1에서 28 사이여야 합니다.")

    @validates('payment_period')
    def validate_payment_period(self, value):
        if value != 1:
            raise ValidationError("지불 주기는 1이어야 합니다.")

rental_schema = RentalSchema()
rentals_schema = RentalSchema(many=True)
