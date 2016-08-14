from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import DECIMAL
from base import Base

# stops.txt

class Stop(Base):
    __tablename__ = 'stops'
    stop_id = Column(String(80), primary_key=True)
    stop_code = Column(String(80))
    stop_name = Column(String(256))
    stop_desc = Column(String(256))
    stop_lat = Column(DECIMAL(16, scale=12))
    stop_lon = Column(DECIMAL(16, scale=12))
    zone_id = Column(String(80))
    stop_url = Column(String(80))
    location_type = Column(String(16))
    parent_station = Column(String(80))
    stop_timezone = Column(String(80))
    wheelchair_boarding = Column(Integer)
    platform_code = Column(String(32))
    stop_type = Column(String(16))
    def __repr__(self):
        return "<Stop(id='%s', name='%s')>" % (self.stop_id, self.stop_name)
