from typing import Union

from pydantic import BaseModel, EmailStr, Field


# The MechanicCreate class is a subclass of the BaseModel class. It has the following fields: first_name, last_name,
# email, password, role, address, and phone. The Mechanic class is a subclass of the MechanicCreate class. It has the
# following fields: id, first_name, last_name, email, password, role, address, and phone
class MechanicCreate(BaseModel):
    first_name: Union[str, None] = Field()
    last_name: Union[str, None] = Field()
    email: Union[EmailStr, None] = Field()
    password: Union[str, None] = Field()
    role: Union[str, None] = Field()
    address: Union[str, None] = Field()
    phone: Union[int, None] = Field()


class Mechanic(MechanicCreate):
    id: int

    class Config:
        orm_mode = True
