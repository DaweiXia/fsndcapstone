from flask import Flask, request, abort, jsonify
from flask_migrate import Migrate
from models import db, setup_db, Movie, Actor
from datetime import datetime
from auth import AuthError, requires_auth


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    migrate = Migrate(app, db)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def post_movies(payload):
        data = request.json
        date = data['release_date']
        release_date = datetime(date['year'], date['month'], date['day'])
        try:
            movie = Movie(title=data['title'], release_date=release_date)
            movie.insert()
            return jsonify({'success': True})
        except Exception:
            db.session.rollback()
            abort(422)

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        movies = Movie.query.all()
        formated_movies = [movie.format() for movie in movies]

        if len(movies) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'movies': formated_movies
        })

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def del_movies(payload, movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie:
            try:
                movie.delete()
                return jsonify({
                    'success': True
                })
            except Exception:
                db.session.rollback()
                abort(422)
        else:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_movies(payload, movie_id):
        data = request.json
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie:
            if movie.title != data['title']:
                movie.title = data['title']
            try:
                movie.update()
                return jsonify({'success': True})
            except Exception:
                db.session.rollback()
                abort(422)
        else:
            abort(422)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def post_actors(payload):
        data = request.json
        try:
            actor = Actor(name=data['name'], age=data['age'], gender=data['gender'])
            actor.insert()
            return jsonify({'success': True})
        except Exception:
            db.session.rollback()
            abort(422)

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        actors = Actor.query.all()
        formated_actors = [actor.format() for actor in actors]

        if len(actors) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'actors': formated_actors
        })

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def del_actors(payload, actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor:
            try:
                actor.delete()
                return jsonify({
                    'success': True
                })
            except Exception:
                db.session.rollback()
                abort(422)
        else:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patch_actors(payload, actor_id):
        data = request.json
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor:
            if actor.name != data['name']:
                actor.name = data['name']
            if actor.age != data['age']:
                actor.age = data['age']
            if actor.gender != data['gender']:
                actor.gender = data['gender']
            try:
                actor.update()
                return jsonify({'success': True})
            except Exception:
                db.session.rollback()
                abort(422)
        else:
            abort(422)

    # Error Handling
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
                        "success": False, 
                        "error": 422,
                        "message": "unprocessable"
                        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
                        "success": False,
                        "error": 404,
                        "message": "resource not found"
                        }), 404

    @app.errorhandler(401)
    def invalid_header(error):
        return jsonify({
                        "success": False,
                        "error": 401,
                        "message": "Invalid header!"
                        }), 401

    @app.errorhandler(405)
    def permission_error(error):
        return jsonify({
                        "success": False,
                        "error": 405,
                        "message": "Permission not found!"
                        }), 405

    return app
