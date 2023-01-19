from sqlalchemy import Column, Float, Integer, String

from util.db_conexion import Base


# The AutoPartModel class is a Python class that inherits from the Base class, and has a name, description, price, and
# quantity.
class AutoPartModel(Base):
    __tablename__ = "auto_parts"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
