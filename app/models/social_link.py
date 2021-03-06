from __future__ import unicode_literals
from future.utils import python_2_unicode_compatible
from utils.compat import u
from app.models import db


@python_2_unicode_compatible
class SocialLink(db.Model):
    __tablename__ = "social_links"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id', ondelete='CASCADE'))
    event = db.relationship("Event", backref="social_link")

    def __init__(self, name=None, link=None, event_id=None):
        self.name = name
        self.link = link
        self.event_id = event_id

    def __repr__(self):
        return '<SocialLink %r>' % self.name

    def __str__(self):
        return u(self.name)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {'id': self.id, 'name': self.name, 'link': self.link}
