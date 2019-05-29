from flask import request
from flask_restful import Resource
from module.lead.model import db, Lead, LeadSchema
from utility.Response import Response

from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)

lead_schema = LeadSchema(many=True)
lead_schema = LeadSchema()


class LeadResource(Resource):
    @jwt_required
    def get(self):
        lead = Lead.query.all()
        leads = lead_schema.dump(lead).data
        return Response.success(leads,200)

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return Response.error('No input data provided',400)
        # Validate and deserialize input
        data, errors = lead_schema.load(json_data)
        if errors:
            return Response.error(errors,422)
        lead = Lead.query.filter_by(name=data['name']).first()
        if lead:
            return Response.error('Lead already exists',400)
        lead = Lead(
            name=json_data['name']
        )

        db.session.add(lead)
        db.session.commit()

        result = lead_schema.dump(lead).data

        return Response.success(result,201)

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return Response.error('No input data provided',400)
        # Validate and deserialize input
        data, errors = lead_schema.load(json_data)
        if errors:
            return errors, 422
        Lead = Lead.query.filter_by(id=data['id']).first()
        if not Lead:
            return Response.error('Lead does not exist',400)
        Lead.name = data['name']
        db.session.commit()

        result = lead_schema.dump(Lead).data

        return Response.success(result,204)

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return Response.error('No input data provided',400)
        # Validate and deserialize input
        data, errors = lead_schema.load(json_data)
        if errors:
            return errors, 422
        Lead = Lead.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = lead_schema.dump(Lead).data

        return Response.success(result,204)
