#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import os


class DBStorage:
    """This class manages storage of hbnb models in db"""
    __engine = None
    __session = None

    def __init__(self):
        from models.base_model import Base
        from models.city import City
        from models.user import User
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity
        from models.place import Place
        u = os.getenv('HBNB_MYSQL_USER')
        p = os.getenv('HBNB_MYSQL_PWD')
        h = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
                           'mysql+mysqldb://{}:{}@{}:3306/{}'
                           .format(u, p, h, db),
                           pool_pre_ping=True)
        env = os.getenv('HBNB_ENV')
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query database for cls"""
        from models.city import City
        from models.state import State
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        dic = {}
        if not cls:
            cls = [City, Review, Place, State, User, Amenity]
        for obj in self.__session.query(cls).all():
            key = f'{type(obj).__name__}.{obj.id}'
            dic[key] = obj
        return dic

    def new(self, obj):
        """add an object to session"""
        self.__session.add(obj)

    def save(self):
        """commit the session to the database"""
        self.__session.commit()

    def delete(self, obj):
        """delete obj from the database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        from models.base_model import Base
        from models.city import City
        from models.state import State
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity

        Base.metadata.create_all(self.__engine)
        factry = sessionmaker(bind=self.__engine)
        Session = scoped_session(factry)
        self.__session = Session()
