import random
from sqlalchemy.orm import sessionmaker
from models import User,engine
# above models.py is a copy of 1_create_db_table.py

Session = sessionmaker(bind=engine)
session = Session()
"""
#Run this blocked area first to get data and then block and sort
names = ["Ezri","Ezer","Zadie","Izak","Ezza"]
ages = [12,11,10,9,8,7,6,5,4,3,2]

for x in range(25):
    user = User(name=random.choice(names),age=random.choice(ages))
    session.add(user)

session.commit()
"""
users = session.query(User).order_by(User.age).all()
for user in users:
    print(f"User age:{user.age},name:{user.name},id:{user.id}")

users = session.query(User).order_by(User.age.desc()).all()
for user in users:
    print(f"User age:{user.age},name:{user.name},ID:{user.id}")

users = session.query(User).order_by(User.age,User.name).all()
for user in users:
    print(f"User age:{user.age},name:{user.name},id:{user.id}")