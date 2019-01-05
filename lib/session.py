from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# TOOD: Config files for conn strings
_AUTH_ENGINE = create_engine("")
_LOBBY_ENGINE = create_engine("")


@contextmanager
def session():
    with \
            _sqlalchemy_session_scope(_AUTH_ENGINE) as auth_session, \
            _sqlalchemy_session_scope(_LOBBY_ENGINE) as lobby_session:

        sess = Session(auth_session, lobby_session)
        try:
            return sess
        finally:
            sess.close()


@contextmanager
def _sqlalchemy_session_scope(engine):
    sess = sessionmaker()(bind=engine)
    failed = False
    try:
        return sess
    except:
        sess.rollback()
        failed = True
        raise
    finally:
        if not failed:
            sess.commit()
        sess.close()


class Session(object):
    def __init__(self, auth_session, lobby_session):
        self._auth = auth_session
        self._lobby = lobby_session
        self._closed = False

    @property
    def auth(self):
        if self._closed:
            raise ValueError("this session is closed")
        return self._auth

    @property
    def lobby(self):
        if self._closed:
            raise ValueError("this session is closed")
        return self._lobby

    def close(self):
        self._closed = True
