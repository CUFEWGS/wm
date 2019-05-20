# -*- coding: utf-8 -*-
# @Time     : 2019/5/20 14:22
# Author    ： Wang Guosong
# @File     : eg_sqlalchemy_ORM.py
# @Software : PyCharm

import sqlalchemy
sqlalchemy.__version__

from sqlalchemy import create_engine
engine = create_engine('sqlite:///E:/Python/sqlite_test/test2', echo=True)
# engine = create_engine('sqlite:///:memory:', echo=True)

# con = engine.execute()

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        if __name__ == '__main__':
            return "<User(name='%s', fullname='%s', nickname"\
            "='%s')>" % (self.name, self.fullname, self.nickname)


User.__tablename__


Base.metadata.create_all(engine)

from sqlalchemy import Sequence
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        if __name__ == '__main__':
            return "<User(name='%s', fullname='%s', nickname"\
            "='%s')>" % (self.name, self.fullname, self.nickname)


ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
ed_user.name
ed_user.nickname
str(ed_user.id)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
session.add(ed_user)

our_user = session.query(User).filter_by(name='ed').all()

session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])


session.query(User).all()

ed_user.nickname = 'eddie'

session.query(User).first()

session.commit()

ed_user.id
session.new

ed_user.name = 'Edwardo'
fake_user = User(name='fakeuser1', fullname='Invalid', nickname='s12345')
session.add(fake_user)
session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser1'])).all()
session.query(User).filter_by(name='fakeuser').all()
session.rollback()

ed_user.name

fake_user in session

session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all()


for instance in session.query(User).\
    order_by(User.name, User.fullname):
    print(instance.name, instance.fullname)

for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)

for row in session.query(User, User.name).all():
    print(row.User, row.name)

session.query(User).filter(User.name.like('%ed')).count()
from sqlalchemy import func
session.query(func.count(User.name), User.name).group_by(User.name).all()


from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


User.addresses = relationship("Address", order_by=Address.id, back_populates="user")

Base.metadata.create_all(engine)

jack =  User(name='jack', fullname='Jack Bean', nickname='gjffdd')
jack.addresses

jack.addresses = [
    Address(email_address='jack@google.com'),
    Address(email_address='j25@yahoo.com')
]

session.add(jack)
session.commit()
session.rollback()