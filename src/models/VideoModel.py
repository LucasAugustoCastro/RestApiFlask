from .. import db

class VideoModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  views = db.Column(db.Integer, nullable=False)
  name = db.Column(db.String(100), nullable=False)
  likes = db.Column(db.Integer, nullable=False)

  def __repr__(self):
    return f'Video(name={name}, views={views}, likes={likes})'