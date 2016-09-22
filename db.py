

from sqlalchemy import create_engine,Column,Integer,String,Date,Text,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql

# Creating the table by making a class

Base = declarative_base()

class Listing(Base):
    __tablename__= 'listings'
    
    street_address = Column(String(200), nullable=False, primary_key=True)
    city = Column(String(50), nullable=False, primary_key=True)
    county = Column(String(50), nullable=False, primary_key=True)
    state_code = Column(String(2), nullable=False, primary_key=True)
    price_dollars = Column(Integer)
    price_dollars_per_sqft = Column(Integer)
    beds = Column(Integer)
    full_baths = Column(Integer)
    half_baths = Column(Integer)
    floor_area_sqft = Column(Integer)
    lot_area_sqft = Column(Integer)
    agent = Column(String(200))
    broker = Column(String(200))
    open_house = Column(Date)
    overview = Column(Text)
    style = Column(Text)
    home_type = Column(Text)
    year_built = Column(mysql.YEAR(4))
    days_on_realtor = Column(Integer)
    status = Column(String(50))
    forclosure = Column(Boolean)
    bank_owned = Column(Boolean)
    


# Creating an engine for connecting to our database named realtor which is already created.

engine = create_engine('mysql://root:root@localhost/realtor', echo=True)
Listing.__table__
Base.metadata.create_all(engine)
