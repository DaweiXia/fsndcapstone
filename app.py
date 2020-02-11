from flask import Flask, request, abort, jsonify
from flask_migrate import Migrate
from models import db, setup_db, Movie

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

    return app
