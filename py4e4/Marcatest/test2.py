import sqlite3
conn = sqlite3.connect('MarcaNews.sqlite')
cur = conn.cursor()
cur.executescript('''
CREATE TABLE IF NOT EXISTS Marca(
	id			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	url 		TEXT(200) UNIQUE,
	title 		TEXT(100) UNIQUE,
	news		TEXT(2000)
);
''')
secondUrl = 'https://www.marca.com/en/football/real-madrid/2020/06/12/5ee38f6aca474150528b45e1.html'
try:
	cur.execute('SELECT url FROM Marca WHERE url IN (?)', secondUrl)
except:
	print('pasa')
