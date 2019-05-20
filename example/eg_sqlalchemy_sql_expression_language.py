# -*- coding: utf-8 -*-
# @Time     : 2019/5/18 16:21
# Author    ： Wang Guosong
# @File     : eg_sql_expression_language.py
# @Software : PyCharm

import sqlalchemy
sqlalchemy.__version__

from sqlalchemy import create_engine
# engine = create_engine('sqlite:///:memory:', echo = True)
engine = create_engine('sqlite:///D:/E/Python/sqlite_test/test1', echo=True)

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Sequence

metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('fullname', String))

addresses = Table('adresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', None, ForeignKey('users.id')),
                  Column('email_address', String, nullable=False),
                  extend_existing=True)

metadata.create_all(engine)

users = Table('users', metadata,
              Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
              Column('name', String(50)),
              Column('fullname', String(50)),
              Column('nickname', String(50)),
              extend_existing=True
)

ins = users.insert()
str(ins)

ins = users.insert().values(name='jack', fullname='Jack John')
str(ins)

ins.compile().params

conn = engine.connect()
result = conn.execute(ins)

ins.bind = engine
str(ins)

result.inserted_primary_key

ins = users.insert()
conn.execute(ins, id=5, name='wendy', fullname='Wendy Williams')

conn.execute(addresses.insert(), [
    {'user_id' : 1, 'email_address' : 'jack@yahoo.com'},
    {'user_id' : 1, 'email_address' : 'jack@msn.com'},
    {'user_id' : 2, 'email_address' : 'www@www.org'},
    {'user_id' : 2, 'email_address' : 'wendy@aol.com'},
])

from sqlalchemy.sql import select
s = select([users])
s = select([users])
result = conn.execute(s)
result
for row in result:
    print(row)

result = conn.execute(s)
row = result.fetchone()
result.fetchall()

for row in conn.execute(s):
    print("name:", row[users.c.name], "; fullname:", row[users.c.name])

result.close()


s = select([users.c.name, users.c.fullname])
result = conn.execute(s)
for row in result:
    print(row)

s = select([users, addresses]).where(users.c.id == addresses.c.user_id)
for row in conn.execute(s):
    print(row)

print(users.c.id == addresses.c.user_id)

print(users.c.id == 7)
(users.c.id == 7).compile().params

print(users.c.id != 7)
print(users.c.name == None)
print('fred' > users.c.name)

print((users.c.name + users.c.fullname).compile(bind=create_engine('mysql://')))
print(users.c.name + users.c.fullname)

print(users.c.name.op('tiddlywinks')('foo'))

from sqlalchemy import type_coerce
expr = type_coerce(users.c.name.op('-%>')('foo'), String)
stmt = select([expr])

from sqlalchemy.sql import and_, or_, not_
print(and_(
    users.c.name.like('j%'),
    users.c.id == addresses.c.user_id,
    or_(
        addresses.c.email_address == 'wendy@aol.com',
        addresses.c.email_address == 'jack@yahoo.com'
    ),
    not_(users.c.id > 5)
))

print(users.c.name.like('j%') & (users.c.id == addresses.c.user_id) &
      (
          (addresses.c.email_address == 'wendy@aol.com') |
          (addresses.c.email_address == 'jack@yahoo.com')
      )
      & ~(users.c.id > 5)
      )

from sqlalchemy.sql import text, bindparam
s = text(
    "SELECT users.fullname || ', ' || addresses.email_address AS title "
        "FROM users, addresses "
        "WHERE users.id = addresses.user_id "
        "AND users.name BETWEEN :x AND :y "
        "AND (addresses.email_address LIKE :e1 "
            "OR addresses.email_address LIKE :e2)")

conn.execute(s, x='m', y='z', e1='%@aol.com', e2='%@msn.com').fetchall()
[(u'Wendy Williams, wendy@aol.com',)]

stmt = text("SELECT * FROM users WHERE users.name BETWEEN :x AND :y")
stmt = stmt.bindparams(x='m', y='z')

stmt = stmt.bindparams(bindparam('x', type_=String), bindparam("y", type_=String))
result = conn.execute(stmt, {"x": "m", "y": "z"})

print(users.join(addresses))

