import sqlite3

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine("sqlite:///database.sqlite3", echo=True)
database = declarative_base()


class Face(database):
    __tablename__ = "faces"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    picture = Column(LargeBinary())

    def __repr__(self):
        return "<Face(id='%s', name='%s', picture='%s')>" % (
            self.id,
            self.name,
            self.picture,
        )


database.metadata.create_all(engine)
