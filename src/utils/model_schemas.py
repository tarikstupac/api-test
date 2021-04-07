from marshmallow import Schema, fields, post_load
from src.models.users import User
from src.models.transactions import Transaction
from src.models.tiles import Tile
from src.models.transaction_details import TransactionDetail


#CountrySchema
class CountrySchema(Schema):
    id = fields.Int()
    name = fields.Str()
    locked = fields.Int()
    code = fields.Str()
    price_multiplier = fields.Float()


#UserSchema
class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()
    status = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()
    phone = fields.Str()
    flag = fields.Int()
    map_style = fields.Int()
    display_name = fields.Str()
    country_id = fields.Int()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

#TransactionSchema
class TransactionSchema(Schema):
    id = fields.Int()
    date_created = fields.DateTime()
    date_processed = fields.DateTime()
    status = fields.Int()
    total_price = fields.Float()
    total_tiles = fields.Int()
    user_id = fields.Int()

    @post_load
    def make_transaction(self, data, **kwargs):
        return Transaction(**data)


#TileSchema
class TileSchema(Schema):
    id = fields.Str()
    base_price = fields.Float()
    location = fields.Str()
    available = fields.Int()
    tile_class = fields.Int()
    for_sale = fields.Int()
    date_changed = fields.DateTime()
    country_id = fields.Int()
    user_id = fields.Int()

    @post_load
    def make_tile(self, data, **kwargs):
        return Tile(**data)

#TransactionDetailSchema
class TransactionDetailSchema(Schema):
    id = fields.Int()
    unit_price = fields.Float()
    transaction_id = fields.Int()
    tile_id = fields.Int()

    @post_load
    def make_transaction_detail(self, data, **kwargs):
        return TransactionDetail(**data)