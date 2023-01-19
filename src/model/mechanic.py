from sqlalchemy import Column, Integer, String

from util.db_conexion import Base


# The MechanicModel class inherits from the Base class, which is a declarative base class that will be used to map the
# MechanicModel class to the mechanic table in the database
class MechanicModel(Base):
    __tablename__ = "mechanic"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String(150))
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)
    address = Column(String)
    phone = Column(String)
