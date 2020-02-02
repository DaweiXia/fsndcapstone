# FSNDCapstone: Casting Agency

This project is the capstone of Udacity Full Stack Web Developer Nanodegree project, which should build an online Casting Agency. The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

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
  -Casting Assistant: Can view actors and movies
  - Casting Director: All permissions a Casting Assistant has and add or delete an actor from the database, modify actors or movies
- Executive Producer: All permissions a Casting Director has and add or delete a movie from the database

- Tests
  - One test for success behavior of each endpoint
  - One test for error behavior of each endpoint
  - At least two tests of RBAC for each role

## Steps

- Create virtual environment: python3 -m venv env
- Create framework of basic test cases
