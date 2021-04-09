from marshmallow import Schema, fields, post_load, validate
from src.models.users import User
from src.models.transactions import Transaction
from src.models.tiles import Tile
from src.models.transaction_details import TransactionDetail


#CountrySchema
class CountrySchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    locked = fields.Int(required=True)
    code = fields.Str(required=True, validate= validate.Length(min=1, max=10))
    price_multiplier = fields.Float(required=True)

    class Meta:
        ordered = True


#UserSchema
class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str(required=True, validate= validate.Length(min=3, max=20))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=8, max=20))
    status = fields.Int(required=True)
    first_name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    last_name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    phone = fields.Str(validate=validate.Length(min=1, max=30))
    flag = fields.Int()
    map_style = fields.Int()
    display_name = fields.Str(validate=validate.Length(min=1,max=20))
    country_id = fields.Int(required=True)
    country = fields.Nested(CountrySchema)

    class Meta:
        ordered = True

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

#TransactionSchema
class TransactionSchema(Schema):
    id = fields.Int()
    date_created = fields.DateTime(required=True)
    date_processed = fields.DateTime(required=True)
    status = fields.Int(required=True)
    total_price = fields.Float(required=True)
    total_tiles = fields.Int(required=True)
    user_id = fields.Int(required=True)
    user = fields.Nested(UserSchema)

    class Meta:
        ordered = True

    @post_load
    def make_transaction(self, data, **kwargs):
        return Transaction(**data)


#TileSchema
class TileSchema(Schema):
    id = fields.Str()
    base_price = fields.Float(required=True)
    location = fields.Str(validate=validate.Length(min=1, max=150))
    available = fields.Int(required=True)
    tile_class = fields.Int(required=True)
    for_sale = fields.Int(required=True)
    date_changed = fields.DateTime()
    country_id = fields.Int(required=True)
    user_id = fields.Int(required=True)


    class Meta:
        ordered = True

    @post_load
    def make_tile(self, data, **kwargs):
        return Tile(**data)

#TransactionDetailSchema
class TransactionDetailSchema(Schema):
    id = fields.Int()
    unit_price = fields.Float(required=True)
    transaction_id = fields.Int(required=True)
    tile_id = fields.Int(required=True)
    tile = fields.Nested(TileSchema)

    class Meta:
        ordered = True

    @post_load
    def make_transaction_detail(self, data, **kwargs):
        return TransactionDetail(**data)