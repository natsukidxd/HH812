-- SQLite
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idno VARCHAR(10) UNIQUE,
    lastname VARCHAR(50),
    firstname VARCHAR(50),
    course VARCHAR(10),
    level VARCHAR(5)
);

PRAGMA TABLE_INFO(students);

INSERT INTO students(idno, lastname, firstname, course, level) VALUES
    ('1000', 'foxtrot', 'zulu', 'bscpe', '4'),
    ('1001', 'xray', 'uniform', 'bscs', '2'),
    ('1002', 'charlie', 'romeo', 'bsit', '2'),
    ('1003', 'romeo', 'november', 'bscs', '1'),
    ('1004', 'alpha', 'bravo', 'bsit', '3');
