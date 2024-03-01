from dao.sqllite.worker_DAO import WorkerDAO
from models.worker import Worker
from utils.logger import Logger


if __name__ == "__main__":
    logger = Logger().get_logger(__name__)
    worker_bobr = Worker(name="bobr")
    worker_DAO = WorkerDAO()
    worker_DAO._create_tables()
    worker_DAO.create_entity(worker_bobr)
    worker_DAO._drop_tables()
