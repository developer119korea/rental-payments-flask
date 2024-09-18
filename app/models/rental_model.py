import uuid
from datetime import datetime

from .. import db


class Rental(db.Model):
    __tablename__ = 'rentals'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    key = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    billing_code = db.Column(db.String(255), nullable=False)
    product_name = db.Column(db.String(255), nullable=False)
    installment_plan = db.Column(db.Integer, nullable=False)
    installment_amount = db.Column(db.Integer, nullable=False)
    payment_day = db.Column(db.Integer, nullable=False)
    payment_period = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, key, status, billing_code, product_name, installment_plan, installment_amount, payment_day, payment_period):
        self.key = key
        self.status = status
        self.billing_code = billing_code
        self.product_name = product_name
        self.installment_plan = installment_plan
        self.installment_amount = installment_amount
        self.payment_day = payment_day
        self.payment_period = payment_period
