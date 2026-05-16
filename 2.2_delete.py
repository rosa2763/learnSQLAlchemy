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
# to delete id user add the following afer blocking the above if is available
user = session.query(User).filter_by(id=1).one_or_none()
session.delete(user)
session.commit() # run and see the database

