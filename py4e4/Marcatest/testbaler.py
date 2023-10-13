import sqlite3

conn = sqlite3.connect('MarcaNews.db')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Marca;
CREATE TABLE Marca(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	url TEXT ,
	title TEXT,
	news TEXT NOT NULL
);
''')


secondUrl = 'www.nunudeajlhksfja.com'
entireNews = '''
Real Madrid trained on Thursday with one eye on Sunday's match against Eibar at the Estadio Alfredo Di Stefano.
Zinedine Zidane designed a session around physical and tactical work, while he is still unable to count on the 
injured Nacho Fernandez and Luka Jovic.The Frenchman has two more training sessions before deciding on the team 
that will play in Los Blancos' first match after the coronavirus-enforced break.Eden Hazard and Marco Asensio are 
Zidane's two biggest additions, and both have been training with the rest of the squad since Real Madrid returned 
to Valdebebas almost four weeks ago.Zidane has already organised several small-sided matches, including one at the 
Di Stefano to simulate Sunday's match against Eibar as much as possible.Gareth Bale did not play that match because 
of a muscle overload, but he is training like usual and could form part of the front three with Karim Benzema and Eden Hazard.
'''
pasa = 'kjahfs'
bal = 1
cur.execute('''INSERT INTO Marca
        ( news) 
        VALUES ( ?)''', 
        ( entireNews, ))
conn.commit()

cur.close()