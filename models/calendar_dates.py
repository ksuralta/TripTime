from sqlalchemy import Column, Integer, String
from base import Base

class CalendarDate(Base):
    __tablename__ = 'calendar_dates'
    service_id = Column(String(80), primary_key=True)
    date = Column(String(32))
    exception_type = Column(Integer)
    def __repr__(self):
        return "<CalendarDate(id='%s')>" % (self.service_id)