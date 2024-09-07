from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

api = Api(app)


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(320), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"User(name = {self.name}, email = {self.email})"


user_args = reqparse.RequestParser()
user_args.add_argument("name", type=str, required=True, help="Name cannot be blank")
user_args.add_argument("email", type=str, required=True, help="Email cannot be blank")

userFields = {"id": fields.Integer, "name": fields.String, "email": fields.String}


class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users, 200

    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        existing_user = UserModel.query.filter_by(email=args.email).first()
        if existing_user:
            abort(409, message="Email already exists.")
        else:
            user = UserModel(name=args["name"], email=args["email"])
            db.session.add(user)
            db.session.commit()
            users = UserModel.query.all()
            return users, 201


class User(Resource):
    @marshal_with(userFields)
    def get(self, user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            abort(404, message="User not found")
        return user, 200

    @marshal_with(userFields)
    def patch(self, user_id):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            abort(404, message="User not found")
        user.name = args["name"]
        user.email = args["email"]
        db.session.commit()
        return user, 200

    @marshal_with(userFields)
    def delete(self, user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            abort(404, message="User not found")
        db.session.delete(user)
        db.session.commit()
        return user, 200


api.add_resource(Users, "/api/v1/users")
api.add_resource(User, "/api/v1/users/<int:user_id>")


@app.route("/")
def home():
    return "<h1>Flask REST API</h1>"


if __name__ == "__main__":
    app.run(debug=True)
