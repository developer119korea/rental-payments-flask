from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()
    print("데이터베이스 테이블이 생성되었습니다.")
