from  module.lead.resource import LeadResource
from module.lead import api



api.add_resource(LeadResource, '/lead')