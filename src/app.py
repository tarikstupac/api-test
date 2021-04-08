import falcon
import json
from src.resources.user_resource import UsersResource, UserResource


api = falcon.App()
api.add_route('/users', UsersResource())
api.add_route('/users/{user_id}', UserResource())


if __name__ == "__main__":
   api.run(host="0.0.0.0", debug=True)