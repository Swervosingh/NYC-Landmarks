
from flask import request, session
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import Landmarks

from flask_cors import CORS
from flask import request, jsonify





@app.route('/')
def index():
    return '<h1>Project Server</h1>'
@app.route('/landmarks', methods=['GET', 'POST'])
def landmarks():
    if request.method == 'GET':
        landmarks = Landmarks.query.all()
        landmark_list = [landmark.to_dict() for landmark in landmarks]
        return jsonify(landmark_list), 200
        
    elif request.method == 'POST':
        json_data = request.get_json()

        if not json_data:
            return jsonify({'error': 'No JSON data received'}), 400

        new_landmark = Landmarks(
            name=json_data.get('name'),
            description=json_data.get('description'),
            image_url=json_data.get('image_url')
        )
        try:
            db.session.add(new_landmark)
            db.session.commit()
            return jsonify(new_landmark.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    
    else:
        return 'Invalid request'

@app.route('/landmarks/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def landmark(id):
    if request.method == 'GET':
        landmark = Landmarks.query.filter(Landmarks.id == id).first()

        return landmark.to_dict()
    
    elif request.method == 'PUT':
        landmark = Landmarks.query.get(id)

        landmark.name = request.form['name']
        landmark.description = request.form['description']
        landmark.image_url = request.form['image_url']
        
        db.session.commit()
        return landmark
    elif request.method == 'DELETE':
        landmark = Landmarks.query.get(id)
        db.session.delete(landmark)
        db.session.commit()
        return landmark
    else:   
        return 'Invalid request'
    

    



if __name__ == '__main__':
    app.run(port=5555, debug=True)





