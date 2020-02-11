from sqlalchemy import Column, String, Integer, DateTime
from flask_sqlalchemy import SQLAlchemy

dbname = "casting_agency_test"
host = 'localhost:5432'
uname = 'postgres'
upwd = 'postgres'
database_path = "postgresql://{}:{}@{}/{}".format(uname, upwd, host, dbname)
db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(DateTime)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()


class Actor:
    pass
