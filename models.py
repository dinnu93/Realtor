
from sqlalchemy import create_engine,Column,Integer,String,Date,Text,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

import settings

# creating a declarative base which derives all the mapping, table generation from the Listing class.
Base = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE), echo=True)

def create_listings_table(engine):
    """
    creates the code for sql schema
    """
    Base.metadata.create_all(engine)


class Listing(Base):
    __tablename__= 'listings'

    url = Column(Text, nullable=False, primary_key=True)
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
    

#engine = create_engine('mysql://root:root@localhost/realtor', echo=True)

engine = db_connect()

# CRUD fuctionality for the listings table

def addListing(listing):
    listingObject = Listing(**listing)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(listingObject)
    session.commit()
    
def addAllListings(listings):
    listingObjects = map(lambda listing: Listing(**listing) ,listings)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add_all(listingObjects)
    session.commit()
    
def readListing():
    pass

def updateListing():
    pass

def removeListing(listing):
    pass 

if __name__=="__main__":
    create_listings_table(engine)


    
