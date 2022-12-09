from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(20), unique=True, nullable=False)
    birth_year = db.Column(db.String(20), unique=False, nullable=False)
    eye_color = db.Column(db.String(14), unique=False, nullable=True)
    gender = db.Column(db.String(10), unique=False, nullable=True)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year":self.birth_year,
            'eye_color':self.eye_color,
            "gender":self.gender,
            # do not serialize the password, its a security breach
        }
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    climate = db.Column(db.String(20), unique=False, nullable=False)
    diameter = db.Column(db.String(28), unique=True, nullable=False)
    gravity = db.Column(db.String(10), unique=False, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.climate

    def serialize(self):
        return {
            "id": self.id,
            "climate": self.email,
            "diameter":self.diameter,
            "gravity":slef.gravity,
            #
        }
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey(User.id))
    PeopleId = db.Column(db.Integer, db.ForeignKey(People.id))
    planetId = db.Column(db.Integer, db.ForeignKey(Planets.id))
    user = db.relationship("User", foreign_keys=[userId])
    people = db.relationship('People')
    planet = db.relationship('Planets')

    def __repr__(self):
        return '<Favorites %r>' % self.user

    def serialize(self):
        return {
            "id": self.id,
            "people": self.character,
            "planet":self.planets,
            #
        }
