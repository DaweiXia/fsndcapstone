import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import *
from datetime import datetime


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_movie = {
            'title': 'TestMovie'
        }

        self.new_actor = {
            'name': 'TestActor',
            'age': '31',
            'gender': 'Female'
        }

    def tearDown(self):
        """Executed after reach test"""
        # test_movie = Movie.query.filter_by(title="TestMovie").first()
        # test_movie.delete()
        # test_actor = Actor.query.filter_by(name="TestActor").first()
        # test_actor.delete()

    def test_post_new_movie_success(self):
        res = self.client().post('/movies', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_post_new_actor_success(self):
        res = self.client().post('/actors', json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_post_new_movie_fail(self):
        res = self.client().post('/movies', json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])

    def test_post_new_actor_fail(self):
        res = self.client().post('/actors', json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])

    def test_get_movies_success(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertTrue(data['success'])
        self.assertTrue(len(data['movies']))

    def test_get_actors_success(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['actors'])

    def test_delete_movie_success(self):
        res = self.client().delete('/movies/1')
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(movie, None)

    def test_delete_actor_success(self):
        res = self.client().delete('/actors/1')
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(actor, None)

    def test_422_delete_movie_do_not_exist(self):
        res = self.client().delete('/movies/50')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Unprocessable')

    def test_422_delete_actor_do_not_exist(self):
        res = self.client().delete('/actors/50')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Unprocessable')

    def test_patch_movie_success(self):
        res = self.client().patch('/movies/2', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_patch_movie_fail(self):
        res = self.client().patch('/movies/50', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])

    def tets_patch_actor_success(self):
        res = self.client().patch('/actors/2', json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test_patch_actor_fail(self):
        res = self.client().patch('/actors/50', json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
