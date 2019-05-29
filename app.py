from flask import Blueprint
from flask_restful import Api

from module.lead.resource import LeadResource
from resources.Category import CategoryResource
from resources.Comment import CommentResource
from resources.Hello import Hello

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route

api.add_resource(Hello, '/hello')
api.add_resource(CategoryResource, '/Category')
api.add_resource(CommentResource, '/Comment')
api.add_resource(LeadResource, '/lead')

from flask import Flask
from flask_jwt_extended import JWTManager

from module.user.model import RevokedTokenModel


app = Flask(__name__)
app.config.from_object("config")

from app import api_bp
from module.user import user_bp
from module.lead import lead_bp

app.register_blueprint(user_bp, url_prefix='/v1')
app.register_blueprint(api_bp, url_prefix='/v1')
app.register_blueprint(lead_bp, url_prefix='/v1')

from models import db
db.init_app(app)

jwt = JWTManager(app)


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)
