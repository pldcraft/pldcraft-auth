from ..entities.lobby import CHALLENGE_SIZE, PlayerServerJoin
from ..session import Session

from datetime import datetime, timedelta

import base64
import os


def _generate_challenge():
    # first, get some characters
    # this length depends on the schema
    basis = os.urandom(CHALLENGE_SIZE // 2)

    # now convert to string for user's convenience + json repr
    return base64.b16encode(basis).decode("utf8").lower()


def request_to_join(session: Session, player_id, server_id):
    join = _find(session, player_id, server_id)
    if join is None:
        join = PlayerServerJoin(player_id=player_id, server_id=server_id)
        session.lobby.add(join)

    challenge = _generate_challenge()

    join.expires_at = datetime.now() + timedelta(minutes=15),
    join.challenge = challenge

    return challenge


def attempt_challenge(session: Session, player_id, server_id, challenge):
    row = _find(session, player_id, server_id).filter(
        PlayerServerJoin.challenge == challenge,
        PlayerServerJoin.expires_at > datetime.now(),
    ).first()

    return row is not None


def _find(session: Session, player_id, server_id=None):
    return session.lobby.query(PlayerServerJoin).filter(
        PlayerServerJoin.player_id == player_id,
        PlayerServerJoin.server_id == server_id,
    )
