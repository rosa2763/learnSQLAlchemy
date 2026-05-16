#QUERY database
from sqlalchemy.orm import sessionmaker
from models import User,engine
# above models.py is a copy of 1_create_db_table.py

Session = sessionmaker(bind=engine)
session = Session()

user_1 = User(name="Rosa",age="66")
user_2 = User(name="Elviz",age="41")
user_3 = User(name="Nivish",age="37")
user_4 = User(name="Chino",age="41")
user_5 = User(name="Anjana",age="34")
#Carefully select the CURD to see the results
"""
#Add user
session.add(user_1)
session.add_all([user_2,user_3,user_4,user_5])
"""
users = session.query(User).all()
# Many print options
#print(users)
user = users[0]
print(user)
print(user.id)
print(user.name)
print(user.age)
for user in users:
    print(f'user_id: {user.id}, name: {user.name}, age: {user.age}')
user = session.query(User).filter_by(id=1).one_or_none()
print(user)
user = session.query(User).filter_by(age=20).one_or_none()
print(user)
user = session.query(User).filter_by(age=20).all() #if same age  available
print(user)
user = session.query(User).filter_by(age=20).first() #select the first available
print(user)
"""
user_sel = session.query(User).filter_by(id=1).all()
print(user_sel)
user=user_sel[0]
print(user.name)

user = session.query(User).filter_by(id=1).one_or_none()
print(user.name)
user.name = "A different name"
print(user.name)
session.commit() # run and see the database
"""
