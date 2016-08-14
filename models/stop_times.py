from sqlalchemy import Column, Integer, String
from base import Base

# stop_times.txt

class StopTime(Base):
    __tablename__ = 'stop_times'
    trip_id = Column(String(80), primary_key=True)
    arrival_time  = Column(String(80))
    departure_time = Column(String(80))
    stop_id = Column(String(80))
    stop_sequence = Column(String(80))
    stop_headsign = Column(String(80))
    pickup_type = Column(String(16))
    drop_off_type = Column(String(16))
    shape_dist_traveled = Column(String(80))
    timepoint = Column(String(80))
    stop_note = Column(String(80))
    def __repr__(self):
        return "<StopTime(id='%s', arrival_time='%s')>" % (self.trip_id, self.arrival_time)