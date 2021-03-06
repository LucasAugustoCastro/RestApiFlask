from flask import Flask, Blueprint
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from ..models.VideoModel import VideoModel

views = Blueprint('views', __name__)

video_put_args =reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required", required=True)

video_update_args =reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required")
video_update_args.add_argument("views", type=int, help="Views of the video is required")
video_update_args.add_argument("likes", type=int, help="Likes of the video is required")

api = Api(views)


resource_fields = {
  'id': fields.Integer,
  'name': fields.String,
  'views': fields.Integer,
  'likes': fields.Integer

}

class Video(Resource):
  @marshal_with(resource_fields)
  def get(self, video_id):
    result = VideoModel.query.filter_by(id=video_id).first()
    if not result:
      abort(404, message='Could not find videos with that id')
    return result
    
  @marshal_with(resource_fields)
  def put(self, video_id):
    args = video_put_args.parse_args()
    result = VideoModel.query.filter_by(id=video_id).first()
    if result:
      abort(409, message='Video id taken...')

    video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
    db.session.add(video)
    db.session.commit()
    return video, 201

  @marshal_with(resource_fields)
  def patch(self, video_id):
    args = video_update_args.parse_args()
    result = VideoModel.query.filter_by(id=video_id).first()
    if not result:
      abort(404, message='Video does not exist, cannot update')

    if args['name']:
      result.name = args['name']
    if args['views']:
      result.views = args['views']
    if args['likes']:
      result.likes = args['likes']
    


    db.session.commit()

    return result

  def delete(self, video_id):
    abort_if_video_id_does_not_exist(video_id)
    del videos[video_id]
    return '', 204


api.add_resource(Video, "/video/<int:video_id>")