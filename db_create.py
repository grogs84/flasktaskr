# project/db_create.py


import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

	# get a cursor object used to execute sql commands
	c = connection.cursor()

	# create the table
	c.execute("""create table tasks(task_id INTEGER PRIMARY KEY
		AUTOINCREMENT,
		name TEXT NOT NULL, 
		due_date TEXT NOT NULL, 
		priority INTEGER NOT NULL,
		status INTEGER NOT NULL)""")

	# insert dummy data
	c.execute(
		'INSERT INTO tasks (name, due_date, priority, status) \
		VALUES("Finish this tutorial", "3/25/2015", 10, 1)'
		)

	c.execute(
		'INSERT INTO tasks (name, due_date, priority, status) \
		VALUES("Finish real python course 2", "3/25/2015", 10, 1)'
		)