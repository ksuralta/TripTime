DROP TABLE stops;
DROP TABLE stop_times;

-- Stops (Stations, Platforms, Wharfs)
CREATE TABLE stops (
id VARCHAR(80),
name VARCHAR(255),
latitude DECIMAL(15, 12),
longitude DECIMAL(15, 12),
location_type INT,
parent_station VARCHAR(80),
wheelchair_boarding INT,
transport_type VARCHAR(20)
);

-- Stop Times / Trips
CREATE TABLE stop_times (
id VARCHAR(80),
arrival_time TIME,
departure_time TIME,
stop_id VARCHAR(15),
stop_sequence INT,
stop_headsign VARCHAR(255),
pickup_type INT,
dropoff_type INT
);

