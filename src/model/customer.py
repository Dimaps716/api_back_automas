from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, Text

from util.db_conexion import Base


# The CustomerModel class inherits from the Base class, which is a declarative base class from the SQLAlchemy library.
class CustomerModel(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String(150))
    email = Column(String(255), unique=True)
    address = Column(String(255))
    phone = Column(String)
    confirm_email = Column(Boolean, default=False)
    image_link = Column(Text())
    country = Column(String)
    identity_document = Column(Integer)
    load_date = Column(TIMESTAMP(timezone=False))
    update_date = Column(TIMESTAMP(timezone=False))
