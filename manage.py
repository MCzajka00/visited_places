from flask_script import Manager, prompt_bool

from visited_places import app, db
from visited_places.models import Bookmark, User

manager = Manager(app)


@manager.command
def init_db():
    db.create_all()

    # db.session.add(Bookmark(url="https://pl.wikivoyage.org/wiki/Split", continent="Europe", country="Croatia", city="Split"))
    db.session.add(User(username="ala", email="a@a.pl", password="test"))

    db.session.commit()

    print("Initialized the db")


@manager.command
def drop_db():
    if prompt_bool("Are you sure you want to lose all your data?"):
        db.drop_all()
        print("Dropped the db")


if __name__ == '__main__':
    manager.run()
