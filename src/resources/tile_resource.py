import falcon
import json
from src.utils.db_base import Session
from sqlalchemy.orm import scoped_session, sessionmaker

from src.utils.model_schemas import TileSchema
from src.models.tiles import Tile
from src.models.users import User

db_session = Session()

tile_schema = TileSchema()
tiles_schema = TileSchema(many=True)


class TileGetResource(object):
    pass

class TilesGetResource(object):

    def on_get(self, req, resp, user_id):
        user = db_session.query(User).filter(User.id == user_id).first()
        if user is None:
            resp.status = falcon.HTTP_404
            resp.body = json.dumps({"message":"User with that id does not exist"})
        else:
            tiles = db_session.query(Tile).filter(Tile.user_id == user_id).all()
            if len(tiles) > 0:
                resp.status = falcon.HTTP_200
                resp.body = tiles_schema.dumps(tiles)
            else:
                resp.status = falcon.HTTP_200
                resp.body = json.dumps({"message":"No tiles found for the specified user."})

    def on_post(self, req, resp):
        quadkey_dict = req.get_media(default_when_empty=None)
        if quadkey_dict is None:
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({"message":"Empty request body or malformed//invalid JSON."})
        if len(quadkey_dict.items()) > 0:
            #Implement bulk select query here to return tiles
            print(quadkey_dict.values())
            tiles = db_session.query(Tile).filter(Tile.id.in_(quadkey_dict.values())).all()
            if len(tiles) > 0:
                resp.status = falcon.HTTP_200
                resp.body = tiles_schema.dumps(tiles)
            else:
                resp.status = falcon.HTTP_200
                resp.body = json.dumps({"message":"Tiles with those ids don't exist."})
        else:
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({"message":"The list of quadkeys is empty."})


class TilesInsertResource(object):

    def on_post(self, req, resp):
        tiles = tiles_schema.loads(req.bounded_stream.read())
        print(tiles)
        if len(tiles) > 0:
            for tile in tiles:
                db_session.add(tile)
            try:
                db_session.commit()
                resp.status = falcon.HTTP_201
                resp.body = json.dumps({"message":"Successfully added tiles!"})
            except:
                db_session.rollback()
                resp.status = falcon.HTTP_400
                resp.body = json.dumps({"message":"Problem while adding tiles to db (existing tiles or invalid key)"})
        else:
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({"message":"You need to add at least one tile."})
            
        