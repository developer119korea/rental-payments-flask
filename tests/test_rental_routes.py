import unittest

from app import create_app, db
from app.models.rental_model import Rental


class RentalRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_rental(self):
        response = self.client.post('/rentals', json={
            "key": "test_key",
            "status": "active",
            "billingCode": "billing-12345",
            "productName": "Test Product",
            "installmentPlan": 12,
            "installmentAmount": 100,
            "paymentDay": 1,
            "paymentPeriod": 1
        })
        self.assertEqual(response.status_code, 201)

    def test_add_rental_bad_request(self):
        response = self.client.post('/rentals', json={
            "key": "test_key",
            "status": "active",
            # "billingCode" 필드가 누락됨
            "productName": "Test Product",
            "installmentPlan": 12,
            "installmentAmount": 100,
            "paymentDay": 1,
            "paymentPeriod": 1
        })
        self.assertEqual(response.status_code, 400)

    def test_add_rental_duplicate_key(self):
        # 첫 번째 추가
        self.client.post('/rentals', json={
            "key": "test_key",
            "status": "active",
            "billingCode": "billing-12345",
            "productName": "Test Product",
            "installmentPlan": 12,
            "installmentAmount": 100,
            "paymentDay": 1,
            "paymentPeriod": 1
        })
        # 중복 추가 시도
        response = self.client.post('/rentals', json={
            "key": "test_key",
            "status": "active",
            "billingCode": "billing-12345",
            "productName": "Test Product",
            "installmentPlan": 12,
            "installmentAmount": 100,
            "paymentDay": 1,
            "paymentPeriod": 1
        })
        self.assertEqual(response.status_code, 400)

    def test_get_rentals(self):
        response = self.client.get('/rentals?page=1&per_page=10')
        self.assertEqual(response.status_code, 200)

    def test_get_rental_by_key(self):
        self.client.post('/rentals', json={
            "key": "test_key",
            "status": "active",
            "billingCode": "12345",
            "productName": "Test Product",
            "installmentPlan": 12,
            "installmentAmount": 100,
            "paymentDay": 1,
            "paymentPeriod": 1
        })
        response = self.client.get('/rentals/test_key')
        self.assertEqual(response.status_code, 200)

    def test_add_rental_missing_field(self):
        response = self.client.post('/rentals', json={"key": "test_key"})
        self.assertEqual(response.status_code, 400)

    def test_get_rental_not_found(self):
        response = self.client.get('/rentals/non_existing_key')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()