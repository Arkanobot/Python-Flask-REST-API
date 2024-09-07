from flask import Flask
from models import db
from flask_restful import Api
from resources.user_resources import Users, User
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config.from_object("config.Config")

db.init_app(app)
api = Api(app)

# Register API Resources

api.add_resource(Users, "/api/v1/users")
api.add_resource(User, "/api/v1/users/<int:user_id>")


@app.route("/")
def home():
    return "<h1>Flask REST API</h1>"


if __name__ == "__main__":
    if os.getenv("ENV") == "PROD":
        app.run()
    else:
        app.run(debug=True)
