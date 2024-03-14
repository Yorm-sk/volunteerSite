from sqlalchemy import select

from dao.sqllite.base_DAO import BaseDAO
from models.worker import Worker
from utils.logger import Logger


class WorkerDAO(BaseDAO):
    logger = Logger().get_logger(__name__)

    def create_entity(self, worker: Worker) -> None:
        with self._session_maker() as session:
            session.add(worker)
            session.commit()
            self.logger.info(f"Worker was added")

    def get_entity_by_id(self, worker_id: int) -> Worker:
        with self._session_maker() as session:
            worker = session.get(Worker, worker_id)
            return worker

    def get_all_workers(self) -> [Worker]:
        with self._session_maker() as session:
            return session.execute(select(Worker)).scalars().all()
