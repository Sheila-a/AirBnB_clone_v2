#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, Integer, ForeignKey, String
from sqlalchemy import Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', ForeignKey('places.id'),
                             primary_key=True),
                      Column('amenity_id', ForeignKey('amenities.id'),
                             primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False,)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', backref='place', cascade='delete')
    amenity_ids = []
    amenities = relationship('Amenity', secondary=place_amenity,
                             viewonly=False)

    @property
    def reviews(self):
        """getter attribute to show FileStorge relationship
        between place and reviews"""
        from models import storage
        if type(storage).__name__ == 'FileStorage':
            from models.review import Review
            reviews = storage.all(Review)
            p_revs = []
            for k, v in reviews.items():
                if self.id == v.place_id:
                    p_revs.append(v)
            return p_revs
        else:
            return Place.reviews

    @property
    def amenities(self):
        '''getter attribute to show FileStorge relationship
        between place and reviews'''
        from models import storage
        if type(storage).__name__ == 'FileStorage':
            from models.amenity import Amenity
            amenities = storage.all(Amenity)
            p_amen = []
            for v in amenities.values():
                if v.id in self.amenity_ids:
                    p_amen.append(v)
            return p_amen
        else:
            return Place.amenities

    @amenities.setter
    def amenities(self, ob):
        '''setter attribute to add amenity_id'''
        if type(obj).__name__ == 'Amenity':
            self.amenity_ids.append(ob.id)
