from sqlalchemy import Column, Boolean, String
from base import Base

class Calendar(Base):
    __tablename__ = 'calendar'
    service_id = Column(String(80), primary_key=True)
    monday = Column(Boolean)
    tuesday = Column(Boolean)
    wednesday = Column(Boolean)
    thursday = Column(Boolean)
    friday = Column(Boolean)
    saturday = Column(Boolean)
    sunday = Column(Boolean)
    start_date = Column(String(32))
    end_date = Column(String(32))
    def __repr__(self):
        return "<Calendar(id='%s')>" % (self.service_id)
