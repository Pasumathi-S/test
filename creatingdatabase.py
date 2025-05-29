import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()


videos = [['packman', 17740, '21-5-2025'],
          ['read from text',46778,'22-5-2025'],
          ['controls top 5',15071,'23-5-2025'],
          ['python excel',80371,'24-5-2025']]
for i in range(len(videos)):
    name = videos[i][0]
    views = videos[i][1]
    date = videos[i][2]
    cursor.execute("INSERT INTO sample VALUES(? ,? ,?)",(name, views, date))

connection.commit()
connection.close()
