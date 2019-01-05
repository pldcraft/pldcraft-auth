from ..entities.lobby import PlayerServerClaim, ServerPlayerClaim
from datetime import datetime

def add_player_server_claim(session, player_id, server_id):
    claim = _player_server_claim(session, player_id)
    claim.server_ids = tuple(sorted(set(claim.server_ids)) )

def _player_server_claim(session, player_id):
    claim = session.lobby.query(PlayerServerClaim).filter(PlayerServerClaim.player_id == player_id).first()
    if not claim:
        claim = PlayerServerClaim(
            expires_at=datetime.now(),
            player_id=player_id,
            server_ids=(),
        )
        session.add(claim)
