#!/usr/bin/python3
"""Start the link class to the  table in db
"""

import sqlalchemy

from sqlalchemy import column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base= declarative_base()

class State(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
