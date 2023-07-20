from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

"""db_connectioon_string = """

class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(length=30), nullable=False, unique=True)
    email_address = Column(String(length=255), nullable=False)
    password_hash = Column(String(length=60), nullable=False)


engine = create_engine(db_connectioon_string,connect_args=
                       {
                           "ssl": {
                                "ssl_ca": "/etc/ssl/cert.pem"
                           }
                       })
