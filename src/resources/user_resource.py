import falcon
import json
from src.utils.db_base import Session
from sqlalchemy.orm import scoped_session, sessionmaker

from src.utils.model_schemas import UserSchema
from src.models.users import User



user_schema = UserSchema()
users_schema = UserSchema(many=True)

db_session = Session()

class UsersResource(object):

    def on_get(self, req, resp):
        users = db_session.query(User).all()
        if users is not None:
            result = users_schema.dumps(users)
            resp.status = falcon.HTTP_200
            resp.body = result
        else:
            resp.status = falcon.HTTP_404


class UserResource(object):

    def on_get(self, req, resp, user_id):

        user = db_session.query(User).filter(User.id == user_id).first()
        if user is None:
            resp.status = falcon.HTTP_404
            resp.body = json.dumps({"message":"User with that id does not exist"})
        else:
            result = user_schema.dumps(user)
            resp.status = falcon.HTTP_200
            resp.body = result
                     


    


        
