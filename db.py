import datetime 
from sqlalchemy import create_engine, Column, Integer, Boolean, Unicode, Sequence, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://greenhouse:greenhouse@postgres:5432/greenhouse", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class DrawerStatus(Base):

    __tablename__ = 'drawer_status'

    id = Column(Integer, 
            Sequence('drawer_status_id_seq'), primary_key=True)
    value = Column(Boolean)
    created_date = Column(DateTime, default=datetime.datetime.utcnow) 

Base.metadata.create_all(engine)