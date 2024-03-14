from dao.sqllite.worker_DAO import WorkerDAO
from dao.sqllite.resume_DAO import ResumeDAO
from models.worker import Worker
from models.resume import Resume
from enums.workload import Workload
from utils.logger import Logger


if __name__ == "__main__":
    logger = Logger().get_logger(__name__)
    # worker_bobr = Worker(name="bobr")
    # resume = Resume(title="job resume", salary=500, worktable=Workload.parttime,
    #                 worker_id=1)
    worker_DAO = WorkerDAO()
    # resume_DAO = ResumeDAO()
    # worker_DAO._create_tables()
    # worker_DAO.create_entity(worker_bobr)
    # resume_DAO.create_entity(resume)
    # worker_volk = Worker(name="Volk")
    # worker_DAO.create_entity(worker_volk)
    workers = worker_DAO.get_all_workers()
    for worker in workers:
        logger.info(worker)
    logger.info(worker_DAO.get_entity_by_id(1))
    # worker_DAO._drop_tables()
