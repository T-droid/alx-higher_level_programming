-- List all cities of CA that can be found in db 'hbtn_0d_usa'

SELECT id, name
FROM cities
WHERE state_id = (
      SELECT id
      FROM states
      WHERE name = 'California'
);
