# -*- coding: utf-8 -*-
# @Time     : 2019/5/18 16:21
# @Author    ：Wang Guosong
# @File     : eg_query.py
# @Software : PyCharm

import pandas as pd
from sqlalchemy.orm import aliased
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey
Base = declarative_base()

from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:wgs1228@127.0.0.1:3306/test?', echo=True)
engine = create_engine('mysql+pymysql://root:wgs1228@192.168.1.100:3306/test?', echo=True)
engine = create_engine('mysql+pymysql://root:wgs1228@localhost:3306/world', echo=True)
conn = engine.connect()
pd.read_sql("select * from city", conn)
metadata=MetaData(engine)

user=Table('user',metadata,
    Column('id',Integer,primary_key=True),
    Column('name',String(20)),
    Column('fullname',String(40)),
    )
address_table = Table('address', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('user.id')),
    Column('email', String(128), nullable=False)
    )

metadata.create_all()
# engine = create_engine('mysql+pymysql:///root:wgs1228@127.0.0.1/world,port=3306/world', echo=True)
# con = engine.execute()
conn = engine.connect()
pd.read_sql("select * from city", engine)


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

class City(Base):
    __tablename__ = 'city'
    ID = Column(Integer, primary_key=True)
    Name = Column(String)
    CountryCode = Column(String)
    District = Column(String)
    Population = Column(Integer)

included_parts =
