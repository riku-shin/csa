import MySQLdb
import sys

params = {
    'host': 'localhost',
    'db': 'scraping',
    'user': 'scraper',
    'passwd': 'password',
    'charset': 'utf8mb4',
}

conn = MySQLdb.connect(**params)
cursor = conn.cursor(MySQLdb.cursors.DictCursor)

cursor.execute('DROP TABLE IF EXISTS `test`')
cursor.execute("""
    CREATE TABLE `test`(
        `id` INTEGER NOT NULL AUTO_INCREMENT,
        `text` VARCHAR(200) NOT NULL,
        PRIMARY KEY(`id`)
    )
""")
conn.commit()
if len(sys.argv) == 2:
    text = sys.argv[1]
else:
    text = 'test_text'
v = {'text' : text}
cursor.execute('INSERT INTO `test` (`text`) VALUES(%(text)s)', v)
record = cursor.execute('SELECT LAST_INSERT_ID()')
conn.commit()
print(record)
