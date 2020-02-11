from sqlalchemy import Column, String, Integer, Date
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
    release_date = Column(Date)


class Actor:
    pass
