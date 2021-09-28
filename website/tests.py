from flask import request, current_app
import pytest
from . import create_app
#  web-in-flask-notesapp>> python -m pytest -v website/tests.py
app = create_app()

# @pytest.fixture(scope='module')
# def test_app_client():
#     # https://www.youtube.com/watch?v=fq8y-9UHjyk
#     flask_app = create_app()
#     ctx = flask_app.app_context()
#     ctx.push()
#     current_app.logger.info("In the test fixutre... ")
#     ctx.pop()
#     testing_client = flask_app.test_client
#     return testing_client
#     # return flask_app
#     # with flask_app.test_client() as testing_client:
#     #     with flask_app.app_context():
#     #         current_app.logger.info("In the test fixture")
#     #     yield testing_client

# # def test_index_page(test_client):
    

def test_flask():
    assert True

def test_flask_app():
    with app.test_client() as c:
        rv = c.get('/')
        print(rv.get_data())
        assert rv.status_code == 401


# def test_client_app():
#     print("Inside the test client app")
#     # with test_client as c:
#     # print(dir(test_app_client()))
    
#     rv = test_app_client().get('/')
#     print(rv.get_data())
#     assert rv.status_code == 401
