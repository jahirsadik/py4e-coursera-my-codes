from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import sqlite3


conn = sqlite3.connect('MarcaNews.sqlite')
cur = conn.cursor()
cur.executescript('''
CREATE TABLE IF NOT EXISTS Marca(
        id                      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        url             TEXT(200) UNIQUE,
        title           TEXT(100) UNIQUE,
        news            TEXT(2000)
);
''')
url = 'https://www.marca.com/en'
html = ''
try: 
        myURL = urlopen(url)
        temp1 = '='
        temp1 *= 20     
        print(temp1, ' RETRIEVED SUCCESSFULLY ', temp1)
        html = myURL.read()
except:
        print('Can\'t retrieve')

print('\n')

soup = BeautifulSoup(html, 'html.parser')
dump = list()
koita = input('Koita?:')
count = int(koita)

for link in soup.find_all('a'):
        if count < 1:
                break
        if link.get('href') is not None:
                secondUrl = link.get('href').strip()
                if secondUrl.startswith('https://www.marca.com/en/football/real-madrid/'):
                        cur.execute('SELECT url FROM Marca WHERE url = (?)', (secondUrl,))
                        nunu = cur.fetchone()
                        if nunu is not None:
                                print('-----------------------------Skipping Existing Links----------------------------------')
                                print('Skipped:', secondUrl)
                                continue
                        if secondUrl[-5:] == '.html':
                                dump.append(secondUrl)
                                print('Retrieving->', secondUrl)
                                try:
                                        count -= 1;
                                        myURL = urlopen(secondUrl)
                                        html2 = myURL.read()
                                        print('Found News!\n\n')
                                        soup2 = BeautifulSoup(html2, 'html.parser')
                                        print('TITLE:' , soup2.title.string)
                                        print('News:\n')
                                        entireNews = ''
                                        for line in soup2.find_all('p'):
                                                print(line.getText())
                                                entireNews += line.getText()
                                                entireNews += '\n'
                                        pasa = soup2.title.string
                                        try:
                                                pos = entireNews.rfind('©')
                                                if pos > 10:
                                                        entireNews = entireNews[:pos]
                                        except:
                                                pass
                                        if entireNews.startswith('Editions:\nEn/football/real-madrid'):
                                                entireNews = entireNews[len('Editions:\nEn/football/real-madrid'):]
                                        print('Inserting into table')
                                        entireNews = "---- TITLE: " + pasa.upper() + "----" + entireNews
                                        try:
                                            cur.execute('INSERT OR REPLACE INTO Marca (url, title, news) VALUES (?,?,?)',(secondUrl, pasa, entireNews))
                                        except:
                                                print('Server Error')
                                except:
                                        print('ERROR Retrieving' , secondUrl)

conn.commit()
cur.close()

