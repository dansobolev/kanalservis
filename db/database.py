from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session

from config import Config
from db.models import Base


class DBSession:
    def __init__(self, session: Session):
        self._session = session

    def query(self, *args, **kwargs):
        return self._session.query(*args, **kwargs)

    def add(self, model: Base):
        self._session.add(model)

    def add_all(self, model: Base):
        self._session.add_all(model)

    def delete(self, instance: Base):
        self._session.delete(instance)

    def delete_all(self, table: Base):
        self._session.query(table).delete()

    def commit(self) -> None:
        # TODO: handle possible exceptions
        self._session.commit()


class Database:
    def __init__(self, connection: Engine):
        self.connection = connection
        self.session_factory = sessionmaker(
            self.connection, autocommit=False, autoflush=False
        )

    def make_session(self) -> DBSession:
        session = self.session_factory()
        return DBSession(session)


engine = create_engine(
    Config.DB_URL,
    pool_pre_ping=True,
)


db = Database(engine).make_session()
