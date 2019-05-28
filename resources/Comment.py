from flask import jsonify, request
from flask_restful import Resource
from models.category import Category
from models.comment import db, Comment, CommentSchema
from utility.Response import Response


comments_schema = CommentSchema(many=True)
comment_schema = CommentSchema()


class CommentResource(Resource):
    def get(self):
        comments = Comment.query.all()
        comments = comments_schema.dump(comments).data
        return Response.success(comments, 200)

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return Response.error('No input data provided', 400)

        # Validate and deserialize input
        data, errors = comment_schema.load(json_data)
        if errors:
            return Response.error(errors, 422)
        category_id = Category.query.filter_by(id=data['category_id']).first()
        if not category_id:
            return Response.error('comment category not found', 400)
        comment = Comment(
            category_id=data['category_id'],
            comment=data['comment']
        )
        db.session.add(comment)
        db.session.commit()

        result = comment_schema.dump(comment).data

        return Response.success(result, 201)
