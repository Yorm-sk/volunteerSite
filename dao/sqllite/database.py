from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from utils.setting import Setting
from utils.logger import Logger


class Database:
    logger = Logger().get_logger(__name__)

    def __init__(self):
        setting = Setting()
        self.engine = create_engine(
            setting.DB_URL,
            echo=True
        )
        self.logger.debug("Engine was created")
        self.session_factory = sessionmaker(self.engine)
        self.logger.debug("Session was created")

    def create_tables(self):
        self.switch_engine_echo()
        Base.metadata.create_all(self.engine)
        self.logger.debug("Tables were created")
        self.switch_engine_echo()

    def drop_tables(self):
        self.switch_engine_echo()
        Base.metadata.drop_all(self.engine)
        self.logger.debug("Tables were dropped")
        self.switch_engine_echo()

    def switch_engine_echo(self):
        if self.engine.echo:
            self.engine.echo = False
            self.logger.info("Echo mode at engine set as False")
        else:
            self.engine.echo = True
            self.logger.info("Echo mode at engine set as True")

    def add_obj(self, obj):
        with self.session_factory() as session:
            session.add(obj)
            session.commit()
            self.logger.info("Object was added")
