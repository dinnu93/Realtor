from sqlalchemy import create_engine,Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Creating an engine for connecting to our database named realtor which is already created.

engine = create_engine('mysql://root:root@localhost/realtor', echo=True)

# Creating the table by making a class

Base = declarative_base()

class Listing(Base):
    __tablename__= 'listings'
    
    street_address = Column(String(200), primary_key=True)
    city = Column(String(50), primary_key=True)
    county = Column(String(50), primary_key=True)
    state_code = Column(String(2), primary_key=True)
    
