from . import db


trees_users = db.Table(
    'trees_users',
    db.Column('tree_id', db.Integer(), db.ForeignKey('tree.id')),
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
)


class Tree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Text())
    latitude = db.Column(db.Text())
    address = db.Column(db.Text())
    common_name = db.Column(db.Text())
    description = db.Column(db.Text())
    date_created = db.Column(db.DateTime())
    # players = db.relationship(
    #     'User',
    #     secondary = trees_users,
    #     backref = db.backref('tree', lazy = 'dynamic')
    # )
