from sqlalchemy import Column, Integer, String
from base import Base

# trips.txt

class Trip(Base):
    __tablename__ = 'trips'
    route_id = Column(String(80), primary_key=True)
    service_id = Column(String(80))
    trip_id = Column(String(80))
    trip_headsign = Column(String(80))
    trip_short_name = Column(String(80))
    direction_id = Column(String(80))
    block_id = Column(String(80))
    shape_id = Column(String(80))
    wheelchair_accessible = Column(String(16))
    bikes_allowed = Column(String(16))
    trip_note = Column(String(80))
    route_direction = Column(String(255))
    def __repr__(self):
        return "<Trip(id='%s', name='%s')>" % (self.route_id, self.trip_short_name)
