from flask import request
from flask_restful import Resource
from models.category import db, Category, CategorySchema
from utility.Response import Response

categories_schema = CategorySchema(many=True)
category_schema = CategorySchema()


class CategoryResource(Resource):
    def get(self):
        categories = Category.query.all()
        categories = categories_schema.dump(categories).data
        return Response.success(categories,200)

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return Response.error('No input data provided',400)
        # Validate and deserialize input
        data, errors = category_schema.load(json_data)
        if errors:
            return Response.error(errors,422)
        category = Category.query.filter_by(name=data['name']).first()
        if category:
            return Response.error('Category already exists',400)
        category = Category(
            name=json_data['name']
        )

        db.session.add(category)
        db.session.commit()

        result = category_schema.dump(category).data

        return Response.success(result,201)

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return Response.error('No input data provided',400)
        # Validate and deserialize input
        data, errors = category_schema.load(json_data)
        if errors:
            return errors, 422
        category = Category.query.filter_by(id=data['id']).first()
        if not category:
            return Response.error('Category does not exist',400)
        category.name = data['name']
        db.session.commit()

        result = category_schema.dump(category).data

        return Response.success(result,204)

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return Response.error('No input data provided',400)
        # Validate and deserialize input
        data, errors = category_schema.load(json_data)
        if errors:
            return errors, 422
        category = Category.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = category_schema.dump(category).data

        return Response.success(result,204)
