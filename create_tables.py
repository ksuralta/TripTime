import os
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from models.base import Base
from models import stops, stop_times, trips

env_host = os.environ['MYSQL_HOST']
env_user = os.environ['MYSQL_USER']
env_passwd = os.environ['MYSQL_PASSWD']
env_db = os.environ['MYSQL_DB']

engine = create_engine(''.join(['mysql://', env_user, ':', env_passwd, '@', env_host, '/', env_db]))

Base.metadata.create_all(engine)
