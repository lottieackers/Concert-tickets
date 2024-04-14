CREATE DATABASE concerts;

USE concerts;

CREATE TABLE tour_dates
(tour_id INT NOT NULL PRIMARY KEY, 
artist VARCHAR(30), 
tour_date DATE, 
tickets_available INT);

INSERT INTO tour_dates
(tour_id, artist, tour_date, tickets_available)
VALUES
(1, 'Taylor Swift', '2024-04-22', 10), 
(2, 'Tate Mcrae', '2024-04-22', 9), 
(3, 'Taylor Swift', '2024-04-22', 11), 
(4, 'Beyonce', '2024-04-22', 8), 
(5, 'Taylor Swift', '2024-04-26', 7), 
(6, 'Dermot Kennedy', '2024-04-26', 9), 
(7, 'Taylor Swift', '2024-04-26', 11), 
(8, 'Cher', '2024-05-01', 10), 
(9, 'Tate Mcrae', '2024-05-01', 12), 
(10, 'Dermot Kennedy', '2024-05-01', 8), 
(11, 'Taylor Swift', '2024-05-02', 7), 
(12, 'Beyonce', '2024-05-02', 12), 
(13, 'Dua Lipa', '2024-05-06', 10), 
(14, 'Taylor Swift', '2024-05-06', 10), 
(15, 'Cher', '2024-05-06', 10), 
(16, 'Robbie Williams', '2024-05-06', 10), 
(17, 'Chris Stapleton', '2024-05-10', 9),
(18, 'Tate McRae', '2024-05-10', 9),
(19, 'Teddy Swims', '2024-05-10', 9),
(20, 'Teddy Swims', '2024-05-10', 9);

SELECT * FROM tour_dates;


