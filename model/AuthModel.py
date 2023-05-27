from config import ENGINE as engine
from sqlalchemy import Column, Integer, String, ForeignKey, func, Boolean
from sqlalchemy.orm import  sessionmaker
from model.BaseModel import Base
import time

class User(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    logged_in = Column(Boolean)

    def __repr__(self):
        return f"<User(username={self.username}, password={self.password}, logged_in={self.logged_in})>"


class UserLog(Base):
    __tablename__ = "user_log"

    user_id = Column(Integer, ForeignKey("user_info.id"))
    logged_in_at = Column(String,primary_key=True)

    def __repr__(self):
        return f"<UserLog(user_id={self.user_id}, logged_in_at={self.logged_in_at})>"


class AuthModel:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def getAllUsername(self):
        return self.session.query(User.username).all()

    def getUser(self, username):
        return self.session.query(User).filter(User.username == username).first()
    
    def getUserLogTime(self, timestamp):
        return self.session.query(UserLog).filter(UserLog.logged_in_at == timestamp).first().logged_in_at

    def validate(self, username, password):
        user = self.getUser(username)
        if user and user.password == password:
            user.logged_in = True
            self.session.commit()
            if self.session.query(func.count(UserLog.user_id)).filter(user.id == UserLog.user_id).scalar() < 10:
               self.addUserLog(user)
            else:
                first = self.session.query(UserLog).filter(user.id == UserLog.user_id).order_by(
                    UserLog.logged_in_at.asc()).first()
                self.session.delete(first)
                self.addUserLog(user)
            self.session.commit()
            return user
        return None
    
    def addUserLog(self, user):
        self.session.add(UserLog(user_id=user.id, logged_in_at=time.strftime('%Y-%m-%d %H:%M:%S')))

    def logout(self, user):
        if user:
            user.logged_in = False
            self.session.commit()

# with engine.connect() as connection:
#     result = connection.execute(text("SELECT * FROM recipes"))
#     print(result.fetchall())