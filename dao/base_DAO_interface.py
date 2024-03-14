from abc import ABC, abstractmethod

from models.base import Base


class BaseDAOInterface(ABC):
    @abstractmethod
    def get_entity_by_id(self, ent_id: int):
        pass

    @abstractmethod
    def update_entity(self, entity: Base):
        pass

    @abstractmethod
    def delete_entity(self, entity: Base):
        pass

    @abstractmethod
    def create_entity(self, entity: Base):
        pass
