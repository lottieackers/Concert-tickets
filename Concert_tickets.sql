CREATE DATABASE concerts;

USE concerts;

CREATE TABLE tour_dates
(tour_id INT NOT NULL PRIMARY KEY, 
artist VARCHAR(30), 
tour_date DATE, 
tickets_available INT);