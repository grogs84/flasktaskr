# project/db_create.py
from datetime import date

from project import db
from project.models import Task, User


db.create_all()

# # add data
# db.session.add(Task("Finish this tutorial", date(2015,7,1), 10, 1))
# db.session.add(Task("Finish Real Python", date(2015,9,1), 10, 1))

db.session.commit()