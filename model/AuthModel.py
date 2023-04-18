from config import ENGINE as engine
from sqlalchemy import text, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
import psycopg2

Base = declarative_base()

class User(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, password={self.password})>"

class UserModel:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def getUser(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def login(self, username, password):
        user = self.getUser(username)
        if user and user.password == password:
            user.logged_in = True
            self.session.commit()
            return user
        return None

    def logout(self, user):
        user.logged_in = False
        self.session.commit()

# with engine.connect() as connection:
#     result = connection.execute(text("SELECT * FROM recipes"))
#     print(result.fetchall())