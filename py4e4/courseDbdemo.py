import sqlite3


conn = sqlite3.connect('courseDBDemo.sqlite')

cur = conn.cursor()


cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User(
	id			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name 		TEXT(50),
	email		TEXT(50)
);

CREATE TABLE Course(
	id			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title		TEXT(50)
);

CREATE TABLE Member(
	user_id 	INTEGER,
	course_id 	INTEGER,
	role 		INTEGER,
	PRIMARY KEY (user_id, course_id)
);
''')

cur.executescript('''
INSERT INTO User (name,email) VALUES ('Jane', 'jane@suji.org');
INSERT INTO User (name,email) VALUES ('Ed', 'ed@tsugi.org');
INSERT INTO User (name,email) VALUES ('Sue', 'sue@suji.org');
INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('SQL');
INSERT INTO Course (title) VALUES ('PHP');
''') 

cur.executescript('''
INSERT INTO Member (user_id, course_id, role) VALUES (1,1,1);
INSERT INTO Member (user_id, course_id, role) VALUES (2,1,0);
INSERT INTO Member (user_id, course_id, role) VALUES (3,1,0);
INSERT INTO Member (user_id, course_id, role) VALUES (1,2,0);
INSERT INTO Member (user_id, course_id, role) VALUES (2,2,1);
INSERT INTO Member (user_id, course_id, role) VALUES (2,3,1);
INSERT INTO Member (user_id, course_id, role) VALUES (3,3,0);
''')




print('done')
cur.close()
