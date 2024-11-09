from pydantic import BaseModel


class PostCreate(BaseModel):
    title:str
    content:str
    description:str


class RetrievePost(BaseModel):
    id:int
    title:str
    content: str
    description:str