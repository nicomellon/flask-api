from typing import Optional, List

from api import db
from api.models import User

class UserController:

    @staticmethod
    def get_all_users() -> List[dict]:
        return [x.to_dict() for x in User.query.all()]

    @staticmethod
    def add_user(username: str, email: str, password: str) -> User:
        user = User(username=username, email=email, password_hash=password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id: int) -> None:
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()

    @staticmethod
    def update_user(user_id: int, 
                    username: Optional[str] = None, 
                    email: Optional[str] = None, 
                    password: Optional[str] = None) -> User:
        user = User.query.get(user_id)
        if username:
            user.username = username
        if email:
            user.email = email
        if password:
            user.password_hash = password
        db.session.commit()
        return user

