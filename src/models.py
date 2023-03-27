import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    created = Column(Date())

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(100), nullable=False)
    character_description = Column(Text(), nullable=True) 

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(100), nullable=False)
    planet_description = Column(Text(), nullable=True) 

class Favorite(Base):
    __tablename__= 'favorite'
    id = Column(Integer, primary_key=True) 
    id_user = Column (Integer, ForeignKey('user.id'))
    id_character = Column (Integer, ForeignKey('character.id'))
    id_planet = Column (Integer, ForeignKey('planet.id'))
    user = relationship(User)
    character = relationship(Character)
    planet = relationship(Planet)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
