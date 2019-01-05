from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import DateTime, Integer, String, Text
from .types import IntTuple

Base = declarative_base()


CHALLENGE_SIZE = 64
assert CHALLENGE_SIZE % 2 == 0

# There's no case where we only fetch *one* of these rows rather than all of them.
# It's faster to delete one row by key than many rows by key.
# So let's fetch these rows blobwise.
class PlayerServerClaim(Base):
    __tablename__ = "player_server_claim"

    id = Column(Integer, primary_key=True)
    expires_at = Column(DateTime)

    player_id = Column(Integer, key=True)
    server_ids = Column(IntTuple)


class ServerPlayerClaim(Base):
    __tablename__ = "server_player_claim"

    id = Column(Integer, primary_key=True)
    expires_at = Column(DateTime)

    server_id = Column(Integer, key=True)
    player_ids = Column(IntTuple)
    reverse_player_ids = Column(IntTuple)


class PlayerServerJoin(Base):
    __tablename__ = "player_server_join"

    id = Column(Integer)
    expires_at = Column(DateTime)

    player_id = Column(Integer, key=True)
    server_id = Column(Integer, key=True)

    challenge = Column(String(CHALLENGE_SIZE))
