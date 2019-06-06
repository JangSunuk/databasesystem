import os
import json

from sqlalchemy import Column, String, Integer, Boolean, Date, Table, ForeignKey
from sqlalchemy.orm import relationship, backref

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Seoul(Base):
    __tablename__ = 'seoul'

    id = Column(String(100),primary_key=True)
    population_total = Column(String(100))
    population_man = Column(String(100))
    population_woman = Column(String(100))
    Region = Column(String(100))
    Risk = Column(String(50))

    def __init__(self,id,population_total,population_man, population_woman, Region, Risk):
        self.id = id
        self.population_total =population_total
        self.population_man = population_man
        self.population_woman = population_woman
        self.Region = Region
        self.Risk = Risk
