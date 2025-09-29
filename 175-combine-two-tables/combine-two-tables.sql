# Write your MySQL query statement below
SELECT p.firstName,
p.lastName,
a.city,
a.state
FROM PERSON as p
LEFT JOIN ADDRESS as a
on p.personID = a.personID

