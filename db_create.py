# project/db_create.py


from views import db
from models import Task
from datetime import date

db.create_all()

# # add data
# db.session.add(Task("Finish this tutorial", date(2015,7,1), 10, 1))
# db.session.add(Task("Finish Real Python", date(2015,9,1), 10, 1))

db.session.commit()