from typing import Any
from hotel.db.engine import DBSession
from hotel.db.models import Base, to_dict   # type: ignore


DataObject = dict[str, Any]


class DBInterface:
    def __init__(self, db_class: type[Base]):   # type: ignore
        self.db_class = db_class

    def read_by_id(self, id: int) -> DataObject:
        session = DBSession()
        result = session.query(self.db_class).get(id)  # type: ignore
        return to_dict(result)  # type: ignore

    def read_all(self) -> list[DataObject]:
        session = DBSession()
        results = session.query(self.db_class).all()
        return [to_dict(r) for r in results]

    def create(self, data: DataObject) -> DataObject:
        session = DBSession()
        result = self.db_class(**data)  # type: ignore
        session.add(result)  # type: ignore
        session.commit()
        return to_dict(result)

    def update(self, id: int, data: DataObject) -> DataObject:
        session = DBSession()
        result = session.query(self.db_class).get(id)  # type: ignore
        for key, value in data.items():
            setattr(result, key, value)  # type: ignore
        session.commit()
        return to_dict(result)  # type: ignore

    def delete(self, id: int) -> DataObject:
        session = DBSession()
        result = session.query(self.db_class).get(id)  # type: ignore
        session.delete(result)  # type: ignore
        session.commit()
        return to_dict(result)  # type: ignore
