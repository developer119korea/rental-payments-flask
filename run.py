import os

from dotenv import load_dotenv

from app import app

load_dotenv()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port)
