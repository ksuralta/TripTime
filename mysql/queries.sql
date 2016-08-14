Route names that runs on Monday
--------------------------------
select * from routes where route_id IN (select route_id from trips where service_id IN (select service_id from calendar where monday=1));

Route names that runs on Monday at Parramatta Train Station - Platform 1
------------------------------------------------------------
select * from stop_times where stop_id = '2150411' AND trip_id IN (select trip_id from trips where service_id IN (select service_id from calendar where monday=1));
