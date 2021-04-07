from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


#create Postgres db engine
engine = create_engine('postgresql+psycopg2://test1:password@localhost:5432/planetix', echo=True)
#declare model base
Base = declarative_base(engine)
#create session
Session = scoped_session(sessionmaker(bind=engine))
