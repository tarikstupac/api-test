import falcon
import json
from src.resources.user_resource import UsersResource


api = falcon.App()
api.add_route('/users/', UsersResource())


if __name__ == "__main__":
   api.run(host="0.0.0.0", debug=True)