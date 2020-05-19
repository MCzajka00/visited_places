from flask_script import Manager

from visited_places import app, db
from visited_places.models import Bookmark


manager = Manager(app)


@manager.command
def init_db():
    db.create_all()

    db.session.add(Bookmark(url="https://pl.wikivoyage.org/wiki/Split", continent="Europe", country="Croatia", city="Split"))
    db.session.commit()

    print("Initialized the db")


if __name__ == '__main__':
    manager.run()