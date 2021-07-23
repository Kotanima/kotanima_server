## Kotanima Project

The goal of this project is to (almost) automate content management for a VK group.


In short:
1. Images are downloaded from reddit, reddit title is parsed for tags, and comments are parsed for an image source link. This information is  stored in a PostgreSQL database.
2. Django REST API is used for database CRUD + nginx as reverse proxy and for serving static files
3. Kivy android application is used to rate images (like/dislike)
4. Liked images are grouped together and posted to VK.

## Table of contents

- [General info](#general-info)
- [Technologies](#technologies)
- [Deployment](#deployment)

## General info

This repository contains the django REST API code for interacting with the database.


## Hosting

It is hosted on a server with nginx as reverse proxy.
Nginx is also used to serve static files to the checker application.

A self-signed SSL cert is used for the data exchange between android application and the server.

## Technologies

Project is created with:

- Python 3
- `poetry` to manage dependencies
- `django-rest-api` 
- `django-url-filters` for graphql-like access to db
- `djoser` - for token based auth

## Deployment

Deployment is described in detail [here](DEPLOYMENT.md)

## License

[MIT](LICENSE.md)