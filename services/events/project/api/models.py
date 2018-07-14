# std stdlib
from datetime import datetime

# local imports
from project import db
from sqlalchemy.dialects.postgresql import ARRAY


class Event(db.Model):
    __tablename__ = "events"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    photo_url = db.Column(db.String(2048), nullable=False)
    event_url = db.Column(db.String(2048), nullable=False)
    description = db.Column(db.String(50000), nullable=False)
    group_name = db.Column(db.String(128), nullable=False)
    member_type = db.Column(db.String(128), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    source = db.Column(db.String(50), nullable=False)

    def __init__(
        self,
        id,
        name,
        created,
        status,
        photo_url,
        event_url,
        description,
        group_name,
        member_type,
        time,
        source,
    ):
        self.id = id
        self.name = name
        self.created = created
        self.status = status
        self.photo_url = photo_url
        self.event_url = event_url
        self.description = description
        self.group_name = group_name
        self.member_type = member_type
        self.time = time
        self.source = source

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "created": self.created.isoformat(),
            "status": self.status,
            "photo_url": self.photo_url,
            "event_url": self.event_url,
            "description": self.description,
            "group_name": self.group_name,
            "member_type": self.member_type,
            "time": self.time.isoformat(),
            "source": self.source,
        }


class Video(db.Model):
    __tablename__ = "videos"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    url = db.Column(db.String(2048), nullable=False)
    description = db.Column(db.String(50000), nullable=False)
    channel = db.Column(db.String(128), nullable=False)
    source = db.Column(db.String(50), nullable=False)

    def __init__(self, id, name, created, url, description, channel, source):
        self.id = id
        self.name = name
        self.created = created
        self.url = url
        self.description = description
        self.channel = channel
        self.source = source

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "created": self.created.isoformat(),
            "url": self.url,
            "description": self.description,
            "channel": self.channel,
            "source": self.source,
        }


class Speaker(db.Model):
    __tablename__ = "speakers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    image = db.Column(db.String(1024), nullable=False)
    contact = db.Column(db.String(128), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.String(128), nullable=False)
    topics = db.Column(ARRAY(db.String), nullable=False)
    diversification = db.Column(db.ARRAY(db.String), nullable=False)
    location = db.Column(db.String(128), nullable=False)
    source = db.Column(db.String(50), nullable=False)

    def __init__(
        self, name, image, contact, role, topics, diversification, location, source
    ):
        self.name = name
        self.image = image
        self.contact = contact
        self.role = role
        self.topics = topics
        self.diversification = diversification
        self.location = location
        self.source = source

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "created": self.created.isoformat(),
            "contact": self.contact,
            "role": self.role,
            "topics": self.topics,
            "diversification": self.diversification,
            "location": self.location,
            "source": self.source,
        }
