from flask import Blueprint
from flask_restful import Api

from resources.Hello import Hello
from resources.Category import CategoryResource
from resources.Comment import CommentResource

from module.lead.resource import LeadResource  
import module.user as user




api_bp = Blueprint('api', __name__)
api = Api(api_bp)



# Route

api.add_resource(Hello, '/hello')
api.add_resource(CategoryResource, '/Category')
api.add_resource(CommentResource, '/Comment')
api.add_resource(LeadResource, '/lead')
api.add_resource(user.UserRegistration, '/registration')
api.add_resource(user.UserLogin, '/login')
api.add_resource(user.UserLogoutAccess, '/logout/access')
api.add_resource(user.UserLogoutRefresh, '/logout/refresh')
api.add_resource(user.TokenRefresh, '/token/refresh')
api.add_resource(user.AllUsers, '/users')
api.add_resource(user.SecretResource, '/secret')


