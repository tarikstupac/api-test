from datetime import datetime
from src.models.countries import Country
from src.models.users import User
from src.models.transactions import Transaction
from src.models.tiles import Tile
from src.models.transaction_details import TransactionDetail
from db_base import Base, Session, engine


Session.configure(bind=engine)
#---------Create DB-----------------
Base.metadata.create_all(engine)
#--------Create a session-----------


#-------Initialize models-----------

#create a few countries
usa = Country("United States of America", 0, "US", 1.0)
mexico = Country("Mexico", 0, "MEX", 1.0)
canada = Country("Canada", 0, "CA", 1.0)

Session.add(usa)
Session.add(mexico)
Session.add(canada)
Session.commit()

#create a few users
user1 = User("test1", "test1@test.com", "test123", 1, "Test", "Testovic", "+38762000000", 1, 1, "Testoo", usa.id)
user2 = User("test2", "test2@test.com", "test123", 2, "Teston", "Testony", "+38565123123", 1, 1, "Testorony", canada.id)

Session.add(user1)
Session.add(user2)
Session.commit()

#create a few tiles
tile1 = Tile("023113001230003213130", 100.0, "Somewhere, Someplace, USA", 0, 1, 0, datetime.utcnow(), usa.id, user1.id)
tile2 = Tile("023113001230003213132", 100.0, "Somewhere, Someplace, USA", 0, 1, 0, datetime.utcnow(), usa.id, user1.id)
tile3 = Tile("023113001230003213131", 100.0, "Somewhere, Someplace, USA", 0, 1, 0, datetime.utcnow(), usa.id, user1.id)
tile4 = Tile("023113001230003302020", 100.0, "Somewhere, Someplace, USA", 0, 1, 0, datetime.utcnow(), usa.id, user1.id)

Session.add(tile1)
Session.add(tile2)
Session.add(tile3)
Session.add(tile4)
Session.commit()

#---------Commit to DB-------------
Session.close()



