-- Keep a log of any SQL queries you execute as you solve the mystery.
-- description of the crime scene.
--bakery!!!! and interviews. 10.15am 3witnesses
SELECT description
FROM crime_scene_reports
WHERE month = 7 AND day = 28
AND street = 'Humphrey Street';

--narrow down suspects to 8
SELECT bakery_security_logs. activity, bakery_security_logs.
license_plate, people.name FROM people
JOIN bakery_security_logs ON bakery_security_logs.license_plate =
people.license_plate
WHERE bakery_security_logs.year = 2021
AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28
AND bakery_security_logs.hour = 10
AND bakery_security_logs.minute >= 15
AND bakery_security_logs.minute <= 25;
--license plate =  can be used to identify thief


--atm at Leggett Street in the monring
--thief called someone who talked to them for less thn a minute. interviewer
--heard thief say take earliest flight out of fiftyville tomorrow.
--the person on call bought the tickets.
--select transcript from interview where month = 7 and day = 28 and year = 2021

 --name and transaction type and narrow down
SELECT people.name, atm_transactions.transaction_type FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.year = 2021
AND atm_transactions.month = 7
AND atm_transactions.day = 28
AND atm_location = "Leggett Street"
AND atm_transactions.transaction_type = "withdraw";

update phone_calls
set caller_name = people.name
from people where phone_calls.caller = people.phone_number;

update phone_calls
set receiver_name = people.name
from people where phone_calls.receiver = people.phone_number;


SELECT caller, caller_name, receiver, receiver_name from phone_calls
where year = 2021
and month = 7
and day = 28
and duration<60;

update flights
set origin_airport_id = airports.city
from airports where flights.origin_airport_id = airports.id;

update flights
set destination_airport_id = airports.city
from airports where flights.destination_airport_id = airports.id;

Select id, hour, minute, origin_airport_id, destination_airport_id from flights
where year = 2021
and month = 7
and day = 29
order by hour asc
limit 1;

SELECT flights.destination_airport_id, name, phone_number,
license_plate from people
JOIN passengers ON people. passport_number= passengers.
passport_number
JOIN flights ON flights.id = passengers.flight_id
WHERE flights.id = 36
ORDER BY flights.hour ASC;