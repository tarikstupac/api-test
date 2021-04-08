import falcon
import json
from src.utils.model_schemas import UserSchema
from src.models.users import User
from src.utils.db_base import Session
from sqlalchemy.orm import scoped_session, sessionmaker


user_schema = UserSchema()
users_schema = UserSchema(many=True)

db_session = Session()

class UsersResource(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        users = db_session.query(User).all()
        result = users_schema.dumps(users)
        resp.body = result


        
