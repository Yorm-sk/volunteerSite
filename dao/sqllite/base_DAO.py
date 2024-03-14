from models.base import Base
from utils.setting import Setting
from utils.logger import Logger
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker


class BaseDAO:
    logger = Logger().get_logger(__name__)

    _engine: Engine
    _session_maker: sessionmaker

    def __init__(self):
        self._create_engine()
        self._create_session_maker(self._engine)

    def _create_engine(self):
        setting = Setting()
        self._engine = create_engine(
            setting.DB_URL,
            echo=True
        )

    def _create_session_maker(self, engine):
        self._session_maker = sessionmaker(engine)

    def _create_tables(self):
        # self._switch_engine_echo()
        Base.metadata.create_all(self._engine)
        self.logger.debug("Tables were created")
        # self._switch_engine_echo()

    def _drop_tables(self):
        # self._switch_engine_echo()
        Base.metadata.drop_all(self._engine)
        self.logger.debug("Tables were dropped")
        # self._switch_engine_echo()

    def _switch_engine_echo(self):
        if self._engine.echo:
            self._engine.echo = False
            self.logger.info("Echo mode at engine set as False")
        else:
            self._engine.echo = True
            self.logger.info("Echo mode at engine set as True")
