"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets, People, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is a name "
    }

    return jsonify(response_body), 200

@app.route('/people', methods=['GET'])
def people_id():
    
    people_y= People.query.all()
   
    people_pl= list(map(lambda x:x.serialize(),people_y))
    
    return jsonify(people_pl), 200

@app.route('/people/<int:id>',methods=["GET"])
def people_detail(id):
    people_id=People.query.filter_by(id)
    return jsonify(people_id.serialize()), 200
    
@app.route('/planets', methods=['GET'])
def planet_data():
    
    planet_query= Planets.query.all()
   
    planet_back= list(map(lambda x:x.serialize(),planet_query))
    
    return jsonify(planet_back), 200

@app.route('/planets/<int:id>',methods=["GET"])
def planet_detail(id):
    planet_id=Planet.query.filter_by(id)
    return jsonify(people_id.serialize()), 200

@app.route('/favorites', methods=['GET'])
def favorites_data():
    
    favorites_query= Favorites.query.all()
   
    favorites_back= list(map(lambda x:x.serialize(),favorites_query))
    
    return jsonify(favorites_back), 200

@app.route('/favorites/<int:id>',methods=["GET"])
def favorites_detail(id):
    favorites_id=Favorites.query.filter_by(id)
    return jsonify(people_id.serialize()), 200
@app.route('/favorites/<int:id>',methods=["DELETE"])
def delete_favorites_detail(id):
    favorites_id=Favorites.query.filter_by(id)
    db.session.delete(favorites_id)
    db.session.commit()
    return jsonify('item deleted success'), 200
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
