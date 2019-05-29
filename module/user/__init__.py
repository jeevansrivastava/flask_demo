from module.user.resource import UserLogin, UserLogoutAccess, UserRegistration, UserLogoutRefresh, TokenRefresh, AllUsers, SecretResource
from flask import Blueprint
from flask_restful import Api

import module.user as user

user_bp = Blueprint('user', __name__)
api = Api(user_bp)

# Route


api.add_resource(user.UserRegistration, '/registration')
api.add_resource(user.UserLogin, '/login')
api.add_resource(user.UserLogoutAccess, '/logout/access')
api.add_resource(user.UserLogoutRefresh, '/logout/refresh')
api.add_resource(user.TokenRefresh, '/token/refresh')
api.add_resource(user.AllUsers, '/users')
api.add_resource(user.SecretResource, '/secret')