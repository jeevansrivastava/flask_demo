from flask import Blueprint
from flask_restful import Api



lead_bp = Blueprint('lead', __name__)
api = Api(lead_bp)

# Route

import module.lead.route

