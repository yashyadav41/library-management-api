from sqlalchemy import Column,Integer ,String ,Boolean 
from database import Base 
class Book (Base):
    __tablename__="books"
    id =Column(Integer,primary_key =True)
    title = Column(String)
    author =Column(String)
    available= Column(Boolean ,default=True)



#  this is just practice -----
# from sqlalchemy import Column, Integer, String,Boolean
# from database import Basez
# class stul(Base):
#     __tablename__="bok3"
#     id= Column(Integer,primary=True)
#     title=Column(String)
#     author=Column(String)
#     available=column(Boolean, default=True)


