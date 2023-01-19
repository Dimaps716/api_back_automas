from typing import Union

from pydantic import BaseModel, Field


# `AutoPart` is a `BaseModel` with `id` and `AutoPartCreate`'s fields
class AutoPartCreate(BaseModel):
    name: Union[str, None] = Field()
    description: Union[str, None] = Field()
    price: Union[float, None] = Field()
    quantity: Union[str, None] = Field()


class AutoPart(AutoPartCreate):
    id: int

    class Config:
        orm_mode = True
