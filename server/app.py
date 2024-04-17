#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import Landmark


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'
@app.route('/landmarks', methods=['GET', 'POST'])
def landmarks():
    if request.method == 'GET':
        landmarks = Landmark.query.all()
        return landmarks
        
    elif request.method == 'POST':
        landmark = Landmark(
            name=request.form['name'],
            description=request.form['description'],
            image_url=request.form['image_url']
        )
        db.session.add(landmark)
        db.session.commit()
        return landmark
    else:
        return 'Invalid request'
    

@app.route('/landmarks/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def landmark(id):
    if request.method == 'GET':
        landmark = Landmark.query.get(id)
        return landmark
    elif request.method == 'PUT':
        landmark = Landmark.query.get(id)
        landmark.name = request.form['name']
        landmark.description = request.form['description']
        landmark.image_url = request.form['image_url']
        db.session.commit()
        return landmark
    elif request.method == 'DELETE':
        landmark = Landmark.query.get(id)
        db.session.delete(landmark)
        db.session.commit()
        return landmark
    else:   
        return 'Invalid request'



if __name__ == '__main__':
    app.run(port=5555, debug=True)

