import sqlite3

db = sqlite3.connect('Like.db', check_same_thread=False)
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS likes
		(memsURL TEXT,
		like BIGINT,
		dislike BIGINT)
	""")
db.commit()

def get_URL(URL):
	global sql
	global db
	sql.execute(f"SELECT memsURL FROM likes WHERE memsURL = '{URL}'")
	if sql.fetchone() is None:
		sql.execute(f"INSERT INTO likes VALUES (?, ?, ?)", (URL, 0, 0))
		db.commit()
def get_rate(value, URL):
	global sql
	global db
	if value == True:
		sql.execute(f"SELECT like FROM likes WHERE memsURL = '{URL}'")
		balance = sql.fetchone()[0]
		sql.execute(f'UPDATE likes SET like = {1 + balance} WHERE memsURL = "{URL}"')
		db.commit()
	else:
		sql.execute(f"SELECT dislike FROM likes WHERE memsURL = '{URL}'")
		balance = sql.fetchone()[0]
		sql.execute(f"UPDATE likes SET dislike = {1 + balance} WHERE memsURL = '{URL}'")
		db.commit()
def show_DataBase():
	for i in sql.execute(f"SELECT * FROM likes"):
		print(i)


