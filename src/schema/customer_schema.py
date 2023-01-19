from datetime import datetime
from typing import Union

from pydantic import BaseModel, EmailStr, Field


# It creates a class called CustomerCreate that inherits from BaseModel.
class CustomerCreate(BaseModel):
    first_name: Union[str, None] = Field()
    last_name: Union[str, None] = Field()
    email: Union[EmailStr, None] = Field()
    address: Union[str, None] = Field()
    phone: Union[int, None] = Field()
    confirm_email: Union[bool, None] = False
    image_link: Union[str, None] = Field()
    country: Union[str, None] = Field()
    identity_document: Union[int, None] = Field()
    load_date: Union[datetime, None] = Field()
    update_date: Union[datetime, None] = Field()


class Customer(CustomerCreate):
    id: int

    class Config:
        orm_mode = True
