# FSNDCapstone: Casting Agency

This project is the capstone of Udacity Full Stack Web Developer Nanodegree project, which should build an online Casting Agency. The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

The Casting Agency Service is hosting on heroku, name is [casting-agency-test](https://casting-agency-test.herokuapp.com/), you can click this url to see hi. The URL is: https://casting-agency-test.herokuapp.com/.

## Endpoints

```bash
GET '/'
GET '/movies'
GET '/movies/<int:movie_id>'
GET '/actors'
GET '/actors/<int:actor_id>'
POST '/movies'
POST '/actors'
PATCH '/movies/<int:movie_id>'
PATCH '/actors/<int:actor_id>'
DELETE '/movies/<int:movie_id>'
DELETE '/actors/<int:actor_id>'
```

## Set Up Authentication

- Paste URL below to web browser and fill the replacements with parameters provided in setup.sh.

```bash
https://{{YOUR_DOMAIN}}/authorize?audience={{API_IDENTIFIER}}&response_type=token&client_id={{YOUR_CLIENT_ID}}&redirect_uri={{YOUR_CALLBACK_URI}}
```

- Sign in with accouts provided below to get token one by one
  - Executive Producer: Because the project has been checked, the account has been deleted
  - Casting Director: Because the project has been checked, the account has been deleted
  - Casting Assistant: Because the project has been checked, the account has been deleted

- Open postman and import collectoins 'CastingAgency.postman_collection.json'

- Use tokens get from step 2 to run test cases one-by-one and you'd better run test cases of Executive Producer first

## Getting Started Locally

### Installing Dependencies

#### Python 3.6

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the /backend directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the requirements.txt file.

#### Running the server locally

From within the ./fsndcapstone directory first ensure you are working using your created virtual environment.Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py
```

To run the server, execute:

```bash
flask run --reload
```

## Specifications

- Models
  - Movies with attributes title and release date
  - Actors with attributes name, age and gender

- Endpoints
  - GET /actors and /movies
  - DELETE /actors/ and /movies/
  - POST /actors and /movies and
  - PATCH /actors/ and /movies/

- Roles
  - Casting Assistant: Can view actors and movies
  - Casting Director: All permissions a Casting Assistant has and add or delete an actor from the database, modify actors or movies
  - Executive Producer: All permissions a Casting Director has and add or delete a movie from the database

- Tests
  - One test for success behavior of each endpoint
  - One test for error behavior of each endpoint
  - At least two tests of RBAC for each role

## Steps

- Create virtual environment: python3 -m venv env
- Create starter code, especially framework of basic test cases
- Finish post movies, actors; get movies, actors; delete movies, actors; patch movies, actors endpoints
- Create account on Auth0, create application, APIs, roles and add corresponding permissions
- Add authentication code and use postman to test RBAC for each role
