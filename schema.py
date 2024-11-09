from pydantic import BaseModel
from typing import Optional, TypeVar

T = TypeVar('T')



class ResponseSchema(BaseModel):
    details:str
    result: Optional[T] = None
