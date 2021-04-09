import falcon
import json
from src.resources.user_resource import UsersResource, UserResource
from src.resources.tile_resource import TilesGetResource, TilesInsertResource


api = falcon.App()
api.add_route('/users', UsersResource())
api.add_route('/users/{user_id}', UserResource())
api.add_route('/tiles/gettilesbyquadkeys', TilesGetResource())
api.add_route('/tiles/{user_id}', TilesGetResource())
api.add_route('/tiles', TilesInsertResource())


if __name__ == "__main__":
   api.run(host="0.0.0.0", debug=True)