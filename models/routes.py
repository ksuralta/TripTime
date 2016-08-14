from sqlalchemy import Column, Integer, String
from base import Base

class Route(Base):
    __tablename__ = 'routes'
    route_id = Column(String(80), primary_key=True)
    agency_id = Column(String(80))
    route_short_name = Column(String(128))
    route_long_name = Column(String(256))
    route_desc = Column(String(512))
    route_type = Column(Integer)
    route_url = Column(String(256))
    route_color = Column(String(64))
    route_text_color = Column(String(64))
    def __repr__(self):
        return "<Route(id='%s', name='%s')>" % (self.route_id, self.route_short_name)