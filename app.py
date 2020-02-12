from flask import Flask, request, abort, jsonify
from flask_migrate import Migrate
from models import db, setup_db, Movie, Actor

from datetime import datetime


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    migrate = Migrate(app, db)

    @app.route('/movies', methods=['POST'])
    def post_movies():
        data = request.json
        release_date = datetime.now()
        try:
            movie = Movie(title=data['title'], release_date=release_date)
            movie.insert()
            return jsonify({'success': True})
        except Exception:
            db.session.rollback()
            abort(422)

    @app.route('/movies', methods=['GET'])
    def get_movies():
        movies = Movie.query.all()
        formated_movies = [movie.format() for movie in movies]

        if len(movies) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'movies': formated_movies
        })

    @app.route('/actors', methods=['POST'])
    def post_actors():
        data = request.json
        try:
            actor = Actor(name=data['name'], age=data['age'], gender=data['gender'])
            actor.insert()
            return jsonify({'success': True})
        except Exception:
            db.session.rollback()
            abort(422)

    return app
