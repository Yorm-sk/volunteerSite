from dao.sqllite.base_DAO import BaseDAO
from models.worker import Worker
from utils.logger import Logger


class WorkerDAO(BaseDAO):
    logger = Logger().get_logger(__name__)

    def create_entity(self, worker: Worker):
        with self._session_maker() as session:
            session.add(worker)
            session.commit()
            self.logger.info(f"Worker was added")
