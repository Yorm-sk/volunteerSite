from dao.sqllite.base_DAO import BaseDAO
from models.resume import Resume
from utils.logger import Logger


class ResumeDAO(BaseDAO):
    logger = Logger().get_logger(__name__)

    def create_entity(self, resume: Resume):
        with self._session_maker() as session:
            session.add(resume)
            session.commit()
            self.logger.info(f"Resume was added")
