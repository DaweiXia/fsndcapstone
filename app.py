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

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    def del_movies(movie_id):
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
            abort(404)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    def patch_movies(movie_id):
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
            abort(404)

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

    @app.route('/actors', methods=['GET'])
    def get_actors():
        actors = Actor.query.all()
        formated_actors = [actor.format() for actor in actors]

        if len(actors) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'actors': formated_actors
        })

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    def del_actors(actor_id):
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
            abort(404)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    def patch_actors(actor_id):
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
            abort(404)

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
